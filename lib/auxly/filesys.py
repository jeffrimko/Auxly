"""Library of functions related to file system contents and manipulation."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import atexit
import codecs
import hashlib
import os
import os.path as op
import re
import shutil
import sys
from datetime import datetime

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Default file encoding.
ENCODING = "utf-8"

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class Cwd(object):
    """Class to handle changing current working directory. Can
    be used as a context manager.

    **Examples**:
    ::
        with auxly.filesys.Cwd(auxly.filesys.homedir()):  # Temporarily set CWD.
            pass  # Do stuff here...

        with auxly.filesys.Cwd("..") as cwd:  # Temporarily set CWD.
            cwd.path      # The current working directory.
            cwd.original  # The original working directory.
    """
    def __init__(self, path=".", root=None):
        #: The new/current working directory path.
        self.path = os.getcwd()
        #: The original working directory path.
        self.original = self.path
        if path:
            if not op.isabs(path):
                path = abspath(path, root=root)
            if op.isfile(path):
                path = op.dirname(path)
            if op.isdir(path):
                self.path = path
            os.chdir(self.path)
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        os.chdir(self.original)
    def __getattr__(self, name):
        return getattr(self.path, name)
    def __repr__(self):
        return self.path

class Path(str):
    def __new__(cls, path, *extrapath):
        return super(Path, cls).__new__(cls, op.abspath(op.join(path, *extrapath)))
    def __init__(self, *path):
        self._fspath = op.abspath(op.join(*path))
    def __add__(self, value):
        return Path(self._fspath + value)
    def __repr__(self):
        return self._fspath
    def isdir(self):
        """Returns true if object is directory, otherwise false."""
        return op.isdir(self._fspath)
    def isfile(self):
        """Returns true if object is file, otherwise false."""
        return op.isfile(self._fspath)
    @property
    def name(self):
        """Returns the base name of the path."""
        return op.basename(self._fspath)
    @property
    def parent(self):
        """Returns a ``Path`` for the parent directory of this object."""
        return Path(op.dirname(self._fspath))
    def join(self, relpath):
        """Returns a ``Path`` of the given relative path joined with this
        object."""
        return Path(self, relpath)
    def exists(self):
        """Returns true if object exists, otherwise false."""
        return op.exists(self._fspath)
    def isempty(self):
        """Returns true if object is empty, otherwise false."""
        return isempty(self._fspath)
    def created(self):
        """Returns the object created date/time."""
        try:
            return datetime.fromtimestamp(op.getctime(self._fspath))
        except:
            return None
    def modified(self):
        """Returns the object modified date/time."""
        try:
            return datetime.fromtimestamp(op.getmtime(self._fspath))
        except:
            return None
    def size(self):
        """Returns the size of the object in bytes."""
        try:
            return getsize(self._fspath, recurse=True)
        except:
            return None

class File(Path):
    """Object representing a file system file. The ENCODING variable defines the
    default encoding."""
    def __init__(self, path, *extrapath, **kwargs):
        """Creates a file object for the given path.

        **Params:**
          - path (str) - Path to the file. Multiple values will be passed to
            `os.path.join()`.
          - del_at_exit (bool) [kwargs] - If true, the file will be deleted when the
            script exits.
        """
        if not path:
            raise ValueError("no path provided")
        if isinstance(path, Path):
            path = path._fspath
        super(File, self).__init__(path, *extrapath, **kwargs)
        if self.exists() and self.isdir():
            raise TypeError("file cannot be dir")
        del_at_exit = kwargs.get('del_at_exit')
        if del_at_exit:
            atexit.register(self.delete)
        toks = op.basename(path)
        self.stem = op.splitext(toks)[0]
        self.ext = op.splitext(toks)[1]
    def __add__(self, value):
        return File(self._fspath + value)
    def read(self, encoding=None):
        """Reads from the file and returns result as a string."""
        encoding = encoding or ENCODING
        try:
            with codecs.open(self, encoding=encoding) as fi:
                return fi.read()
        except:
            return None
    def readlines(self, encoding=None):
        """Reads from the file and returns result as a list of lines."""
        try:
            encoding = encoding or ENCODING
            with codecs.open(self, encoding=encoding) as fi:
                return fi.readlines()
        except:
            return []
    def _write(self, content, mode, encoding=None, linesep=False):
        """Handles file writes."""
        makedirs(self)
        try:
            encoding = encoding or ENCODING
            if "b" not in mode:
                try:
                    content = str(content)
                except:
                    pass
                if linesep:
                    content += os.linesep
            with codecs.open(self, mode, encoding=encoding) as fo:
                fo.write(content)
                return True
        except:
            return False
    def append(self, content, binary=False, encoding=None):
        """Appends the given content to the file. Existing content is
        preserved. Returns true if successful, otherwise false."""
        mode = "ab" if binary else "a"
        return self._write(content, mode, encoding=encoding, linesep=False)
    def appendline(self, content, binary=False, encoding=None):
        """Same as `append()` but adds a line break after the content."""
        mode = "ab" if binary else "a"
        return self._write(content, mode, encoding=encoding, linesep=True)
    def write(self, content, binary=False, encoding=None):
        """Writes the given content to the file. Existing content is
        deleted. Returns true if successful, otherwise false."""
        mode = "wb" if binary else "w"
        return self._write(content, mode, encoding=encoding, linesep=False)
    def writeline(self, content, binary=False, encoding=None):
        """Same as `write()` but adds a line break after the content."""
        mode = "wb" if binary else "w"
        return self._write(content, mode, encoding=encoding, linesep=True)
    def empty(self):
        """Erases/empties the content in a file but does not delete it."""
        return self.write("")
    def delete(self):
        """Deletes the file. Returns true if successful, otherwise false."""
        return delete(self)
    def checksum(self, **kwargs):
        """Returns the checksum of the file."""
        return checksum(self, **kwargs)

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def _is_match(regex, text):
    """Returns true if the given text matches the given regex pattern."""
    try:
        return re.compile(regex).search(text) != None
    except:
        return False

def abspath(relpath, root=None):
    """Returns an absolute path based on the given root and relative path."""
    root = root or cwd()
    if op.isfile(root):
        root = op.dirname(root)
    return op.abspath(op.join(root, relpath))

def homedir():
    """Returns the path to the current user's home directory."""
    return op.expanduser("~")

def cwd(path=None, root=None):
    """Returns the CWD and optionally sets it to the given path.
    **Examples**:
    ::
        print(auxly.filesys.cwd())  # Get the CWD.
        auxly.filesys.cwd("foo")  # Set the CWD to `foo`.
    """
    return Cwd(path, root=root).path

def makedirs(path, ignore_extsep=False):
    """Makes all directories required for given path; returns true if successful
    otherwise false.

    **Examples**:
    ::
        auxly.filesys.makedirs("bar/baz")
    """
    if not ignore_extsep and op.basename(path).find(os.extsep) > -1:
        path = op.dirname(path)
    try:
        os.makedirs(path)
    except:
        return False
    return True

def delete(path, regex=None, recurse=False, test=False):
    """Deletes the file or directory at `path`. If `path` is a directory and
    `regex` is provided, matching files will be deleted; `recurse` controls
    whether subdirectories are recursed. A list of deleted items is returned.
    If `test` is true, nothing will be deleted and a list of items that would
    have been deleted is returned.
    """
    deleted = []
    if op.isfile(path):
        if not test: os.remove(path)
        else: return [path]
        return [] if op.exists(path) else [path]
    elif op.isdir(path):
        if regex:
            for r,ds,fs in os.walk(path):
                for i in fs:
                    if _is_match(regex, i):
                        deleted += delete(op.join(r,i), test=test)
                if not recurse:
                    break
        else:
            if not test: shutil.rmtree(path)
            else: return [path]
            return [] if op.exists(path) else [path]
    return deleted

def walkfiles(startdir, regex=None, recurse=True, regex_entire=True):
    """Yields Path object for files found within the given start
    directory. Can optionally filter paths using a regex pattern, either on the
    entire path if regex_entire is true otherwise on the file name only."""
    if sys.version_info >= (3, 6):
        startdir = op.abspath(startdir)
        with os.scandir(startdir) as it:
            for i in it:
                if i.is_file():
                    if regex:
                        path = op.join(startdir, i.name)
                        n = path if regex_entire else i.name
                        if _is_match(regex, n):
                            yield Path(path)
                    else:
                        yield op.join(startdir, i.name)
                elif recurse:
                    for j in walkfiles(op.join(startdir, i.name), regex, recurse, regex_entire):
                        yield Path(j)
    else:
        for r,_,fs in os.walk(startdir):
            if not recurse and startdir != r:
                return
            for f in fs:
                path = op.abspath(op.join(r,f))
                n = path if regex_entire else f
                if regex and not _is_match(regex, n):
                    continue
                if op.isfile(path):
                    yield Path(path)

def walkdirs(startdir, regex=None, recurse=True, regex_entire=True):
    """Yields Path object for directories found within the given start
    directory. Can optionally filter paths using a regex pattern, either on the
    entire path if regex_entire is true otherwise on the directory name only."""
    if sys.version_info >= (3, 6):
        startdir = op.abspath(startdir)
        with os.scandir(startdir) as it:
            for i in it:
                if i.is_dir():
                    if regex:
                        path = op.join(startdir, i.name)
                        n = path if regex_entire else op.basename(i.name)
                        if _is_match(regex, n):
                            yield Path(path)
                    else:
                        yield Path(startdir, i.name)
                    if recurse:
                        for j in walkdirs(op.join(startdir, i.name), regex, recurse, regex_entire):
                            yield Path(j)
    else:
        for r,ds,_ in os.walk(startdir):
            if not recurse and startdir != r:
                return
            for d in ds:
                path = op.abspath(op.join(r,d))
                n = path if regex_entire else d
                if regex and not _is_match(regex, n):
                    continue
                if op.isfile(path):
                    yield Path(path)

def countfiles(path, recurse=False):
    """Returns the number of files under the given directory path."""
    if not op.isdir(path):
        return 0
    count = 0
    for r,ds,fs in os.walk(path):
        count += len(fs)
        if not recurse:
            break
    return count

def countdirs(path, recurse=False):
    """Returns the number of directories under the given directory path."""
    if not op.isdir(path):
        return 0
    count = 0
    for r,ds,fs in os.walk(path):
        count += len(ds)
        if not recurse:
            break
    return count

def isempty(path):
    """Returns true if the given file or directory path is empty.

    **Examples**:
    ::
        auxly.filesys.isempty("foo.txt")  # Works on files...
        auxly.filesys.isempty("bar")  # ...or directories!
    """
    if op.isdir(path):
        return [] == os.listdir(path)
    elif op.isfile(path):
        return 0 == os.stat(path).st_size
    return None

def getsize(path, recurse=False):
    """Returns the size of the file or directory in bytes."""
    if not op.isdir(path):
        return op.getsize(path)
    size = 0
    for r,_,fs in os.walk(path):
        for f in fs:
            size += getsize(op.join(r,f))
        if not recurse:
            break
    return size

def copy(srcpath, dstpath, overwrite=True):
    """Copies the file or directory at `srcpath` to `dstpath`. Returns true if
    successful, otherwise false."""
    # Handle bail conditions.
    if not op.exists(srcpath):
        return False
    if not overwrite:
        if op.isfile(dstpath):
            return False
        if op.isdir(dstpath):
            chkpath = op.join(dstpath, op.basename(srcpath))
            if op.isdir(chkpath) or op.isfile(chkpath):
                return False
    srcpath = op.abspath(srcpath)
    dstpath = op.abspath(dstpath)

    # Handle copying.
    if op.isdir(srcpath):
        dstdir = dstpath
        if op.isfile(dstpath):
            dstdir = op.dirname(dstpath)
        elif op.isdir(dstpath):
            # Make sure srcdir is copied INTO dstdir.
            dstdir = op.join(dstpath, op.basename(srcpath))
        makedirs(dstdir)
        for r,ds,fs in os.walk(srcpath):
            basedir = r.replace(srcpath, "").rstrip(os.sep).strip(os.sep)
            curdir = op.join(dstdir, basedir)
            makedirs(curdir)
            for f in fs:
                if not copy(op.join(r,f), op.join(curdir, f), overwrite=overwrite):
                    return False
    elif op.isfile(srcpath):
        dstdir = dstpath
        if op.basename(srcpath).count(".") == 0 and op.basename(srcpath) == op.basename(dstpath):
            # NOTE: This is a special condition to prevent creating an extra
            # directory in a scenario where the srcpath is a file without an
            # extension. For example, if `C:\LICENSE` is the srcpath and
            # `C:\foo\LICENSE` is the dstpath, this will prevent creating a
            # directory named `C:\foo\LICENSE` and then copying the `LICENSE`
            # to that directory.
            dstdir = op.dirname(dstpath)
        makedirs(dstdir)
        shutil.copy2(srcpath, dstpath)

    return op.exists(dstpath)

def move(srcpath, dstpath, overwrite=True):
    """Moves the file or directory at `srcpath` to `dstpath`. Returns true if
    successful, otherwise false."""
    # TODO: (JRR@201612230924) Consider adding smarter checks to prevent files ending up with directory names; e.g. if dstpath directory does not exist.
    srcpath = op.abspath(srcpath)
    dstpath = op.abspath(dstpath)
    if not op.exists(srcpath):
        return False
    if srcpath == dstpath:
        return True
    if op.isfile(srcpath) and op.isdir(dstpath):
        verfunc = op.isfile
        verpath = op.join(dstpath, op.basename(srcpath))
    elif op.isfile(srcpath):
        verfunc = op.isfile
        verpath = dstpath
        makedirs(dstpath)
    elif op.isdir(srcpath) and op.isdir(dstpath):
        verfunc = op.isdir
        verpath = op.join(dstpath, op.basename(srcpath))
    elif op.isdir(srcpath):
        verfunc = op.isdir
        verpath = dstpath
    else:
        return False
    if op.isfile(verpath):
        if not overwrite:
            return False
        else:
            # On Windows, file name case is ignored so the following check will
            # prevent unintentionally deleting the srcpath before moving.
            if "nt" == os.name and srcpath.lower() == dstpath.lower():
                pass
            elif not delete(verpath):
                return False
    try:
        shutil.move(srcpath, dstpath)
    except:
        return False
    return verfunc(verpath)

def checksum(fpath, hasher=None, asbytes=False):
    """Returns the checksum of the file at the given path as a hex string
    (default) or as a bytes literal. Uses MD5 by default.

    **Attribution**:
    Based on code from
    `Stack Overflow <https://stackoverflow.com/a/3431835/789078>`_."""
    def blockiter(fpath, blocksize=0x1000):
        with open(fpath, "rb") as afile:
            block = afile.read(blocksize)
            while len(block) > 0:
                yield block
                block = afile.read(blocksize)
    try:
        hasher = hasher or hashlib.md5()
        for block in blockiter(fpath):
            hasher.update(block)
        return (hasher.digest() if asbytes else hasher.hexdigest())
    except:
        return None

def rootdir():
    """Returns the system root directory."""
    return os.path.abspath(os.sep)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

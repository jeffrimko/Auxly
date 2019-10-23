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
            pass  # do stuff here...
    """
    def __init__(self, path=".", root=None):
        self.path = os.getcwd()
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

class _FileSysObject(object):
    def __init__(self, *path):
        self._fspath = op.join(*path)
    def isfile(self):
        """Returns true if object is file, false otherwise."""
        return op.isfile(self._fspath)
    def isdir(self):
        """Returns true if object is directory, false otherwise."""
        return op.isdir(self._fspath)
    def dirpath(self):
        """Returns a Path object for the directory associated with this object."""
        if self.isfile():
            return Path(op.dirname(self._fspath))
        else:
            return Path(self)
    def exists(self):
        """Returns true if object exists, false otherwise."""
        return op.exists(self._fspath)
    def isempty(self):
        """Returns true if object is empty, false otherwise."""
        return isempty(self._fspath)
    def created(self):
        """Returns the object created date/time."""
        return datetime.fromtimestamp(op.getctime(self._fspath))
    def modified(self):
        """Returns the object modified date/time."""
        return datetime.fromtimestamp(op.getmtime(self._fspath))
    def size(self):
        """Returns the size of the object in bytes."""
        return getsize(self._fspath, recurse=True)

class Path(_FileSysObject, str):
    """Object representing a filesystem path."""
    def __new__(cls, *content):
        return super(Path, cls).__new__(cls, op.abspath(op.join(*content)))
    def __init__(self, *path):
        super(Path, self).__init__(self)
        self.parse()
    def parse(self):
        self.dir = None
        self.file = None
        self.ext = None
        if op.isdir(self):
            self.dir = self
        elif op.isfile(self):
            base = op.basename(self)
            self.dir = op.dirname(self)
            self.filename = base
            self.file = op.splitext(base)[0]
            self.ext = op.splitext(base)[1]
    def join(self, relpath):
        """Joins the given relative path with this path."""
        return Path(self, relpath)

class File(_FileSysObject):
    """Object representing a filesystem file. The ENCODING variable defines the
    default encoding."""
    def __init__(self, *path, **kwargs):
        """Creates a file object for the given path.

        **Params:**
          - path (str) - Path to the file. Multiple values will be passed to
            `os.path.join()`.
          - del_at_exit (bool) [kwargs] - If true, the file will be deleted when the
            script exits.
        """
        self.path = Path(*path)
        if self.path.exists() and self.path.isdir():
            raise Exception("AuxlyExceptionFileCannotBeDir")
        super(File, self).__init__(self.path)
        del_at_exit = kwargs.get('del_at_exit')
        if del_at_exit:
            atexit.register(self.delete)
    def __repr__(self):
        return self.path
    def read(self, encoding=None):
        """Reads from the file and returns result as a string."""
        encoding = encoding or ENCODING
        try:
            with codecs.open(self.path, encoding=encoding) as fi:
                return fi.read()
        except:
            return None
    def readlines(self, encoding=None):
        """Reads from the file and returns result as a list of lines."""
        try:
            encoding = encoding or ENCODING
            with codecs.open(self.path, encoding=None) as fi:
                return fi.readlines()
        except:
            return []
    def _write(self, content, mode, encoding=None, linesep=False):
        """Handles file writes."""
        makedirs(self.path)
        try:
            encoding = encoding or ENCODING
            if "b" not in mode:
                try:
                    content = str(content)
                except:
                    pass
                if linesep:
                    content += os.linesep
            with codecs.open(self.path, mode, encoding=encoding) as fo:
                fo.write(content)
                return True
        except:
            return False
    def append(self, content, binary=False, encoding=None):
        """Appends the given content to the file. Existing content is
        preserved. Returns true if successful, false otherwise."""
        mode = "ab" if binary else "a"
        return self._write(content, mode, encoding=encoding, linesep=False)
    def appendline(self, content, binary=False, encoding=None):
        """Same as `append()` but adds a line break after the content."""
        mode = "ab" if binary else "a"
        return self._write(content, mode, encoding=encoding, linesep=True)
    def write(self, content, binary=False, encoding=None):
        """Writes the given content to the file. Existing content is
        deleted. Returns true if successful, false otherwise."""
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
        """Deletes the file. Returns true if successful, false otherwise."""
        return delete(self.path)
    def checksum(self, **kwargs):
        """Returns the checksum of the file."""
        return checksum(self.path, **kwargs)

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
    and false otherwise.

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

def walkfiles(startdir, regex=None, recurse=True):
    """Yields the absolute paths of files found within the given start
    directory. Can optionally filter paths using a regex pattern."""
    startdir = op.abspath(startdir)
    with os.scandir(startdir) as it:
        for i in it:
            if i.is_file():
                if regex:
                    n = op.join(startdir, i.name)
                    if _is_match(regex, n):
                        yield n
                else:
                    yield op.join(startdir, i.name)
            elif recurse:
                for j in walkfiles(op.join(startdir, i.name), regex, recurse):
                    yield j

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
    """Returns True if the given file or directory path is empty.

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
    """Copies the file or directory at `srcpath` to `dstpath`. Returns True if
    successful, False otherwise."""
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
        makedirs(dstpath)
        shutil.copy2(srcpath, dstpath)

    return op.exists(dstpath)

def move(srcpath, dstpath, overwrite=True):
    """Moves the file or directory at `srcpath` to `dstpath`. Returns True if
    successful, False otherwise."""
    # TODO: (JRR@201612230924) Consider adding smarter checks to prevent files ending up with directory names; e.g. if dstpath directory does not exist.
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
            # On Windows, filename case is ignored so the following check will
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
    hasher = hasher or hashlib.md5()
    for block in blockiter(fpath):
        hasher.update(block)
    return (hasher.digest() if asbytes else hasher.hexdigest())

def rootdir():
    """Returns the system root directory."""
    return os.path.abspath(os.sep)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

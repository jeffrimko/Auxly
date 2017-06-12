"""Library of functions related to file system contents and manipulation."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import atexit
import os
import os.path as op
import re
import shutil

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class Cwd(object):
    """Class to handle changing current working directory. Can
    be used as a context manager."""
    def __init__(self, newpath=""):
        self.path = os.getcwd()
        self.original = self.path
        if newpath:
            if not op.isabs(newpath):
                newpath = op.abspath(newpath)
            if op.isfile(newpath):
                newpath = op.dirname(newpath)
            if op.isdir(newpath):
                self.path = newpath
            os.chdir(self.path)
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        os.chdir(self.original)
    def __getattr__(self, name):
        return getattr(self.path, name)
    def __repr__(self):
        return self.path

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def abspath(relpath, root=__file__):
    """Returns an absolute path based on the given root and relative path."""
    if op.isfile(root):
        root = op.dirname(root)
    return op.abspath(op.join(root, relpath))

def homedir():
    """Returns the path to the current user's home directory."""
    return op.expanduser("~")

def cwd(path=None):
    """Returns the CWD and optionally sets it to the given path."""
    return Cwd(path).path

def makedirs(path, ignore_extsep=False):
    """Makes all directories required for given path; returns true if successful
    and false otherwise."""
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
            try:
                ptrn = re.compile(regex)
            except:
                return []
            for r,ds,fs in os.walk(path):
                for i in fs:
                    if ptrn.search(i):
                        deleted += delete(op.join(r,i), test=test)
                if not recurse:
                    break
        else:
            if not test: shutil.rmtree(path)
            else: return [path]
            return [] if op.exists(path) else [path]
    return deleted

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
    """Returns True if the given file or directory path is empty."""
    if op.isdir(path):
        return [] == os.listdir(path)
    elif op.isfile(path):
        return 0 == os.stat(path).st_size
    return None

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

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

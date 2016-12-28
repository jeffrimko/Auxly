"""Library of functions related to file system contents and manipulation."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import os.path as op
import re
import shutil

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

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

    # Make dirs if needed.
    ies = op.isdir(srcpath)
    makedirs(dstpath, ignore_extsep=ies)

    # Handle copying.
    if op.isdir(srcpath):
        if op.isdir(srcpath) or op.isdir(dstpath):
            dstdir = dstpath
        elif "" != op.splitext(dstpath)[1]:
            dstdir = op.dirname(dstpath)
        else:
            dstdir = dstpath
        for r,ds,fs in os.walk(srcpath):
            for f in fs:
                if not copy(op.join(r,f), op.join(dstdir, r, f), overwrite=overwrite):
                    return False
    elif op.isfile(srcpath):
        shutil.copy2(srcpath, dstpath)
    return op.exists(dstpath)

def move(srcpath, dstpath, overwrite=True):
    """Moves the file or directory at `srcpath` to `dstpath`. Returns True if
    successful, False otherwise."""
    # TODO: (JRR@201612230924) Consider adding smarter checks to prevent files ending up with directory names; e.g. if dstpath directory does not exist.
    if not op.exists(srcpath):
        return False
    if op.isfile(srcpath) and op.isdir(dstpath):
        verfunc = op.isfile
        verpath = op.join(dstpath, op.basename(srcpath))
    elif op.isdir(srcpath) and op.isdir(dstpath):
        verfunc = op.isdir
        verpath = op.join(dstpath, op.basename(srcpath))
    elif op.isfile(srcpath):
        verfunc = op.isfile
        verpath = dstpath
        makedirs(dstpath)
    else:
        return False
    if os.path.isfile(verpath):
        if not overwrite:
            return False
        else:
            if not delete(verpath):
                return False
    try:
        shutil.move(srcpath, dstpath)
    except:
        return False
    return verfunc(verpath)

def makedirs(path, ignore_extsep=False):
    """Makes all directories required for given path; returns true if successful
    and false otherwise."""
    if not ignore_extsep and os.path.basename(path).find(os.extsep) > -1:
        path = os.path.dirname(path)
    try:
        os.makedirs(path)
    except:
        return False
    return True

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

"""Library of functions related to file system contents and manipulation."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import re
import os.path as op
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

def is_empty(path):
    """Returns True if the given file or directory path is empty."""
    if op.isdir(path):
        return [] == os.listdir(path)
    elif op.isfile(path):
        return 0 == os.stat(path).st_size
    return None

def copy(srcpath, dstpath):
    """Copies the file or directory at `srcpath` to `dstpath`. Returns True if
    successful, False otherwise."""
    if not op.exists(srcpath):
        return False
    if op.isdir(dstpath):
        dstdir = dstpath
    elif "" != op.splitext(dstpath)[1]:
        dstdir = op.dirname(dstpath)
    else:
        dstdir = dstpath
    if dstdir and not op.isdir(dstdir):
        if not makedirs(dstdir):
            return False
    if op.isdir(srcpath):
        for r,ds,fs in os.walk(srcpath):
            for f in fs:
                copy(op.join(r,f), op.join(dstdir, r, f))
    elif op.isfile(srcpath):
        shutil.copy2(srcpath, dstpath)
    return op.exists(dstpath)

def move(srcpath, dstpath):
    """Moves the file or directory at `srcpath` to `dstpath`. Returns True if
    successful, False otherwise."""
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
    else:
        return False
    try:
        shutil.move(srcpath, dstpath)
    except:
        return False
    return verfunc(verpath)

def makedirs(path):
    """Makes all directories required for given path; returns true if successful
    and false otherwise."""
    try:
        os.makedirs(path)
    except:
        return False
    return True

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    # copy("__temp-foo.txt", "foo.txt")
    # copy("__temp-foo.txt", "foo/bar/baz")
    # copy("__backup__", "foo/baz")
    # copy("__backup__", "../")
    # print copy("__backup__", "__temp__")
    # delete("__temp__")
    # print delete("__temp__", "txt", recurse=True, test=True)
    # print move(r"__temp__\backup2", r"__backup__")
    # print move(r"__backup__\__backup__", "__temp__")
    # print move(r"test.txt", r"__temp__")
    print move(r"test2.txt", r"test.txt")

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import os.path as op
import shutil

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def delete(path):
    if op.isdir(path):
        shutil.rmtree(path)
        return False == op.exists(path)
    elif op.isfile(path):
        os.remove(path)
        return False == op.exists(path)
    return None

def is_empty(path):
    """Returns True if the given file or directory path is empty."""
    if op.isdir(path):
        return [] == os.listdir(path)
    elif op.isfile(path):
        return 0 == os.stat(path).st_size
    return None

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

"""Library of functions related to path manipulation."""

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os.path as op

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def abspath(relpath, root=__file__):
    """Returns an absolute path based on the given root and relative path."""
    if op.isfile(root):
        root = op.dirname(root)
    return op.abspath(op.join(root, relpath))

def homepath():
    """Returns the path to the current user's home directory."""
    return op.expanduser("~")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import os.path as op
import sys
import webbrowser

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def open(target):
    """Opens the target file or URL in the default application."""
    if sys.platform.startswith("win"):
        webbrowser.open(target)
    # TODO: (JRR@201605192229) Will need to test on other platforms.

def cwd(path=""):
    """Returns the CWD and optionally sets it to the given path."""
    if path:
        if op.isfile(path):
            path = op.dirname(path)
        os.setcwd(path)
    return os.getcwd()

def abspath(relpath, root=__file__):
    """Returns an absolute path based on the given root and relative path."""
    if op.isfile(root):
        root = op.dirname(root)
    return op.abspath(op.join(root, relpath))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import os.path as op
import subprocess
import sys

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Library version string.
__version__ = "0.3.0"

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def open(target):
    """Opens the target file or URL in the default application. Taken from
    `http://stackoverflow.com/a/17317468`."""
    if sys.platform == "win32":
        os.startfile(target)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, target])

def cwd(path=None):
    """Returns the CWD and optionally sets it to the given path."""
    if path:
        if not op.isabs(path):
            path = op.abspath(path)
        if op.isfile(path):
            path = op.dirname(path)
        os.chdir(path)
    return os.getcwd()

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    open(r"C:\__temp__\Launchy\BUILD.txt")

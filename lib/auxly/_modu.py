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
__version__ = "0.3.4"

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class Cwd:
    def __init__(self, newpath=""):
        self.path = os.getcwd()
        self.original = self.path
        if newpath:
            if not op.isabs(newpath):
                newpath = op.abspath(newpath)
            if op.isfile(newpath):
                newpath = op.dirname(newpath)
            self.path = newpath
            os.chdir(newpath)
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        os.chdir(self.original)
    def __getattr__(self, name):
        return getattr(self.path, name)

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
    return Cwd(path).path

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

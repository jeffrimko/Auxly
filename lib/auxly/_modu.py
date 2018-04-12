##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from __future__ import print_function
import ctypes
import os
import os.path as op
import subprocess
import sys

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Library version string.
__version__ = "0.4.1"

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

def throw(name="AuxlyException"):
    """Convenience function for throwing/raising exceptions. Usefully with
    compound "or" statements and similar situations."""
    raise Exception(name)

def isadmin():
    """Returns true if the script is being run in admin mode, false
    otherwise."""
    if sys.platform == "win32":
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    return os.getuid() == 0

def verbose(enabled):
    """Returns normal print function if enable, otherwise a dummy print
    function is returned which will suppress output."""
    def _vprint(msg, **kwargs):
        print(msg, **kwargs)
    def _nprint(msg, **kwargs):
        pass
    return _vprint if enabled else _nprint

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

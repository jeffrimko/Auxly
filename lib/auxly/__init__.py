##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from top import (
        AuxlyError,
        callstop,
        isadmin,
        islinux,
        ismac,
        iswindows,
        open,
        throw,
        trycatch,
        trythrow,
        verbose,
    )
import auxly.filesys
import auxly.listy
import auxly.shell
import auxly.stringy

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Library version string.
__version__ = "0.9.0"

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

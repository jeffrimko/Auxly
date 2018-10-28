##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import auxly
import os.path as op
from ubuild import main, menu

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

@menu
def test():
    with auxly.filesys.Cwd("tests", __file__):
        auxly.shell.call("_Run_Tests.py")

@menu
def version():
    with auxly.filesys.Cwd(".", __file__):
        auxly.shell.call("_Check_Versions.py")

@menu
def install():
    with auxly.filesys.Cwd("lib", __file__):
        auxly.shell.call("_Install_Package.py")

@menu
def upload():
    with auxly.filesys.Cwd("lib", __file__):
        auxly.shell.call("_Upload_PyPI.py")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    main()

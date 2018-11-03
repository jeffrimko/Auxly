##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import verace

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

VERCHK = verace.VerChecker("Auxly", __file__)
VERCHK.include(r"lib\setup.py", match="version = ", splits=[('"',1)])
VERCHK.include(r"lib\auxly\__init__.py", match="__version__ = ", splits=[('"',1)])
VERCHK.include(r"CHANGELOG.adoc", match="auxly-", splits=[("-",1),(" ",0)], updatable=False)
VERCHK.include(r"doc\source\conf.py", match="version = ", splits=[("'",1)])
VERCHK.include(r"doc\source\conf.py", match="release = ", splits=[("'",1)])

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    VERCHK.prompt()

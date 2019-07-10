##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from __future__ import print_function
import auxly.filesys
import auxly.shell
import auxly.stringy
import auxly.listy
import ctypes
import os
import os.path as op
import subprocess
import sys

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Library version string.
__version__ = "0.6.1"

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def open(target):
    """Opens the target file or URL in the default application.

    **Attribution**:
    Written by user4815162342 and originally posted on
    `Stack Overflow <http://stackoverflow.com/a/17317468>`_.

    **Examples**:
    ::
        auxly.open("myfile.txt")
        auxly.open("https://www.github.com/")
    """
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

def trycatch(*args, **kwargs):
    """Wraps a function in a try/catch block. Can be used as a function
    decorator or as a function that accepts another function.

    **Params**:
      - func (func) - Function to call. Only available when used as a function.
      - oncatch (str) [kwargs] - Function to call if an exception is caught.
      - rethrow (str) [kwargs] - If true, exception will be re-thrown.

    **Examples**:
    ::

        trycatch(myfunc)(myarg1, myarg2, kwarg=mykwarg)
        trycatch(myfunc, oncatch=mycatchfunc)(myarg1, myarg2, kwarg=mykwarg)
        trycatch(myfunc, rethrow=True)(myarg1, myarg2, kwarg=mykwarg)
    """
    rethrow = kwargs.get('rethrow', False)
    oncatch = kwargs.get('oncatch', None)
    def decor(func):
        def wrapper(*fargs, **fkrgs):
            try:
                return func(*fargs, **fkrgs)
            except:
                if oncatch != None:
                    oncatch()
                if rethrow:
                    raise
        return wrapper
    if len(args) > 0 and callable(args[0]):
        func = args[0]
        return decor(func)
    return decor

def callstop(*args, **kwargs):
    """Limits the number of times a function can be called. Can be used as a
    function decorator or as a function that accepts another function. If used
    as a function, it returns a new function that will be call limited.

    **Params**:
      - func (func) - Function to call. Only available when used as a function.

    **Examples**:
    ::

        call = callstop(myfunc, limit=3)
        call(myarg1, myarg2)
    """
    limit = kwargs.get('limit', 1)
    def decor(func):
        def wrapper(*args, **kwargs):
            if wrapper.calls < limit:
                wrapper.calls += 1
                return func(*args, **kwargs)
        wrapper.calls = 0
        return wrapper
    if len(args) > 0 and callable(args[0]):
        func = args[0]
        return decor(func)
    return decor

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

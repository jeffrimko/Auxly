##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from __future__ import print_function

import ctypes
import os
import os.path as op
import platform
import subprocess
import sys
import traceback

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class AuxlyError(Exception):
    """Default Auxly error."""
    def __init__(self, ex=None):
        self.exc_name = ""
        self.traceback = ""
        self.ex = ex
        if isinstance(ex, Exception):
            try:
                raise ex
            except:
                self.ex = ""
                self._trycollect()
        else:
            self._trycollect()
        super(AuxlyError, self).__init__(ex)
    def _trycollect(self):
        try:
            self.exc_name = sys.exc_info()[0].__name__
            self.traceback = traceback.format_exc() or ""
        except:
            pass
    def __bool__(self):
        return False
    def __str__(self):
        output = self.__class__.__name__
        if self.ex or self.traceback:
            output += ": "
        if self.ex:
            output += str(self.ex)
        if self.exc_name:
            output += str(self.exc_name)
        if self.traceback:
            output += os.linesep + str(self.traceback)
        return output
    def __repr__(self):
        return str(self)

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def iswindows():
    """Returns true if host OS is Windows."""
    return "windows" in platform.platform().lower()

def islinux():
    """Returns true if host OS is Linux."""
    return "linux" in platform.platform().lower()

def ismac():
    """Returns true if host OS is Mac."""
    return "darwin" in platform.platform().lower()

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
    if iswindows():
        os.startfile(target)
    else:
        opener = "open" if ismac() else "xdg-open"
        subprocess.call([opener, target])

def throw(*args, **kwargs):
    """Convenience function for throwing/raising exceptions. Usefully with
    compound "or" statements and similar situations. Throws an AuxlyError by
    default unless another exception is provided as the first argument.

    **Examples**:
    ::
        throw()
        throw("error message")
        throw(ValueError)
        throw(ValueError, "error message")
    """
    exception = AuxlyError
    if len(args) > 0 and isinstance(args[0], type) and issubclass(args[0], Exception):
        exception = args[0]
        args = args[1:]
    raise exception(*args, **kwargs)

def isadmin():
    """Returns true if the script is being run in admin mode, otherwise
    false."""
    if iswindows():
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    return os.getuid() == 0

def verbose(enabled):
    """Returns normal print function if enabled, otherwise a dummy print
    function is returned which will suppress output."""
    def _vprint(msg, **kwargs):
        print(msg, **kwargs)
    def _nprint(msg, **kwargs):
        pass
    return _vprint if enabled else _nprint

def trythrow(arg):
    if isinstance(arg, Exception):
        raise arg
    return arg

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
                cresult = None
                if oncatch != None:
                    cresult = oncatch()
                if rethrow:
                    raise
                return cresult
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

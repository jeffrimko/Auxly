##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import atexit
import functools
import os
import os.path as op
import subprocess
import sys
import signal
import tempfile

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Null device.
NULL = open(os.devnull, "w")

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class _StartedProcess:
    """This object is returned by a ``start()`` call."""
    def __init__(self, popen, logfile):
        self.pid = popen.pid
        self._popen = popen
        self._logfile = logfile
        atexit.register(self.stop)
    def __del__(self):
        self.stop()
    def stop(self):
        """Stops the started process."""
        self._logfile.close()
        # NOTE: These two CTRL_BREAK_EVENT seem to be necessary on Windows. A
        # single CTRL_BREAK_EVENT does not always work properly.
        os.kill(self._popen.pid, signal.CTRL_BREAK_EVENT)
        os.kill(self._popen.pid, signal.CTRL_BREAK_EVENT)
        self._popen.kill()
    def poll(self):
        """Returns None if the process is still running, otherwise return the
        status code."""
        return self._popen.poll()
    def wait(self):
        """Waits for the process to complete then returns the status code."""
        return self._popen.wait()

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def call(cmd, **kwargs):
    """Calls the given shell command. Output will be displayed. Returns the
    status code.

    **Examples**:
    ::
        auxly.shell.call("ls")
    """
    kwargs['shell'] = True
    return subprocess.call(cmd, **kwargs)

def silent(cmd, **kwargs):
    """Calls the given shell command. Output will not be displayed. Returns the
    status code.

    **Examples**:
    ::
        auxly.shell.silent("ls")
    """
    return call(cmd, shell=True, stdout=NULL, stderr=NULL, **kwargs)

def start(cmd, logpath=None, **kwargs):
    """Starts the given command as a background process. Redirects stdin/stderr
    to an optional log file path. Returns a ``_StartedProcess`` object.

    **Examples**:
    ::
        p = auxly.shell.start("python -m http.server")
        ...
        p.stop()
    """
    if logpath:
        logfile = open(op.abspath(logpath), "w")
    else:
        # NOTE: Using a temp file seems to be necessary in some cases for
        # Windows. For example, instances have been seen where Python Flask
        # apps would not work properly having the stdout/stderr directed to
        # NULL.
        logfile = tempfile.NamedTemporaryFile("w", delete=True)
    popen = subprocess.Popen(
            cmd,
            shell=True,
            stdout=logfile,
            stderr=logfile,
            stdin=subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
    return _StartedProcess(popen, logfile)

def has(cmd):
    """Returns true if the give shell command is available.

    **Examples**:
    ::
        auxly.shell.has("ls")  # True
    """
    helps = ["--help", "-h", "--version"]
    if "nt" == os.name:
        helps.insert(0, "/?")
    fakecmd = "fakecmd"
    cmderr = strerr(fakecmd).replace(fakecmd, cmd)
    for h in helps:
        hcmd = "%s %s" % (cmd, h)
        if 0 == silent(hcmd):
            return True
        if len(listout(hcmd)) > 0:
            return True
        if strerr(hcmd) != cmderr:
            return True
    return False

def iterstd(cmd, std="out", **kwargs):
    """Iterates through the lines of a stderr/stdout stream for the given shell
    command."""
    def _readline():
        while True:
            line = getattr(proc, "std"+std).readline()
            if line != b"":
                yield line.rstrip().decode("UTF-8", "replace")
            else:
                break
    kwargs['shell'] = True
    kwargs['stdout'] = subprocess.PIPE
    kwargs['stderr'] = subprocess.PIPE
    if sys.version_info >= (3,0):
        with subprocess.Popen(cmd, **kwargs) as proc:
            for line in _readline(): yield line
    else:
        proc = subprocess.Popen(cmd, **kwargs)
        for line in _readline(): yield line
        proc.kill()

##--------------------------------------------------------------#
## Stdout related functions.                                    #
##--------------------------------------------------------------#

#: Iterates through lines of stdout.
#:
#: **Examples**:
#: ::
#:      for line in auxly.shell.iterout("cat myfile.txt"):
#:          print(line)
iterout = functools.partial(iterstd, std="out")

def listout(cmd, **kwargs):
    """Same as ``iterout()`` but returns a list."""
    return [line for line in iterout(cmd, **kwargs)]

def strout(cmd, **kwargs):
    """Same as ``iterout()`` but returns a string."""
    return "\n".join(listout(cmd, **kwargs))

##--------------------------------------------------------------#
## Stderr related functions.                                    #
##--------------------------------------------------------------#

#: Iterates through lines of stderr.
itererr = functools.partial(iterstd, std="err")

def listerr(cmd, **kwargs):
    """Same as ``itererr()`` but returns a list."""
    return [line for line in itererr(cmd, **kwargs)]

def strerr(cmd, **kwargs):
    """Same as ``itererr()`` but returns a string."""
    return "\n".join(listerr(cmd, **kwargs))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import functools
import os
import subprocess
import sys

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

#: Null device.
NULL = open(os.devnull, "w")

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def call(cmd, **kwargs):
    """Calls the given shell command. Output will be displayed. Returns the
    status code."""
    kwargs['shell'] = True
    return subprocess.call(cmd, **kwargs)

def silent(cmd, **kwargs):
    """Calls the given shell command. Output will not be displayed. Returns the
    status code."""
    return call(cmd, shell=True, stdout=NULL, stderr=NULL, **kwargs)

def has(cmd):
    """Returns true if the give shell command is available."""
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
iterout = functools.partial(iterstd, std="out")

def listout(cmd, **kwargs):
    """Same as iterout() but returns a list."""
    return [line for line in iterout(cmd, **kwargs)]

def strout(cmd, **kwargs):
    """Same as iterout() but returns a string."""
    return "\n".join(listout(cmd, **kwargs))

##--------------------------------------------------------------#
## Stderr related functions.                                    #
##--------------------------------------------------------------#

#: Iterates through lines of stderr.
itererr = functools.partial(iterstd, std="err")

def listerr(cmd, **kwargs):
    """Same as itererr() but returns a list."""
    return [line for line in itererr(cmd, **kwargs)]

def strerr(cmd, **kwargs):
    """Same as itererr() but returns a string."""
    return "\n".join(listerr(cmd, **kwargs))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import subprocess
import functools

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

def iterout(cmd, **kwargs):
    """Iterates through the lines of stdout from the given shell command."""
    kwargs['shell'] = True
    kwargs['stdout'] = subprocess.PIPE
    kwargs['stderr'] = NULL
    proc = subprocess.Popen(cmd, **kwargs)
    while True:
        line = proc.stdout.readline()
        if line != "":
            yield line.rstrip()
        else:
            break

def listout(cmd, **kwargs):
    """Same as iterout() but returns a list."""
    return [line for line in iterout(cmd, **kwargs)]

def has(cmd):
    """Returns true if the give shell command is available."""
    if 0 == silent(cmd + " --help"):
        return True
    if 0 == silent(cmd + " -h"):
        return True
    if 0 == silent(cmd + " --version"):
        return True
    if 0 == silent(cmd + " /?"):
        return True
    # TODO: (JRR@201605192227) Not sure if this is valid.
    # if len(listout(cmd)) > 0:
    #     return True
    return False

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from random import choice
from string import ascii_lowercase
import re

import top as auxly
from listy import iterate

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def subat(orig, index, replace):
    """Substitutes the replacement string/character at the given index in the
    given string, returns the modified string.

    **Examples**:
    ::
        auxly.stringy.subat("bit", 2, "n")
    """
    return "".join([(orig[x] if x != index else replace) for x in range(len(orig))])

def randomize(length=6, choices=None):
    """Returns a random string of the given length."""
    if type(choices) == str:
        choices = list(choices)
    choices = choices or ascii_lowercase
    return "".join(choice(choices) for _ in range(length))

def between(orig, start, end):
    """Returns the substring of the given string that occurs between the start
    and end strings."""
    try:
        parse = orig
        if start and start in parse:
            parse = parse.split(start, 1)[1]
        if end and end in parse:
            parse = parse.split(end, 1)[0]
        return parse
    except:
        return auxly.AuxlyError()

def remove(orig, subs):
    """Removes the given substrings from the given string, returns the modified
    string."""
    output = orig
    try:
        for s in iterate(subs):
            output = output.replace(s, "")
        return output
    except:
        return auxly.AuxlyError()

def haspattern(pattern, search):
    """Returns true if the given text contains the given regex pattern."""
    try:
        return re.compile(pattern).search(search) != None
    except:
        return auxly.AuxlyError()

def subtract(orig, tosub):
    """Returns the original string with the given substring removed if it is
    found at the end, otherwise returns just the original string."""
    if orig.endswith(tosub):
        return orig[:-1 * len(tosub)]
    return orig

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

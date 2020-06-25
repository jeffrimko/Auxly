##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from random import choice
from string import ascii_lowercase

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

def between(full, start, end):
    """Returns the substring of the given string that occurs between the start
    and end strings."""
    try:
        if not start:
            parse = full
        else:
            parse = full.split(start, 1)[1]
        if end:
            result = parse.split(end, 1)[0]
        else:
            result = parse
        return result
    except:
        return full

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

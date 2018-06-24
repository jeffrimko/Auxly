##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def chunk(l, n):
    """Yields a generator which groups the given list into successive n-size
    chunks.

    **Attribution**:
    Written by Ned Batchelder and originally posted at
    https://stackoverflow.com/a/312464/789078."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def smooth(l):
    """Yields a generator which smooths all elements as if the given list
    was of depth 1."""
    if type(l) in [list, tuple]:
        for i in l:
            yield from smooth(i)
    else:
        yield l

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

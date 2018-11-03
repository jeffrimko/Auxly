##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def chunk(l, n):
    """Yields a generator which groups the given list into successive n-size
    chunks.

    **Attribution**:
    Written by Ned Batchelder and originally posted on
    `Stack Overflow <https://stackoverflow.com/a/312464/789078>`_.

    **Examples**:
    ::
        list(auxly.listy.chunk([1,2,3,4,5,6,7,8], 3))
        # [[1, 2, 3], [4, 5, 6], [7, 8]]
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]

def smooth(l):
    """Yields a generator which smooths all elements as if the given list
    was of depth 1.

    **Examples**:
    ::
        list(auxly.listy.smooth([1,[2,[3,[4]]]]))
        # [1, 2, 3, 4]
    """
    if type(l) in [list, tuple]:
        for i in l:
            for j in smooth(i):
                yield j
    else:
        yield l

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

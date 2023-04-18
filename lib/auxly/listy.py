##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import top as auxly

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def chunk(items, size):
    """Yields a generator which groups the given list items into successive chunks of
    the given size.

    **Attribution**:
    Written by Ned Batchelder and originally posted on
    `Stack Overflow <https://stackoverflow.com/a/312464/789078>`_.

    **Examples**:
    ::
        list(auxly.listy.chunk([1,2,3,4,5,6,7,8], 3))
        # [[1, 2, 3], [4, 5, 6], [7, 8]]
    """
    for i in range(0, len(items), size):
        yield items[i:i + size]

def smooth(items):
    """Yields a generator which smooths all items as if the given list
    was of depth 1.

    **Examples**:
    ::
        list(auxly.listy.smooth([1,[2,[3,[4]]]]))
        # [1, 2, 3, 4]
    """
    if type(items) in [list, tuple]:
        for i in items:
            for j in smooth(i):
                yield j
    else:
        yield items

def isiterable(item):
    """Returns true if the given item is iterable."""
    try:
        [i for i in item]
        return True
    except TypeError:
        return False

def iterate(items):
    """Iterates over the given items, whether they are iterable or not. Strings
    are not iterated per character."""
    if isinstance(items, str) or not isiterable(items):
        items = [items]
    for i in items:
        yield i

def index(items, num):
    """Returns the item at the given index, otherwise AuxlyError."""
    try:
        return items[num]
    except IndexError as ex:
        return auxly.AuxlyError(ex)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
from testlib import *

from auxly.filesys import copy, isempty, delete

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(unittest.TestCase):

    def test_copy_1(test):
        path = "foo.txt"
        test.assertIsNone(isempty(path))
        with open(path, "w") as fo:
            pass
        test.assertTrue(isempty(path))
        with open(path, "w") as fo:
            fo.write("not empty")
        test.assertFalse(isempty(path))
        test.assertTrue(delete(path))
        test.assertIsNone(isempty(path))
        test.assertFalse(delete(path))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

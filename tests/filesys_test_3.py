##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os.path as op
from testlib import *

from auxly.filesys import makedirs, copy, isempty, delete

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_isempty_1(test):
        path = FNAME[0]
        test.assertIsNone(isempty(path))
        with open(path, "w") as fo:
            pass
        test.assertTrue(isempty(path))
        with open(path, "w") as fo:
            fo.write(TEXT[0])
        test.assertFalse(isempty(path))
        test.assertTrue(delete(path))
        test.assertIsNone(isempty(path))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

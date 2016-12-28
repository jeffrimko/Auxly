##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import makedirs, delete, isempty, copy

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_makedirs_1(test):
        """Make a single dir."""
        path = DIR[0]
        test.assertFalse(op.exists(path))
        test.assertTrue(makedirs(path))
        test.assertTrue(op.isdir(path))
        test.assertTrue(isempty(path))
        test.assertTrue(delete(path))
        test.assertFalse(op.exists(path))

    def test_makedirs_2(test):
        """Make nested dirs."""
        path = op.join(DIR[0], DIR[1])
        test.assertIsNone(isempty(path))
        test.assertFalse(op.exists(path))
        test.assertTrue(makedirs(path))
        test.assertTrue(op.exists(path))
        test.assertTrue(op.isdir(path))
        test.assertFalse(isempty(DIR[0]))
        test.assertTrue(isempty(path))
        test.assertTrue(delete(path))
        test.assertIsNone(isempty(path))
        test.assertFalse(op.exists(path))
        test.assertTrue(op.isdir(DIR[0]))
        test.assertTrue(delete(DIR[0]))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

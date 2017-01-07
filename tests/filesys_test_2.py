##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import copy, delete

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_copy_1(test):
        """Copy file to dir/file, overwrite existing file."""
        path0 = FNAME[0]
        path1 = op.join(DIR[0], FNAME[0])
        fwrite(path0, TEXT[0])
        fwrite(path1, TEXT[1])
        test.assertTrue(TEXT[1] == fread(path1))
        test.assertTrue(copy(path0, path1))
        test.assertTrue(TEXT[0] == fread(path1))

    def test_copy_2(test):
        """Copy file to dir/file fails due to overwrite flag."""
        path0 = FNAME[0]
        path1 = op.join(DIR[0], FNAME[0])
        fwrite(path0, TEXT[0])
        fwrite(path1, TEXT[1])
        test.assertTrue(TEXT[1] == fread(path1))
        test.assertFalse(copy(path0, path1, overwrite=False))
        test.assertTrue(TEXT[1] == fread(path1))

    def test_copy_3(test):
        """Copy file to dir."""
        path0 = FNAME[0]
        fwrite(path0, TEXT[0])
        path1 = DIR[1]
        test.assertTrue(copy(path0, path1))
        path1 = op.join(path1, path0)
        test.assertTrue(TEXT[0] == fread(path1))

    def test_copy_4(test):
        """Copy file to dir fails due to overwrite flag."""
        path0 = FNAME[0]
        path1 = DIR[0]
        fpath1 = op.join(path1, path0)
        fwrite(path0, TEXT[0])
        fwrite(fpath1, TEXT[1])
        test.assertFalse(copy(path0, path1, overwrite=False))
        test.assertTrue(TEXT[1] == fread(fpath1))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

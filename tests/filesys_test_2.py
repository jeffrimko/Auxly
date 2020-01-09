##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

import auxly
from auxly.filesys import copy, cwd, delete, isempty

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

    def test_copy_5(test):
        """Copy empty dir to dir."""
        path0 = op.join(DIR[0])
        path1 = op.join(DIR[1])
        test.assertTrue(makedirs(path0))
        test.assertTrue(makedirs(path1))
        test.assertTrue(copy(path0, path1))
        tpath = op.join(DIR[1], DIR[0])
        test.assertTrue(op.isdir(tpath))

    def test_copy_6(test):
        """Copy dir to dir using relative src path."""
        test.assertTrue(makedirs(op.join(DIR[0], DIR[1])))
        test.assertTrue(makedirs(op.join(DIR[2])))
        test.assertFalse(op.isdir(DIR[1]))
        cwd(DIR[0])
        test.assertTrue(op.isdir(DIR[1]))
        path0 = op.join("..", DIR[2])
        path1 = DIR[1]
        tpath = op.join(DIR[1], DIR[2])
        test.assertFalse(op.isdir(tpath))
        test.assertTrue(copy(path0, path1))
        test.assertTrue(op.isdir(path0))
        test.assertTrue(op.isdir(tpath))

    def test_copy_7(test):
        """Copy dir to dir using relative dst path."""
        test.assertTrue(makedirs(op.join(DIR[0], DIR[1])))
        cwd(DIR[0])
        test.assertTrue(op.isdir(DIR[1]))
        path0 = DIR[1]
        path1 = ".."
        tpath = op.join("..", DIR[1])
        test.assertFalse(op.isdir(tpath))
        test.assertTrue(copy(path0, path1))
        test.assertTrue(op.isdir(path0))
        test.assertTrue(op.isdir(tpath))

    def test_copy_8(test):
        """Copy dir to dir that does not exist."""
        path0 = DIR[0]
        path1 = DIR[1]
        test.assertTrue(makedirs(path0))
        test.assertFalse(op.isdir(path1))
        test.assertTrue(copy(path0, path1))
        test.assertTrue(op.isdir(path0))
        test.assertTrue(op.isdir(path1))
        test.assertTrue(isempty(path1))

    def test_copy_9(test):
        """Copy file without extension."""
        path0 = r"..\LICENSE"
        path1 = "LICENSE"
        test.assertTrue(op.isfile(path0))
        test.assertFalse(op.isfile(path1))
        test.assertTrue(copy(path0, path1))
        test.assertTrue(op.isfile(path0))
        test.assertTrue(op.isfile(path1))
        test.assertTrue(delete(path1))
        test.assertFalse(op.isfile(path1))

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

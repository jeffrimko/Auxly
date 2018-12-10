##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import Path

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_path_1(test):
        """Basic Path usage."""
        path = FNAME[0]
        fwrite(path, TEXT[0])
        base,ext = op.splitext(path)
        dir_ = op.abspath(".")
        p = Path(path)
        test.assertTrue(p.exists())
        test.assertTrue(p.isfile())
        test.assertFalse(p.isdir())
        test.assertEqual(dir_, p.dir)
        test.assertEqual(path, p.filename)
        test.assertEqual(base, p.file)
        test.assertEqual(ext, p.ext)

    def test_path_2(test):
        """Basic Path usage."""
        p = Path(DIR[0], FNAME[0])
        test.assertFalse(p.exists())
        test.assertFalse(p.isfile())
        test.assertFalse(p.isdir())
        test.assertEqual(op.abspath(op.join(DIR[0], FNAME[0])), p)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

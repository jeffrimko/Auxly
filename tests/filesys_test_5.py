##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import ParsedPath

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_parsedpath_1(test):
        """Basic path check."""
        path = FNAME[0]
        fwrite(path, TEXT[0])
        base,ext = op.splitext(path)
        dir_ = op.abspath(".")
        p = ParsedPath(path)
        test.assertTrue(p.exists())
        test.assertTrue(p.isfile())
        test.assertFalse(p.isdir())
        test.assertEqual(dir_, p.dir)
        test.assertEqual(path, p.filename)
        test.assertEqual(base, p.file)
        test.assertEqual(ext, p.ext)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

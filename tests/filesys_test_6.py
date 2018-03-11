##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import File

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_file_1(test):
        """Basic File usage."""
        p = FNAME[0]
        f = File(p)
        test.assertFalse(f.exists())
        test.assertTrue(f.write("hello"))
        test.assertTrue(f.append(" world"))
        test.assertTrue(f.exists())
        test.assertEqual("hello world", fread(p))
        test.assertEqual("5eb63bbbe01eeed093cb22bb8f5acdc3", f.checksum())

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from testlib import *

from auxly.filesys import walkfiles

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class TestCase(BaseTest):
    def test_file_1(test):
        """Test walkfiles() behavior."""
        norecurse = [f for f in walkfiles("..", regex=".py$", recurse=False)]
        withrecurse = [f for f in walkfiles("..", regex=".py$")]
        test.assertTrue(len(withrecurse) > len(norecurse))

    def test_file_2(test):
        """Test walkfiles() behavior."""
        noregex = [f for f in walkfiles("..")]
        withregex = [f for f in walkfiles("..", regex=".adoc$")]
        test.assertTrue(len(noregex) > len(withregex))

    def test_file_3(test):
        """Test walkfiles() behavior."""
        for f in walkfiles("..", regex=".py$"):
            test.assertTrue(f.endswith(".py"))

    def test_file_4(test):
        """Test walkfiles() behavior."""
        test.assertTrue(1 == len([f for f in walkfiles("..", regex="README.adoc", recurse=False)]))

    def test_file_5(test):
        """Test walkfiles() behavior."""
        found = False
        for f in walkfiles(".", recurse=False):
            found |= f.endswith(__file__)
        test.assertTrue(found)

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    unittest.main()

##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import os.path as op
import sys
import unittest

# Allows development version of library to be used instead of installed.
sys.path.insert(0, r"..\lib")

from auxly.filesys import delete, makedirs

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

FNAME = ["foo.txt", "bar.txt"]
DIR = ["foo", "bar", "baz", "qux"]
TEXT = ["hello", "world"]

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

class BaseTest(unittest.TestCase):
    def tearDown(test):
        super(BaseTest, test).tearDown()
        for i in FNAME + DIR:
            delete(i)

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def fwrite(path, text):
    makedirs(path)
    with open(path, "w") as fo:
        fo.write(text)

def fread(path):
    with open(path) as fi:
        return fi.read()

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    pass

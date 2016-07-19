##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

import os
import subprocess
import sys

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

def generate_readme():
    subprocess.call("asciidoctor -b docbook ../README.adoc", shell=True)
    subprocess.call("pandoc -r docbook -w rst -o README.rst ../README.xml", shell=True)
    os.remove("../README.xml")

def cleanup_readme():
    os.remove("README.rst")

##==============================================================#
## SECTION: Main Body                                           #
##==============================================================#

if __name__ == '__main__':
    generate_readme()
    if len(sys.argv) > 1 and sys.argv[1] == "generate_readme":
        exit()
    subprocess.call("python setup.py install", shell=True)
    cleanup_readme()

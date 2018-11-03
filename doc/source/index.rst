.. Auxly documentation master file, created by
   sphinx-quickstart on Sat Jun 10 11:15:52 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Auxly
=======

This is the main documentation for Auxly, a Python library for various helper classes/functions originally intended to make shell-like scripting easier.

For more information:

  - **Readme** - https://github.com/jeffrimko/Auxly/blob/master/README.adoc - Main readme file.
  - **GitHub** - https://github.com/jeffrimko/Auxly - Main version control repository.
  - **PyPI** - https://pypi.python.org/pypi/auxly - Package index page.

Introduction
------------

Auxly provides various convenience functions for common tasks. Functions
that overlap with the standard library are designed to do what you would
reasonably expect
(`POLA <https://en.wikipedia.org/wiki/Principle_of_least_astonishment>`__)
and, when necessary, fail without throwing exceptions.


The following are basic examples of Auxly (all examples can be found
`here <https://github.com/jeffrimko/Auxly/tree/master/examples>`__):

-  `examples/delete\_1.py <https://github.com/jeffrimko/Auxly/blob/master/examples/delete_1.py>`__
   - Deletes all PYC files in the project.

Refer to the unit tests
`here <https://github.com/jeffrimko/Auxly/tree/master/tests>`__ for
additional examples.

API Documentation
-----------------

Top Level
*********

.. automodule:: auxly
    :members:

File System
***********
The ``auxly.filesys`` module provides various convenience functions for working with the file system.

.. automodule:: auxly.filesys
    :members:

Shell
*****
The ``auxly.shell`` module provides various convenience functions for working with the system shell.

.. automodule:: auxly.shell
    :members:

Stringy
*******
The ``auxly.stringy`` module provides various convenience functions for working with strings.

.. automodule:: auxly.stringy
    :members:

Listy
*****
The ``auxly.listy`` module provides various convenience functions for working with lists.

.. automodule:: auxly.listy
    :members:

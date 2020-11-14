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

.. include:: readme_excerpt.rst

API Documentation
-----------------

``auxly``
*********

.. automodule:: auxly
    :members:

``auxly.filesys``
*****************
The ``auxly.filesys`` module provides various convenience functions for working with the file system.

.. automodule:: auxly.filesys
    :members:
    :inherited-members:
    :show-inheritance:
    :exclude-members: capitalize, center, casefold, count, endswith, expandtabs, encode, find, format, index, isalnum, isalpha, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, join, ljust, rjust, lower, upper, swapcase, lstrip, rstrip, strip, partition, maketrans, rpartition, translate, replace, rfind, rindex, split, rsplit, splitlines, startswith, title, zfill, format_map

``auxly.shell``
***************
The ``auxly.shell`` module provides various convenience functions for working with the system shell.

.. automodule:: auxly.shell
    :members:
    :inherited-members:

``auxly.stringy``
*****************
The ``auxly.stringy`` module provides various convenience functions for working with strings.

.. automodule:: auxly.stringy
    :members:
    :inherited-members:

``auxly.listy``
***************
The ``auxly.listy`` module provides various convenience functions for working with lists.

.. automodule:: auxly.listy
    :members:
    :inherited-members:

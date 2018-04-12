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

Top Level
---------

.. autofunction:: auxly.open
.. autofunction:: auxly.throw
.. autofunction:: auxly.isadmin
.. autofunction:: auxly.verbose

File System
-----------

.. autofunction:: auxly.filesys.abspath
.. autofunction:: auxly.filesys.homedir
.. autofunction:: auxly.filesys.cwd
.. autofunction:: auxly.filesys.makedirs
.. autofunction:: auxly.filesys.delete
.. autofunction:: auxly.filesys.countfiles
.. autofunction:: auxly.filesys.countdirs
.. autofunction:: auxly.filesys.isempty
.. autofunction:: auxly.filesys.copy
.. autofunction:: auxly.filesys.move
.. autofunction:: auxly.filesys.checksum

.. autoclass:: auxly.filesys.Cwd
    :members:

.. autoclass:: auxly.filesys.Path
    :members:

.. autoclass:: auxly.filesys.File
    :members:

Shell
-----

.. autofunction:: auxly.shell.call
.. autofunction:: auxly.shell.silent
.. autofunction:: auxly.shell.has
.. autofunction:: auxly.shell.iterstd
.. autofunction:: auxly.shell.listout
.. autofunction:: auxly.shell.iterout
.. autofunction:: auxly.shell.itererr
.. autofunction:: auxly.shell.strout
.. autofunction:: auxly.shell.listerr
.. autofunction:: auxly.shell.strerr

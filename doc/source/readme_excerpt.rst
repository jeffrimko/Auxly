Introduction
------------

This project provides a Python 2.7/3.x library for common tasks
especially when writing shell-like scripts. Some of the functionality
overlaps with the standard library but the API is slightly modified.

The goal of this project is to leverage the straightforward, clean
syntax of Python while avoiding some of the boilerplate code that might
be necessary when using the standard library. Functions that overlap
with the standard library are designed to do what you would reasonably
expect
(`POLA <https://en.wikipedia.org/wiki/Principle_of_least_astonishment>`__)
and, when necessary, fail **without** throwing exceptions.

Please note when using this library that operations will fail silently.
This is a deliberate design decision. However, there is often a way to
check if an operation has failed and optionally throw and exception if
that is desirable:

.. code:: python

    auxly.filesys.copy("foo.txt", "bar") or auxly.throw()  # Throws/raises exception on failure.

Auxly provides the following modules:

-  ``auxly``

-  ``auxly.filesys``

-  ``auxly.shell``

-  ``auxly.stringy``

-  ``auxly.listy``

The following are basic examples of Auxly (all examples can be found
`here <https://github.com/jeffrimko/Auxly/tree/master/examples>`__):

-  `examples/delete\_pyc.py <https://github.com/jeffrimko/Auxly/blob/master/examples/delete_pyc.py>`__
   - Deletes all PYC files in the project.

-  `examples/guess\_os.py <https://github.com/jeffrimko/Auxly/blob/master/examples/guess_os.py>`__
   - Attempts to guess the host OS based on available shell commands.

Refer to the unit tests
`here <https://github.com/jeffrimko/Auxly/tree/master/tests>`__ for
additional examples.

Status
------

Currently, this project is in the **development release** stage. While
this project is suitable for use, please note that there may be
incompatibilities in new releases.

Release notes are maintained in the project
`changelog <https://github.com/jeffrimko/Auxly/blob/master/CHANGELOG.adoc>`__.

Requirements
------------

Auxly should run on any Python 2.7/3.x interpreter without additional
dependencies.

Installation
------------

Auxly can be installed with pip using the following command:
``pip install auxly``

Additionally, Auxly can be installed from source by running:
``python setup.py install``


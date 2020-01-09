from setuptools import setup, find_packages
from auxly.filesys import File

setup(
    name = "auxly",
    version = "0.6.6",
    author = "Jeff Rimko",
    author_email = "jeffrimko@gmail.com",
    description = "Python library for common shell-like script tasks.",
    license = "MIT",
    keywords = "cli script utility library",
    url = "https://github.com/jeffrimko/Auxly",
    packages=["auxly"],
    long_description=File("README.rst").read() or "",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)

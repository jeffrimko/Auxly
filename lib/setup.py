from setuptools import setup, find_packages

setup(
    name = "auxly",
    version = "0.2.0-alpha1",
    author = "Jeff Rimko",
    author_email = "jeffrimko@gmail.com",
    description = "Python library for common shell-like script tasks.",
    license = "MIT",
    keywords = "cli script utility library",
    url = "https://github.com/jeffrimko/Auxly",
    packages=["auxly"],
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)

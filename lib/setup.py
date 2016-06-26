from setuptools import setup, find_packages

setup(
    name = "auxly",
    version = "0.1.0-alpha",
    author = "Jeff Rimko",
    author_email = "jeffrimko@gmail.com",
    description = "TODO",
    license = "MIT",
    keywords = "cli library",
    url = "https://github.com/jeffrimko/Auxly",
    packages=["auxly"],
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)

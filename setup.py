from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from getpass import getuser
import os
from sys import platform
import subprocess

user = getuser()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'turbocharge',
    version = '0.0.1',
    description= 'Turbocharged Way To Install All The Packages You Love!',
    url="https://github.com/TheBossProSniper/TurboCharge",
    author = 'TheBossProSniper',
    author_email = 'thebossprosniper@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['turbocharge'],
    packages=find_packages(),
    install_requires = [
        'Click',
        'progress',
    ],
    entry_points =
    '''
        [console_scripts]
        turbo=turbocharge:cli
    ''',
classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ]
)

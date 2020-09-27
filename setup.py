from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from getpass import getuser
import os
from sys import platform
import subprocess
from src.Setup import Setup
import atexit

user = getuser()

s = Setup()

class PostDevelop(develop):
    def run(self):
        develop.run(self)
        s.setup()
    
class PostInstall(install):
    def run(self):
        install.run(self)
        s.setup()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = 'turbocharge',
    version = '3.0.6',
    description= 'Turbocharged Way To Install All The Packages You Love!',
    url="https://github.com/TheBossProSniper/TurboCharge",
    author = 'TheBossProSniper',
    author_email = 'thebossprosniper@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['turbocharge'],
    packages=find_packages(),
    scripts=[os.path.join(os.path.abspath(os.getcwd()), 'src', 'turbocharge.py')],
    install_requires = [
        'Click',
        'progress',
    ],
    cmdclass={
        'develop': PostDevelop,
        'install': PostInstall
    },
    package_dir={'': 'src'},
    entry_points = 
    '''
        [console_scripts]
        turbo=turbocharge:cli
    ''',
    classifiers=[
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: Unix",
    ]
)

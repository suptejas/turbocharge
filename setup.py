from setuptools import setup, find_packages
from getpass import getuser
import os
from sys import platform
import subprocess

user = getuser()

if platform == 'linux':
    os.system(f'export PATH="/home/{user}/.local/bin:$PATH"')
elif platform == 'win32':
    subprocess.Popen(['powershell.exe', 'Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))'])

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
    package_dir={'': 'src'},
    entry_points = 
    '''
        [console_scripts]
        turbocharge=turbocharge:cli
    ''',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ]
)

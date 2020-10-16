from os import system
from os.path import isfile
import os
from sys import platform
from getpass import getuser
import click
from progress.bar import IncrementalBar
from progress.spinner import Spinner
from time import sleep


class Setup:
    def setup(self):
        user = getuser()
        if platform == 'linux':
            # Creating the config file
            setup_progress = IncrementalBar(
                message='Setting Up Your Turbocharge Config...', max=100)
            for _ in range(1, 101):
                sleep(0.02)
                setup_progress.next()

            file_exists = None
            if isfile(f'/home/{getuser()}/config.tcc'):
                file_exists = True
            else:
                file_exists = False

            if not file_exists:
                with open(f'/home/{getuser()}/config.tcc', 'w+') as f:
                    f.write(f'linux\n{user}\n')

        elif platform == 'win32':
            # Install Chocolatey And Setup
            setup_progress = Spinner(
                'Setting up your Turbocharge config file...')
            click.echo('\n')
            for _ in range(1, 41):
                sleep(0.02)
                setup_progress.next()

            file_exists = None
            if isfile(os.path.join("C:\\Turbocharge", "config.tcc")):
                file_exists = True
            else:
                file_exists = False

            for _ in range(41, 61):
                sleep(0.02)
                setup_progress.next()

            if not file_exists:
                with open(os.path.join("C:\\Turbocharge", "config.tcc"), 'w+') as f:
                    f.write(f'win32\n{user}\n')
            for _ in range(61, 100):
                sleep(0.02)
                setup_progress.next()

        elif platform == 'darwin':
            # Installing and setting up Homebrew
            click.echo(click.style(
                'Setting Up Turbocharge on your Mac...', fg='green'))

            os.system(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" < /dev/null')

            if isfile(f'/Users/{getuser()}/config.tcc'):
                file_exists = True
            else:
                file_exists = False
            if not file_exists:
                with open(f'/Users/{getuser()}/config.tcc', 'w+') as f:
                    f.write(f'darwin\n{user}\n')

        click.echo('\n')
        click.echo('Succesfully Setup Turbocharge!')

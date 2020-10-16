from os import system
from os.path import isfile
from sys import platform
from getpass import getuser
import click
from progress.bar import IncrementalBar
from time import sleep
import subprocess
from subprocess import Popen, PIPE
import os

class Setup:
    def setup(self, password : str):
        if platform == 'linux':
            # Creating the config file
            setup_progress = IncrementalBar(message='Setting Up Your Turbocharge Config...', max=100)
            for _ in range(1, 41):
                sleep(0.02)
                setup_progress.next()
            
            file_exists = None
            if isfile(f'/home/{getuser()}/config.tcc'):
                file_exists = True
            else:
                file_exists = False
            
            for _ in range(41, 61):
                sleep(0.02)
                setup_progress.next()
            
            if file_exists:
                # Config already exists... 
                action = click.prompt('Turbocharge found a pre-existing configuration. Would you like to reset it or install the contents of the config? [reset/install]: ')
                if action == 'install':
                    # Need to import the configinstaller and do the setup...
                    for _ in range(61, 100):
                        sleep(0.02)
                        setup_progress.next()
                        
                if action == 'reset':
                    # Just creating the file and deleting all its contents...
                    with open(f'/home/{getuser()}/config.tcc', 'w+'):
                        pass
                    for _ in range(61, 100):
                        sleep(0.02)
                        setup_progress.next()
            else:
                # Config does not exist so creating config.tcc...
                click.echo(f'Turbocharge couldn\'t find a pre-existing configuration, creating config.tcc at /home/{getuser()}.')
                
                if action == 'install':
                    # Need to import the configinstaller and do the setup...
                    for _ in range(61, 100):
                        sleep(0.02)
                        setup_progress.next()
                if action == 'reset':
                    # Just creating the file and deleting all its contents...
                    with open(f'/home/{getuser()}/config.tcc', 'w+'):
                        pass
                    for _ in range(61, 100):
                        sleep(0.02)
                        setup_progress.next()
                        
        if platform == 'win32':
            # Install Chocolatey And Setup
            click.echo('Installing Chocolatey...')
            subprocess.Popen(
            [
                'powershell.exe',
                'Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))'
            ]
            )
            
        if platform == 'darwin':
            click.echo(click.style('Setting Up Turbocharge on your Mac...', fg='green'))
            
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" < /dev/null')
            
            if isfile(f'/Users/{getuser()}/config.tcc'):
                file_exists = True
            else:
                file_exists = False
            
            
            if file_exists:
                # Config already exists... 
                action = click.prompt('Turbocharge found a pre-existing configuration. Would you like to reset it or install the contents of the config? [reset/install]')
                if action == 'install':
                    # Need to import the configinstaller and do the setup...
                        pass
                    
                if action == 'reset':
                    # Just creating the file and deleting all its contents...
                    with open(f'/Users/{getuser()}/config.tcc', 'w+'):
                        pass
            else:
                # Config does not exist so creating config.tcc...
                click.echo(f'Turbocharge couldn\'t find a pre-existing configuration, creating config.tcc at /Users/{getuser()}.')
                
                with open(f'/Users/{getuser()}/config.tcc', 'w+'):
                        pass
                    
            click.echo('Succesfully Setup Turbocharge!')

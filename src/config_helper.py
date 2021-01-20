from os.path import isfile
import os
from sys import platform
from getpass import getuser
import click
from progress.bar import IncrementalBar
from progress.spinner import Spinner
from time import sleep
from miscellaneous import is_admin
from colorama import Fore

class Setup:
    def setup(self):
        user = getuser()
        if platform == 'linux':
            # Creating the config file
            setup_progress = IncrementalBar(message='Setting Up Your Turbocharge Config...', max=100)
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
            install_chocolatey = click.prompt('Turbocharge requires Chocolatey To Be Installed. Would You Like To Install Chocolatey?')
            if install_chocolatey:
                print('\n')
                os.system('powershell.exe -c Set-ExecutionPolicy RemoteSigned -Scope CurrentUser')
                if is_admin():
                    os.system("powershell.exe -c Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")
                else:
                    print(f'{Fore.RED}Setup Must Be Run As Administrator!{Fore.RESET}')
                    exit()
            else:
                exit()

            setup_progress = Spinner('Setting up your Turbocharge config....')
            for _ in range(1, 41):
                sleep(0.02)
                setup_progress.next()
            
            file_exists = None
            if isfile(os.path.join(os.path.abspath(os.getcwd()), "config.tcc")):
                file_exists = True
            else:
                file_exists = False
            
            for _ in range(41, 61):
                sleep(0.02)
                setup_progress.next()
                        
            if not file_exists:
                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'w+') as f:
                    f.write(f'win32\n{user}\n')
            for _ in range(61, 100):
                sleep(0.02)
                setup_progress.next()
            exit()

        elif platform == 'darwin':
            # Installing and setting up Homebrew
            click.echo(click.style('Setting Up Turbocharge on your Mac...', fg='green'))
            
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" < /dev/null')
            
            if isfile(f'/Users/{getuser()}/config.tcc'):
                file_exists = True
            else:
                file_exists = False
            if not file_exists:
                with open(f'/Users/{getuser()}/config.tcc', 'w+') as f:
                    f.write(f'darwin\n{user}\n')
                    
        click.echo('Succesfully Setup Turbocharge!')

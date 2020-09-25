from sys import platform
from subprocess import Popen, PIPE, DEVNULL, run
import time
from progress.spinner import Spinner
from progress.bar import IncrementalBar
from os.path import isfile
import click
from getpass import getuser
from constants import applications_windows, devpackages_windows, applications_linux, devpackages_linux
import subprocess

class Uninstaller:
    def uninstall(self, script: str, password: str, package_name: str):
        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(
                    script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

                
                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())

                file_exists = False
                if isfile(f'/home/{getuser()}/config.tcc'):
                    file_exists = True
                
                if file_exists:
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()
                else:
                    for _ in range(1, 25):
                        time.sleep(0.01)
                        installer_progress.next()

                    click.echo(
                        click.style(
                            f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                            fg='green'))
                    return

                def get_key(val, dictionary):
                    for key, value in dictionary.items():
                        if val == value:
                            return key

                package_type = None
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'
                
                dictionary = None
                if package_type == 'p':
                    dictionary = devpackages_linux
                
                elif package_type == 'a':
                    dictionary = applications_linux

                with open(f'/home/{getuser()}/config.tcc', 'w+') as file:
                    for line in lines:
                        if get_key(package_name, dictionary) in line:
                            continue
                        else:
                            file.write(line)

                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()


                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

        elif platform == 'win32':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(script, stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)
        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(
                    script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)


                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())

                file_exists = False
                if isfile(f'/home/{getuser()}/config.tcc'):
                    file_exists = True

                if file_exists:
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()
                else:
                    for _ in range(1, 25):
                        time.sleep(0.01)
                        installer_progress.next()

                    click.echo(
                        click.style(
                            f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                            fg='green'))
                    return

                def get_key(val, dictionary):
                    for key, value in dictionary.items():
                        if val == value:
                            return key

                package_type = None
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'

                dictionary = None
                if package_type == 'p':
                    dictionary = devpackages_linux

                elif package_type == 'a':
                    dictionary = applications_linux

                with open(f'/home/{getuser()}/config.tcc', 'w+') as file:
                    for line in lines:
                        if get_key(package_name, dictionary) in line:
                            continue
                        else:
                            file.write(line)

                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()


                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

    def clean(self, password: str):
        if platform == 'linux':
            try:
                install_progress = Spinner(message='Cleaning Up Packages ')

                for _ in range(1, 75):
                    time.sleep(0.007)
                    install_progress.next()

                proc = Popen('sudo apt-get -y autoremove'.split(),
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)

                proc.communicate(password.encode())

                for _ in range(1, 26):
                    time.sleep(0.007)
                    install_progress.next()

                click.echo('\n')
                click.echo(
                    click.style(
                        '🎉 Successfully Cleaned Turbocharge! 🎉',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

        elif platform == 'win32':
            pass  # chocolatey auto removes files
        
        elif platform == 'darwin':
            try:
                install_progress = Spinner(message='Cleaning Up Packages ')

                for _ in range(1, 75):
                    time.sleep(0.007)
                    install_progress.next()

                proc = Popen('brew cleanup'.split(),
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)

                # proc.communicate(password.encode())

                for _ in range(1, 26):
                    time.sleep(0.007)
                    install_progress.next()

                click.echo('\n')
                click.echo(
                    click.style(
                        '🎉 Successfully Cleaned Turbocharge! 🎉',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

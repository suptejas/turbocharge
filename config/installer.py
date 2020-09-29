from sys import platform
import click
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
from subprocess import Popen, PIPE, DEVNULL, run
from getpass import getuser
from Debugger import Debugger
import subprocess
from src import constants as c
from Debugger import Debugger
from getpass import getpass, getuser
from os.path import isfile
import os
from Installable import Installable



def show_progress(finding_bar):
    for _ in range(1, 2):
        time.sleep(0.01)
        finding_bar.next()
    click.echo('\n')

def install(theLine: str):
    '''
    Install A Specified Package(s)
    '''
    decoded = theLine.split(" ")
    package_name = decoded[0]
    package_version = decoded[1]
    package_type = decoded[2]
    linux_compat = decoded[3]
    win_compat = decoded[4]
    dar_compat = decoded[5]

    if platform == 'linux' and linux_compat == 1:
        password = getpass('Enter your password: ')
        try:
            installer_progress = Spinner(
                message=f'Installing {package_name}...', max=100)

            if package_type == 'p':
                script = f'sudo -S apt-get install -y {package_name}={package_version}'
            elif package_type == 'a':
                script = f'sudo -S snap install --classic {package_name}={package_version}'
            # sudo requires the flag '-S' in order to take input from stdin
            for _ in range(1, 75):
                time.sleep(0.01)
                installer_progress.next()

            proc = Popen(
                script.split(),
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE)

            # Popen only accepts byte-arrays so you must encode the string
            output, error = proc.communicate(password.encode())

            if proc.returncode != 0:
                click.echo(
                    click.style(
                        '❎ Installation Failed... ❎',
                        fg='red',
                        blink=True,
                        bold=True))

                debug = click.prompt(
                    'Would you like us to debug the failed installation?[y/n]')

                if debug == 'y':
                    debugger = Debugger()
                    debugger.debug(password, error)

                    logs = click.prompt(
                        'Would you like to see the logs?[y/n]', type=str)

                    if logs == 'y':
                        final_output = error.decode('utf-8')

                        if final_output == '':
                            click.echo('There were no logs found...')

                            return
                        else:
                            click.echo(final_output)

                            return
                    return
                else:
                    logs = click.prompt(
                        'Would you like to see the logs?[y/n]', type=str)

                    if logs == 'y':
                        final_output = output.decode('utf-8')

                        if final_output == '':
                            click.echo('There were no logs found...')

                            return
                        else:
                            click.echo(final_output)

                            return
                    return

            click.echo(
                click.style(
                    f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n',
                    fg='green',
                    bold=True))

            testing_bar = IncrementalBar('Testing package...', max=100)
            for _ in range(1, 21):
                time.sleep(0.002)
                testing_bar.next()
            if package_type == 'p':
                test_script = f'{package_name} --version'
                proc = Popen(
                    test_script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

            for _ in range(22, 101):
                time.sleep(0.002)
                testing_bar.next()
        except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)
        
    elif platform == 'win32' and win_compat == 1:
        installer_progress = Spinner(
                message=f'Installing {package_name}...', max=100)
        try:
            for _ in range(1, 75):
                time.sleep(0.01)
                installer_progress.next()

            run(f"choco install {package_name} --version {package_version}", stdout=PIPE, stderr=PIPE) # first time

            for _ in range(1, 25):
                time.sleep(0.01)
                installer_progress.next()

            # Haven't implemented debug because .run() doesn't offer
            # communicate() function

            click.echo(
                click.style(
                    f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n',
                    fg='green',
                    bold=True))
            
            if package_type == 'p':
                testing_bar = IncrementalBar('Testing package...', max=100)

                test_script = f"{package_name} --version"
                tests_passed=[f'{c.devpackages_windows[package_name]} Version']

                
                # this condition will be true for all application package stuff
                for _ in range(1, 64):
                    time.sleep(0.002)
                    testing_bar.next()
                
                run(test_script, stdout=PIPE, stderr=PIPE)
                
                for _ in range(64, 101):
                    time.sleep(0.002)
                    testing_bar.next()

                click.echo('\n')

                for test in tests_passed:
                    click.echo(
                        click.style(
                            f'Test Passed: {test} ✅\n',
                            fg='green'))
            elif package_type == 'a':
                click.echo('\n')
                click.echo(
                    click.style(
                        f'Test Passed: {package_name} Launch ✅\n',
                        fg='green'))

            return
        except Exception as e:
            click.echo(e)
            click.echo('An Error Occured During Installation...', err=True)
    elif platform == 'darwin' and dar_compat == 1:
        try:
            installer_progress = Spinner(
                message=f'Installing {package_name}...', max=100)

            # sudo requires the flag '-S' in order to take input from stdin
            if package_type == 'a':
                script = f"brew install {package_name}"
                test_script = f"{package_name} --version"
                tests_passed=[
                        f'{c.devpackages_macos[package_name]} Version']
            elif package_type == 'p':
                script = f"brew cask install {package_name}"
                test_script = ""
                tests_passed = []

            for _ in range(1, 75):
                time.sleep(0.01)
                installer_progress.next()

            proc = Popen(
                script.split(),
                stdout=PIPE,
                stdin=PIPE,
                stderr=PIPE)

            # Popen only accepts byte-arrays so you must encode the string
            output, error = proc.communicate(password.encode())

            if proc.returncode != 0:
                click.echo(
                    click.style(
                        '❎ Installation Failed... ❎',
                        fg='red',
                        blink=True,
                        bold=True))

                debug = click.prompt(
                    'Would you like us to debug the failed installation?[y/n]')

                if debug == 'y':
                    debugger = Debugger()
                    debugger.debug(password, error)

                    logs = click.prompt(
                        'Would you like to see the logs?[y/n]', type=str)

                    if logs == 'y':
                        final_output = error.decode('utf-8')

                        if final_output == '':
                            click.echo('There were no logs found...')

                            return
                        else:
                            click.echo(final_output)

                            return
                    return
                else:
                    logs = click.prompt(
                        'Would you like to see the logs?[y/n]', type=str)

                    if logs == 'y':
                        final_output = output.decode('utf-8')

                        if final_output == '':
                            click.echo('There were no logs found...')

                            return
                        else:
                            click.echo(final_output)

                            return
                    return

            click.echo(
                click.style(
                    f'\n\n 🎉  Successfully Installed {package_name}! 🎉 \n',
                    fg='green',
                    bold=True))

            # Testing the successful installation of the package
            testing_bar = IncrementalBar('Testing package...', max=100)

            if tests_passed == [] and test_script == '':
                                    
                click.echo('\n')
                click.echo(
                    click.style(
                        f'Test Passed: {package_name} Launch ✅\n',
                        fg='green'))

                return

            for _ in range(1, 21):
                time.sleep(0.002)
                testing_bar.next()

            for _ in range(21, 60):
                time.sleep(0.002)
                testing_bar.next()

            proc = Popen(
                test_script.split(),
                stdin=PIPE,
                stdout=PIPE,
                stderr=PIPE)

            for _ in range(60, 101):
                time.sleep(0.002)
                testing_bar.next()

            click.echo('\n')

            for test in tests_passed:
                click.echo(
                    click.style(
                        f'Test Passed: {test} ✅\n',
                        fg='green'))

        except subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occured During Installation...', err=True)

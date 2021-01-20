from sys import platform
import click
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
from subprocess import Popen, PIPE, run
from colorama import Fore
from getpass import getuser
from Debugger import Debugger
import subprocess
from constants import applications_windows, devpackages_windows, applications_linux, devpackages_linux, applications_macos, devpackages_macos
from os.path import isfile
import os
from miscellaneous import is_admin
import halo

class Installer:
    def install_task(self, package_name: str, script: str,
                     password: str, test_script: str, tests_passed):
        def get_key(val, dictionary):
            for key, value in dictionary.items():
                if val == value:
                    return key
            return -1
        
        def getWinVer(output : str, name : str):
            lines = output.split('\n')
            for line in lines:
                line = line.split()
                version = line[1]
                package_name = line[0]
                if name == package_name:
                    final = version
                    break
            return final

        def subprocess_cmd(command):
                    process = subprocess.Popen(
                        command, stdout=subprocess.PIPE, stdin=PIPE, stderr=PIPE)
                    proc_stdout = process.communicate()[0].strip()
                    decoded = proc_stdout.decode("utf-8")
                    version_tag = decoded.split("\n")[1]
                    # using [1:] might be useful in some scenario where the
                    # version has multiple colons in it.
                    cleaned_version = version_tag.split(": ")[1]
                    return cleaned_version

        def parse(string):
            var1 = string.split(": ")
            if len(var1[1]) >7:
                var2 = var1[1].split(" ")
                return var2[1]
            else:
                var2 = var1[1].split("\n")
                return var2[0]

        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Installing {package_name}...', max=100)

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

                package_type = None
                
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'


                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max=100)

                if tests_passed == [] and test_script == '':

                    if package_type == 'a':
                        file_exists = False
                        if isfile(f'/home/{getuser()}/config.tcc'):
                            file_exists = True
            
                        if file_exists:
                            with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                                lines = file.readlines()

                            package_exists = False

                            for line in lines:
                                if get_key(package_name, applications_linux) in line:
                                    package_exists = True

                            # The order for the package compatiblity numbers is
                            # Linux, Windows, MacOS
                            if package_exists == False:
                                with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                                    file.write(
                                        f'{get_key(package_name, applications_linux)} None {package_type} 1 {0 if get_key(package_name, applications_windows)==-1 else 1} {0 if get_key(package_name, applications_macos)==-1 else 1}\n')
                    
                    
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

                

                package_type = None
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'


                if package_type == 'p':

                    file_exists = False
                    if isfile(f'/home/{getuser()}/config.tcc'):
                        file_exists = True
                                        
                    package_version = subprocess_cmd(
                        f'apt show {get_key(package_name, devpackages_linux)}'.split())
                    

                    if file_exists:
                        with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                            lines = file.readlines()

                        package_exists = False

                        for line in lines:
                            if get_key(package_name, devpackages_linux) in line:
                                package_exists = True

                        if package_exists == False:
                            with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                                file.write(
                                    f'{get_key(package_name, devpackages_linux)} {package_version} {package_type} 1 {0 if get_key(package_name, devpackages_windows)==-1 else 1} {0 if get_key(package_name, devpackages_macos)==-1 else 1}\n')
                    
                    
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

        elif platform == 'win32':
            if is_admin():
                try:
                    with halo.Halo(text=f'Installing {package_name}'):
                        run(script, stdout=PIPE, stderr=PIPE) # first time

                    click.echo(
                        click.style(
                            f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n',
                            fg='green',
                            bold=True))

                    testing_bar = IncrementalBar('Testing package', max=100)

                    # this condition will be true for all applications

                    if tests_passed == [] and test_script == '':
                        # Dont run any tests, just exit
                        
                        click.echo('\n')
                        click.echo(
                            click.style(
                                f'Test Passed: {package_name} Launch ✅\n',
                                fg='green'))

                        return
                    
                    for _ in range(1, 64):
                        time.sleep(0.002)
                        testing_bar.next()
                    
                    
                    run(test_script, stdout=PIPE, stderr=PIPE)
                    
                    inApp = get_key(package_name, applications_windows)
                    inDev = get_key(package_name, devpackages_windows)
                    w_version = subprocess.Popen("clist -l", stdin= PIPE, stderr=PIPE, stdout=PIPE)
                    output = w_version.communicate()[0].decode()
                    package_exists = False
                    with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'r') as f:
                        lines = f.readlines()
                    for i in range(len(lines)):
                        if (str(inApp) in lines[i]) or (str(inDev) in lines[i]):
                            package_exists = True
                            break
                    if not package_exists:
                        if inApp != -1:
                            version = getWinVer(output,inApp)
                            with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'a+') as f:
                                f.write(f'{inApp} {version} a {0 if get_key(package_name, applications_windows)==-1 else 1} 1 {0 if get_key(package_name, applications_macos)==-1 else 1}\n')
                        elif inDev != -1:
                            version = getWinVer(output, inDev)
                            with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'a+') as f:
                                f.write(f'{inDev} {version} p {0 if get_key(package_name, devpackages_windows)==-1 else 1} 1 {0 if get_key(package_name, devpackages_macos)==-1 else 1}\n')
                            
                    for _ in range(64, 101):
                        time.sleep(0.002)
                        testing_bar.next()

                    click.echo('\n')

                    for test in tests_passed:
                        click.echo(
                            click.style(
                                f'Test Passed: {test} ✅\n',
                                fg='green'))

                    return

                except Exception as e:
                    click.echo(e)
                    click.echo('An Error Occured During Installation...', err=True)
            else:
                print(f'{Fore.RED}Installation Must Be Run As Administrator{Fore.RESET}')
        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Installing {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
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

                

                package_type = None

                if 'brew install' in script:
                    package_type = 'p'
                elif 'brew cask install' in script:
                    package_type = 'a'

                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max=100)

                if tests_passed == [] and test_script == '':
                    if package_type == 'a':
                        file_exists = False
                        if isfile(f'/Users/{getuser()}/config.tcc'):
                            file_exists = True
            
                        if file_exists:
                            with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                                lines = file.readlines()

                            package_exists = False

                            for line in lines:
                                if get_key(package_name, applications_macos) in line:
                                    package_exists = True

                            # The order for the package compatiblity numbers is
                            # Linux, Windows, MacOS
                            if package_exists == False:
                                with open(f'/Users/{getuser()}/config.tcc', 'a+') as file:
                                    file.write(
                                        f'{get_key(package_name, applications_macos)} None {package_type} {0 if get_key(package_name, applications_linux)==-1 else 1} {0 if get_key(package_name, applications_windows)==-1 else 1} 1\n')

                        
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

                package_type = None
                if 'brew install' in script:
                    package_type = 'p'
                elif 'brew cask install' in script:
                    package_type = 'a'

                if package_type == 'p':
                    file_exists = False
                    if isfile(f'/Users/{getuser()}/config.tcc'):
                        file_exists = True

                    proc = Popen(f'brew info {package_name}'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                    stdout = proc.communicate()
                    parsing = stdout[0].decode('utf-8')
                    
                    package_version = parse(parsing)

                    if file_exists:
                        with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                            lines = file.readlines()

                        line_exists = False

                        for line in lines:
                            if get_key(package_name, devpackages_macos) in line:
                                line_exists = True
                        
                        #TODO : Implement versioning for macOS
                        with open(f'/Users/{getuser()}/config.tcc', 'a+') as file:
                            if line_exists == False:
                                file.write(
                                        f'{get_key(package_name, applications_macos)} None {package_type} {0 if get_key(package_name, devpackages_linux)==-1 else 1} {0 if get_key(package_name, devpackages_windows)==-1 else 1} 1\n')

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

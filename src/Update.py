from sys import platform
import click
import subprocess
from subprocess import Popen, PIPE, DEVNULL, run
import time
from progress.spinner import Spinner
from getpass import getuser
import os
from os.path import isfile
from constants import applications_windows, devpackages_windows, applications_linux, devpackages_linux, applications_macos, devpackages_macos


class Updater:
    # the pacakage name here is directly as typed by user, hence like the keys of
    # dictionaries we have in constants.py . So no need on using getKey() here.
    
    def updatepack(self, package_name: str, password: str):
        def subprocess_cmd(command):
            process = subprocess.Popen(
                command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
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
            
        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Updating {devpackages_linux[package_name]}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(
                    f'sudo -S apt-get install --only-upgrade -y {package_name}'.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE
                )

                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())



                package_type = 'p'

                package_version = subprocess_cmd(
                    f'apt show {package_name}'.split())


                if isfile(f'/home/{getuser()}/config.tcc'):
                    file_exists = True
            
                if file_exists:
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()

                    package_exists = False
                    package_idx = -1
                    for i in range(len(lines)):
                        if (package_name in lines[i]):
                            package_exists = True
                            package_idx = i
                            break
                    lines[package_idx] = f'{package_name} {package_version} {package_type} 1 {1 if package_name in devpackages_windows.keys() else 0} {1 if package_name in devpackages_macos.keys() else 0}\n'

                    # The order for the package compatiblity numbers is
                    # Linux, Windows, MacOS
                    if package_exists == False:
                        with open(f'/home/{getuser()}/config.tcc', 'w') as file:
                            file.writelines(lines)

                for _ in range(1, 26):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {devpackages_linux[package_name]}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

        if platform == 'win32':
            try:
                installer_progress = Spinner(
                    message=f'Updating {devpackages_windows[package_name]}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(f'choco upgrade {package_name} -y',
                    stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {devpackages_windows[package_name]}! 🎉 \n',
                        fg='green'))
                
                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'r') as file:
                    lines = file.readlines()

                package_exists = False

                w_version = subprocess.Popen("clist -l", stdin= PIPE, stderr=PIPE, stdout=PIPE)
                output = w_version.communicate()
                version = getWinVer(output,package_name)
                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} p {1 if package_name in devpackages_linux.keys() else 0} 1 {1 if package_name in devpackages_macos.keys() else 0}\n'

                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'w') as file:
                    file.writelines(lines)

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)
        
        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(f'brew upgrade {package_name}'.split(),
                    stdout=PIPE, stderr=PIPE)

                package_type = 'p'

                proc = Popen(f'brew info {package_name}'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output = proc.communicate()
                parsable = output[0].decode('utf-8')

                package_version = parse(parsable)

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} p {1 if package_name in devpackages_linux.keys() else 0} {1 if package_name in devpackages_windows.keys() else 0} 1\n'

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    file.writelines(lines)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

    def updateapp(self, package_name: str, password: str):
        def subprocess_cmd(command):
            process = subprocess.Popen(
                command, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            proc_stdout = process.communicate()[0].strip()
            decoded = proc_stdout.decode("utf-8")
            version_tag = decoded.split("\n")[1]
            # using [1:] might be useful in some scenario where the
            # version has multiple colons in it.
            cleaned_version = version_tag.split(": ")[1]
            return cleaned_version
        
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
                    message=f'Updating {package_name}...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()
                proc = Popen(
                    f'sudo -S snap refresh -y {package_name}'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())
                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(1, 26):
                    time.sleep(0.01)
                    installer_progress.next()
                click.echo(click.style(
                    f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n', fg='green'))

                #TODO: possible bug here.
                package_version = subprocess_cmd(
                    f'snap info {package_name}'.split())


                if isfile(f'/home/{getuser()}/config.tcc'):
                    file_exists = True
            
                if file_exists:
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()

                    package_exists = False
                    package_idx = -1
                    for i in range(len(lines)):
                        if (package_name in lines[i]):
                            package_exists = True
                            package_idx = i
                            break
                    lines[package_idx] = f'{package_name} {package_version} a 1 {1 if package_name in devpackages_windows.keys() else 0} {1 if package_name in devpackages_macos.keys() else 0}\n'

                    # The order for the package compatiblity numbers is
                    # Linux, Windows, MacOS
                    if package_exists == False:
                        with open(f'/home/{getuser()}/config.tcc', 'w') as file:
                            file.writelines(lines)

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating...', err=True)

        if platform == 'win32':
            try:
                installer_progress = Spinner(
                    message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(f'choco upgrade {package_name} -y',
                    stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n',
                        fg='green'))
                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'r') as file:
                    lines = file.readlines()

                package_exists = False

                w_version = subprocess.Popen("clist -l", stdin= PIPE, stderr=PIPE, stdout=PIPE)
                output = w_version.communicate()
                version = getWinVer(output,package_name)
                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} p {1 if package_name in devpackages_linux.keys() else 0} 1 {1 if package_name in devpackages_macos.keys() else 0}\n'

                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'w') as file:
                    file.writelines(lines)

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)
                
        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(f'brew cask upgrade {package_name}',
                    stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(f'brew info {package_name}'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output = proc.communicate()
                parsable = output[0].decode('utf-8')
                
                package_version = parse(parsable)

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} a {1 if package_name in devpackages_linux.keys() else 0} {1 if package_name in devpackages_windows.keys() else 0} 1\n'

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    file.writelines(lines)

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

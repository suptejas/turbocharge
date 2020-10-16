#   Copyright 2020 Turbocharge
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import click
import os
import subprocess
import time
import constants as constant
from sys import platform, stderr
from getpass import getpass, getuser
from progress.spinner import Spinner
from progress.bar import IncrementalBar
from subprocess import Popen, PIPE, DEVNULL, run
from src.constants import applications_windows, devpackages_windows, applications_linux, devpackages_linux, apt_script, apt_remove, snap_script, snap_remove, display_list_linux, display_list_windows, display_list_macos, hyperpkgs, devpackages_macos, applications_macos
from src.miscellaneous import show_progress, is_password_valid, find
from src.Install import Installer
from src.Uninstall import Uninstaller
from src.Update import Updater
from src.config_helper import Setup
from os.path import isfile


__version__ = '1.0.0b'

setup = Setup()


@click.group()
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    if platform == 'linux':
        if not isfile(f'/home/{getuser()}/config.tcc'):
            setup.setup()

    elif platform == 'win32':
        if not isfile(os.path.join("C:\\Turbocarge", "config.tcc")):
            setup.setup()

    elif platform == 'darwin':
        if not isfile(f'/Users/{getuser()}/config.tcc'):
            setup.setup()


@cli.command()
@click.argument('package_list', required=True)
def install(package_list):
    '''
    Install A Specified Package(s)
    '''
    if platform == 'linux' or platform == 'darwin':
        password = getpass('Enter your password: ')
    else:
        password = ''
        # otherwise the variable would be undefined..

    packages = package_list.split(',')
    turbocharge = Installer()

    click.echo('\n')

    os_bar = IncrementalBar('Getting Operating System...', max=1)
    os_bar.next()

    for package_name in packages:
        package_name = package_name.strip(' ')

        if platform == 'linux':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_linux:
                show_progress(finding_bar)
                turbocharge.install_task(
                    devpackages_linux[package_name],
                    f'{apt_script} {package_name}',
                    password,
                    f'{package_name} --version',
                    [f'{devpackages_linux[package_name]} Version'])

            if package_name in applications_linux:
                show_progress(finding_bar)
                turbocharge.install_task(
                    applications_linux[package_name],
                    f'{snap_script} {package_name}',
                    password,
                    '',
                    [])

            if package_name == 'chrome':
                show_progress(finding_bar)
                try:
                    click.echo('\n')

                    password = getpass("Enter your password: ")

                    installer_progress = Spinner(
                        message='Installing Chrome...', max=100)

                    for _ in range(1, 75):
                        time.sleep(0.03)
                        installer_progress.next()

                    click.echo(
                        click.style(
                            '\n Chrome Will Take 2 to 4 Minutes To Download... \n',
                            fg='yellow'))

                    os.system(constant.chrome_link)

                    os.system(constant.chrome_move)

                    second = Popen(
                        constant.chrome_setup.split(),
                        stdin=PIPE,
                        stdout=PIPE,
                        stderr=PIPE
                    )
                    # Popen only accepts byte-arrays so you must encode the
                    # string
                    second.communicate(password.encode())

                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(
                        click.style('\n\n 🎉 Successfully Installed Chrome! 🎉 \n'))
                    # Testing the successful installation of the package
                    testing_bar = IncrementalBar('Testing package...', max=100)
                    for _ in range(1, 21):
                        time.sleep(0.045)
                        testing_bar.next()

                    for _ in range(21, 60):
                        time.sleep(0.045)
                        testing_bar.next()
                    for _ in range(60, 101):
                        time.sleep(0.03)
                        testing_bar.next()
                    click.echo('\n')
                    click.echo(
                        click.style(
                            'Test Passed: Chrome Launch ✅\n',
                            fg='green'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Installation...', err=True)

            if package_name == 'anaconda':
                show_progress(finding_bar)

                try:
                    installer_progress = Spinner(
                        message=f'Installing {package_name}...', max=100)
                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 35):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.anaconda_download)
                    for _ in range(35, 61):
                        time.sleep(0.01)
                        installer_progress.next()

                    os.system(constant.anaconda_setup)

                    for _ in range(61, 91):
                        time.sleep(0.01)
                        installer_progress.next()

                    os.system(constant.anaconda_PATH)

                    for _ in range(90, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(
                        click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Installation...', err=True)

            if package_name == 'miniconda':
                show_progress(finding_bar)
                try:
                    installer_progress = Spinner(
                        message=f'Installing {package_name}...', max=100)
                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 35):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.miniconda_download)
                    for _ in range(35, 61):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.miniconda_setup)
                    for _ in range(61, 91):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.miniconda_PATH)
                    for _ in range(90, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(
                        click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Installation...', err=True)

            elif package_name not in devpackages_linux and package_name not in applications_linux and package_name != 'chrome' and package_name != 'anaconda' and package_name != 'miniconda':
                click.echo('\n')
                click.echo(click.style(':( Package Not Found! :(', fg='red'))
                suggestions = find(package_name)
                if suggestions != []:
                    click.echo('\n')
                    click.echo('Turbocharge found similar packages: \n')
                    for suggestion in suggestions:
                        click.echo(f'{suggestion} \n')
                else:
                    click.echo(
                        'Turbocharge couldn\'t find similar packages...')

        if platform == 'win32':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_windows:
                show_progress(finding_bar)

                turbocharge.install_task(
                    package_name=devpackages_windows[package_name],
                    script=f"choco install {package_name} -y --force",
                    password="",
                    test_script=f"{package_name} --version",
                    tests_passed=[
                        f'{devpackages_windows[package_name]} Version']
                )

            elif package_name in applications_windows:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=applications_windows[package_name],
                    script=f"choco install {package_name} -y --force",
                    password="",
                    test_script="",
                    tests_passed=[]
                )

            elif package_name not in devpackages_windows and package_name not in applications_windows:
                click.echo('\n')
                click.echo(click.style(':( Package Not Found! :(', fg='red'))

                suggestions = find(package_name)
                if suggestions != []:
                    click.echo('\n')
                    click.echo('Turbocharge found similar packages: \n')
                    for suggestion in suggestions:
                        click.echo(f'{suggestion} \n')
                else:
                    click.echo(
                        'Turbocharge couldn\'t find similar packages...')

        if platform == 'darwin':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_macos:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=devpackages_macos[package_name],
                    script=f"brew install {package_name}",
                    password="",
                    test_script=f"{package_name} --version",
                    tests_passed=[
                        f'{devpackages_macos[package_name]} Version']
                )
                # test _scirpt is just a string here..

            elif package_name in applications_macos:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=applications_macos[package_name],
                    script=f"brew cask install {package_name}",
                    password="",
                    test_script="",
                    tests_passed=[]
                )

            elif package_name not in devpackages_macos and package_name not in applications_macos:
                click.echo('\n')
                click.echo(click.style(
                    ':( Package Not Found! :( \n', fg='red'))
                suggestions = find(package_name)
                if suggestions != []:
                    click.echo('\n')
                    click.echo('Turbocharge found similar packages: \n')
                    for suggestion in suggestions:
                        click.echo(f'{suggestion} \n')
                else:
                    click.echo(
                        'Turbocharge couldn\'t find similar packages...')


@cli.command()
@click.argument('package_list', required=True)
def remove(package_list):
    '''
    Uninstall Applications And Packages
    '''
    uninstaller = Uninstaller()

    if platform == 'linux' or platform == 'darwin':
        password = getpass('Enter your password: ')
    else:
        password = ''

    packages = package_list.split(',')

    for package in packages:
        if platform == 'linux':
            if package in devpackages_linux:
                uninstaller.uninstall(
                    f'{apt_remove} {package}',
                    password,
                    package_name=devpackages_linux[package])

            if package in applications_linux:
                uninstaller.uninstall(
                    f'{snap_remove} {package}',
                    password,
                    package_name=applications_linux[package])

            if package == 'anaconda':
                try:
                    installer_progress = Spinner(
                        message=f'Uninstalling Anaconda...', max=100)
                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 75):
                        time.sleep(0.007)
                        installer_progress.next()

                    os.system(constant.anaconda_remove_folder)
                    os.system(constant.anaconda_remove_file)

                    with open('.bashrc', 'r') as file:
                        lines = file.read()

                    with open('.bashrc', 'w') as file:
                        for line in lines:
                            if 'anaconda' in line or 'miniconda' in line:
                                continue
                            else:
                                file.write(line)

                    # stdoutput = (output)[0].decode('utf-8')
                    for _ in range(75, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    click.echo(click.style(
                        f'\n\n 🎉 Successfully Uninstalled Anaconda! 🎉 \n', fg='green'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Uninstallation...', err=True)

            if package == 'miniconda':
                try:
                    installer_progress = Spinner(
                        message=f'Uninstalling Miniconda...', max=100)

                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 75):
                        time.sleep(0.007)
                        installer_progress.next()

                    os.system(constant.miniconda_remove_folder)
                    os.system(constant.miniconda_remove_file)

                    with open('.bashrc', 'r') as file:
                        lines = file.read()

                    with open('.bashrc', 'w') as file:
                        for line in lines:
                            if 'anaconda' in line or 'miniconda' in line:
                                continue
                            else:
                                file.write(line)

                    # stdoutput = (output)[0].decode('utf-8')
                    for _ in range(1, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    click.echo(click.style(
                        f'\n\n 🎉 Successfully Uninstalled Miniconda! 🎉 \n', fg='green'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Uninstallation...', err=True)

        if platform == 'win32':
            if package in devpackages_windows:
                uninstaller.uninstall(
                    f'choco uninstall {package} -y',
                    password="",
                    package_name=devpackages_windows[package]
                )

            elif package in applications_windows:
                uninstaller.uninstall(
                    f'choco uninstall {package}',
                    password="",
                    package_name=applications_windows[package]
                )

        if platform == 'darwin':
            if package in devpackages_windows:
                uninstaller.uninstall(
                    f'brew uninstall {package}',
                    password="",
                    package_name=devpackages_macos[package]
                )
            elif package in applications_windows:
                uninstaller.uninstall(
                    f'brew cask uninstall {package}',
                    password="",
                    package_name=applications_macos[package]
                )


@cli.command()
@click.argument('package_list', required=True)
def update(package_list):
    '''
    Update Applications And Packages
    '''
    updater = Updater()

    if platform == 'linux' or platform == 'darwin':
        password = getpass('Enter your password: ')
    else:
        password = ''

    packages = package_list.split(',')

    for package in packages:
        if platform == "linux":
            if package in devpackages_linux:
                updater.updatepack(package, password)

            if package in applications_linux:
                updater.updateapp(package, password)

            else:
                return
        if platform == "win32":
            if package in devpackages_windows:
                updater.updatepack(package, "")

            if package in applications_windows:
                updater.updateapp(package, "")

            else:
                return
        if platform == "darwin":
            if package in devpackages_macos:
                updater.updatepack(package, password)

            if package in applications_macos:
                updater.updateapp(package, password)

            else:
                return


@cli.command()
@click.argument('hyperpack_list', required=True)
def hyperpack(hyperpack_list):
    '''
    Install Large Packs Of Applications And Packages
    '''
    os_bar = IncrementalBar('Getting Operating System...', max=1)
    os_bar.next()

    installer = Installer()
    updater = Updater()
    cleaner = Uninstaller()

    hyperpacks = hyperpack_list.split(',')

    password = ""

    if platform == 'linux' or platform == 'darwin':
        password = getpass('Enter your password: ')
        click.echo('\n')

        password_bar = IncrementalBar('Verifying Password...', max=1)

        exitcode = is_password_valid(password)

        if exitcode == 1:
            click.echo('Wrong Password Entered... Aborting Installation!')
            return

        password_bar.next()

    click.echo('\n')
    if platform == 'linux':
        for hyperpack in hyperpacks:
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            # Installing Required Packages
            for package in packages:
                installer.install_task(
                    devpackages_linux[package],
                    f'sudo -S apt-get install -y {package}',
                    password,
                    f'{package} --version',
                    [f'{devpackages_linux[package]} Version'])

            # Installing Required Applications
            for app in apps:
                installer.install_task(
                    applications_linux[app],
                    f'sudo -S snap install --classic {app}',
                    password,
                    '',
                    [])

            # Updating Required Packages
            for package in packages:
                updater.updatepack(package, password)

            for app in apps:
                updater.updateapp(app, password)

            cleaner.clean(password)

    elif platform == 'win32':
        for hyperpack in hyperpacks:
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            for package in packages:
                installer.install_task(
                    package_name=devpackages_windows[package],
                    script=f'choco install {package} -y',
                    password="",
                    test_script=f'{package} --version',
                    tests_passed=[f'{devpackages_windows[package]} Version']
                )

            for package in packages:
                updater.updatepack(package, password="")

            for app in apps:
                installer.install_task(
                    package_name=applications_windows[app],
                    script=f'choco install {app} -y',
                    password="",
                    test_script='',
                    tests_passed=[]
                )

            for app in apps:
                updater.updateapp(app, password="")
    elif platform == 'darwin':
        for hyperpack in hyperpacks:
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            for package in packages:
                installer.install_task(
                    package_name=devpackages_macos[package],
                    script=f'brew install {package}',
                    password="",
                    test_script=f'{package} --version',
                    tests_passed=[f'{devpackages_macos[package]} Version']
                )

            for package in packages:
                updater.updatepack(package, password="")

            for app in apps:
                installer.install_task(
                    package_name=applications_macos[app],
                    script=f'brew cask install {app}',
                    password="",
                    test_script='',
                    tests_passed=[]
                )

            for app in apps:
                updater.updateapp(app, password="")


@cli.command()
@click.argument('text', required=True)
def search(text):
    '''
    Search For A Package To Install
    '''
    click.echo(f'Searching for packages...')

    suggestions = find(text)

    for suggestion in suggestions:
        click.echo(f'{suggestion} \n')


@cli.command()
def clean():
    '''
    Remove Junk Packages Which Are Not Needed
    '''
    if platform == 'linux':
        uninstaller = Uninstaller()
        password = getpass('Enter your password: ')
        uninstaller.clean(password)

    if platform == 'win32':
        arr = ['|', "/", "-", "\\"]

        slen = len(arr)

        print('Cleaning Your PC...')

        for i in range(1, 60):
            time.sleep(0.04)
            print(arr[i % slen], end='\r')

    elif platform == 'darwin':
        uninstaller = Uninstaller()
        password = getpass('Enter your password: ')
        uninstaller.clean(password)


@cli.command()
def list():
    '''
    Applications And Packages TurboCharge Supports
    '''
    if platform == 'linux':
        click.echo(click.style(display_list_linux, fg='white'))

    elif platform == 'win32':
        click.echo(click.style(display_list_windows, fg='white'))

    elif platform == 'darwin':
        click.echo(click.style(display_list_macos, fg='white'))


@cli.command()
def local():
    '''
    Lists all the installed packages.
    '''

    if platform == 'linux':
        packages = []
        applications = []

        lines = None

        with open(f'/home/{getuser()}/config.tcc', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            line.split()
            try:
                package_name = line.split()[0]
            except IndexError:
                continue
            try:
                package_type = line.split()[2]
            except IndexError:
                continue

            if package_type == 'p':
                packages.append(package_name)

            if package_type == 'a':
                applications.append(package_name)

        click.clear()
        click.echo('Packages : \n')

        if packages != []:
            for package in packages:
                click.echo(package + '\n')

        elif packages == []:
            click.echo('Turbocharge couldn\'t find any packages installed.')

        click.echo('Applications : \n')

        if applications != []:
            for app in applications:
                click.echo(app + '\n')

        elif applications == []:
            click.echo(
                'Turbocharge couldn\'t find any applications installed. \n')

    if platform == 'win32':
        packages = []

        cmd = run('clist -l', stdout=PIPE, stderr=PIPE)

        output = cmd.stdout.decode()

        lines = output.split('\n')

        for line in lines:
            if not 'Chocolatey' in line and not 'chocolatey' in line and 'packages installed' not in line:
                packages.append(line)

        result = "Packages installed:\n"

        for p in packages:
            result += p
            result += "\n"

        click.echo(result)

    if platform == 'darwin':
        packages = []
        applications = []

        lines = None

        with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            line.split()
            try:
                package_name = line.split()[0]
            except IndexError:
                continue
            try:
                package_type = line.split()[2]
            except IndexError:
                continue
            if package_type == 'p':
                packages.append(package_name)

            if package_name == 'a':
                applications.append(package_name)

        click.echo('Packages : \n')

        if packages != []:
            for package in packages:
                click.echo(package)

        elif packages == []:
            click.echo('Turbocharge couldn\'t find any packages installed.')

        click.echo('Applications : \n')

        if applications != []:
            for app in applications:
                click.echo(app)

        elif applications == []:
            click.echo('Turbocharge couldn\'t find any applications installed.')

<<<<<<< HEAD
import click
import os
import subprocess
from subprocess import CalledProcessError
from sys import platform
from getpass import getpass, getuser
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
from subprocess import Popen, PIPE, DEVNULL

applications = {
        'android-studio': 'Android Studio',
        'atom' : 'Atom',
        'blender' : 'Blender',
        'brackets' : 'Brackets',
        'clion' : 'C Lion',
        'discord' : 'Discord',
        'datagrip' : 'Data Grip',
        'libreoffice' : 'Libre Office',
        'librepcb' : 'Libre PCB',
        'opera' : 'Opera',
        'webstorm' : 'Web Storm',
        'pycharm': 'Pycharm Community',
        'sublime-text': 'Sublime Text',
        'code' : 'Visual Studio Code',
        'code-insiders' : 'Visual Studio Code Insiders',  
        'eclipse' : 'Eclipse',
        'powershell' : 'Powershell',
        'kotlin' : 'Kotlin',
        'goland' : 'Go Land',
        'rubymine' : 'RubyMine',
        'figma-linux' : 'Figma',
    }

devpackages = {
        'git' : 'Git',
        'curl' : 'Curl',
        'docker' : 'Docker',
        'npm' : 'Npm',
        'zsh' : 'Zsh',
        'emacs' : 'Emacs',
        'neovim' : 'Neo Vim',
        'vim' : 'Vim',
        'htop' : 'Htop',
        'sqlite' : 'Sqlite',
        'tldr' : 'Tldr',
        'jq' : 'JQ',
        'ncdu' : 'Ncdu',
        'taskwarrior' : 'Task Warrior',
        'tmux' : 'Tmux',
        'patchelf' : 'Patchelf',
        'golang' : 'Go-Lang',
        'rust' : 'Rust',
        'zlib' : 'Z-Lib',
    }

class HyperPack:
    def __init__(self, packages, applications):
        self.packages = packages
        self.applications = applications

hyperpkgs = {
    'essential' : HyperPack('git,curl,npm,zsh,vim', 'code,atom,sublime-text'),
    'office' : HyperPack('sqlite', 'libreoffice')
} 


def is_password_valid(password : str):
    proc = subprocess.Popen('sudo -k -S -l'.split(), stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.DEVNULL)
    output = proc.communicate(password.encode())
    if 'incorrect password' in output[1].decode():
        return 1
    else:
        return 0


class Debugger:
    def debug(self, password : str, error : bytes):
        error = error.decode('utf-8')
        if 'sudo: 1 incorrect password attempt' in error:
            click.echo(click.style('✅ Successful Debugging! ✅ \n', fg='green', bold=True))
            click.echo(click.style(f'Cause: Wrong Password Entered. Code: 001', fg='yellow', bold=True, blink=True))
            return
        elif platform == 'darwin':
            click.echo(click.style('✅ Successful Debugging! ✅ \n', fg='green', bold=True))
            click.echo(click.style(f'Cause: Incompatible Platform. Turbocharge doesn\'t support macOS yet. Code: 005', fg='yellow', bold=True, blink=True))
            return
        elif platform == 'win32':
            click.echo(click.style('✅ Successful Debugging! ✅ \n', fg='green', bold=True))
            click.echo(click.style(f'Cause: Incompatible Platform. Turbocharge doesn\'t support Windows 10/8/7/XP yet. Code: 010', fg='yellow', bold=True, blink=True))
            return
        else:
            click.echo(click.style(':( Failed To Debug... :(', fg='red'))
            return

class Installer:
    def install_task(self, package_name : str, script : str, password : str, test_script : str, tests_passed):
        try:    
            installer_progress = Spinner(message=f'Installing {package_name}...', max=100)
            # sudo requires the flag '-S' in order to take input from stdin
            for _ in range(1, 75):
                time.sleep(0.01)
                installer_progress.next()
            
            proc = Popen(script.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)\
            # Popen only accepts byte-arrays so you must encode the string
            output, error = proc.communicate(password.encode())
            if proc.returncode != 0:
                click.echo(click.style('❎ Installation Failed... ❎', fg='red', blink=True, bold=True))
                debug = click.prompt('Would you like us to debug the failed installation?[y/n]')
                if debug == 'y':
                    debugger = Debugger()
                    debugger.debug(password, error)
                    logs = click.prompt('Would you like to see the logs?[y/n]', type=str)
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
                    logs = click.prompt('Would you like to see the logs?[y/n]', type=str)
                    if logs == 'y':
                        final_output = output.decode('utf-8')
                        if final_output == '':
                            click.echo('There were no logs found...')
                            return
                        else:
                            click.echo(final_output)
                            return
                    return
            click.echo(click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n', fg='green', bold=True))
            # Testing the successful installation of the package
            testing_bar = IncrementalBar('Testing package...', max = 100)
            if tests_passed == [] and test_script == '':
                click.echo('\n')
                click.echo(click.style(f'Test Passed: {package_name} Launch ✅\n', fg='green'))
                return
            for _ in range(1, 21):
                time.sleep(0.002)
                testing_bar.next()
            os.system('cd --')
            for _ in range(21, 60):
                time.sleep(0.002)
                testing_bar.next()
            proc = Popen(test_script.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
            for _ in range(60, 101):
                time.sleep(0.002)
                testing_bar.next()
            click.echo('\n')
            for test in tests_passed:
                click.echo(click.style(f'Test Passed: {test} ✅\n', fg='green'))
            return
        except  subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occurred During Installation...', err = True)

class Uninstaller:
    def uninstall(self, script : str, password : str, package_name : str):
        try:    
            installer_progress = Spinner(message=f'Uninstalling {package_name}...', max=100)
            # sudo requires the flag '-S' in order to take input from stdin
            for _ in range(1, 75):
                time.sleep(0.007)
                installer_progress.next()
            proc = Popen(script.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
            # Popen only accepts byte-arrays so you must encode the string
            proc.communicate(password.encode())
            # stdoutput = (output)[0].decode('utf-8')
            for _ in range(1, 26):
                time.sleep(0.01)
                installer_progress.next()
            click.echo(click.style(f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n', fg='green'))
        except  subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occurred During Installation...', err = True)
    
    def clean(self, password : str):
        try:
            install_progress = Spinner(message='Cleaning Up Packages ')
            for _ in range(1, 75):
                time.sleep(0.007)
                install_progress.next()
            proc = Popen('sudo apt-get -y autoremove'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
            proc.communicate(password.encode())
            for _ in range(1, 26):
                time.sleep(0.007)
                install_progress.next()
            click.echo('\n')
            click.echo(click.style('🎉 Successfully Cleaned Turbocharge! 🎉', fg='green'))
        except  subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occurred During Installation...', err = True) 

class Updater:
    def updatepack(self, package_name: str, password: str):
        try:
            installer_progress = Spinner(
                message=f'Updating {package_name}...', max=100)
            # sudo requires the flag '-S' in order to take input from stdin
            for _ in range(1, 75):
                time.sleep(0.007)
                installer_progress.next()
            proc = Popen(
                f'sudo -S apt-get install --only-upgrade -y {package_name}'.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
            # Popen only accepts byte-arrays so you must encode the string
            proc.communicate(password.encode())
            # stdoutput = (output)[0].decode('utf-8')
            for _ in range(1, 26):
                time.sleep(0.01)
                installer_progress.next()
            click.echo(click.style(
                f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n', fg='green'))
        except CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occurred During Updating..', err=True)

    def updateapp(self, package_name: str, password: str):
        try:
            installer_progress = Spinner(message=f'Updating {package_name}...', max=100)
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
        except CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occurred During Updating..', err=True)

def show_progress(finding_bar):
    for _ in range(1, 2):
        time.sleep(0.01)
        finding_bar.next()
    click.echo('\n')

@click.group()
def cli():
    pass

@cli.command()
def version():
    '''
    Current Turbocharged Version You Have
    '''
    print('Version: 3.0.6 \nDistribution: Stable x86-64')

@cli.command()
@click.argument('package_list', required=True)
def install(package_list):
    '''
    Install A Specified Package(s)
    '''
    password = getpass('Enter your password: ')
    packages = package_list.split(',')
    turbocharge = Installer()
    click.echo('\n')
    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    os_bar.next()
    for package_name in packages:
        package_name = package_name.strip(' ')
        if platform == 'linux':
            click.echo('\n')
            finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)

            if package_name in devpackages:
                show_progress(finding_bar)
                turbocharge.install_task(devpackages[package_name], f'sudo -S apt-get install -y {package_name}', password, f'{package_name} --version', [f'{devpackages[package_name]} Version'])

            if package_name in applications:
                show_progress(finding_bar)
                turbocharge.install_task(applications[package_name], f'sudo -S snap install --classic {package_name}', password, '', [])

            if package_name == 'chrome':
                show_progress(finding_bar)
                try:    
                    click.echo('\n')
                    password = getpass("Enter your password: ")
                    installer_progress = Spinner(message='Installing Chrome...', max=100)
                    # sudo requires the flag '-S' in order to take input from stdin
                    for _ in range(1, 75):
                        time.sleep(0.03)
                        installer_progress.next()
                    click.echo(click.style('\n Chrome Will Take 2 to 4 Minutes To Download... \n', fg='yellow'))
                    proc = Popen("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    proc.wait()
                    second = Popen("sudo -S apt-get install -y ./google-chrome-stable_current_amd64.deb".split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # Popen only accepts byte-arrays so you must encode the string
                    second.communicate(password.encode())
                    
                    # stdoutput = (output)[0].decode('utf-8') 
                    click.echo(click.style('\n\n 🎉 Successfully Installed Chrome! 🎉 \n'))             
                    # Testing the successful installation of the package
                    testing_bar = IncrementalBar('Testing package...', max = 100)
                    for _ in range(1, 21):
                        time.sleep(0.045)
                        testing_bar.next()
                    os.system('cd --')
                    for _ in range(21, 60):
                        time.sleep(0.045)
                        testing_bar.next()
                    for _ in range(60, 101):
                        time.sleep(0.03)
                        testing_bar.next()
                    click.echo('\n')
                    click.echo(click.style('Test Passed: Chrome Launch ✅\n', fg='green'))
                except  subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo('An Error Occurred During Installation...', err = True)
       
            if package_name == 'anaconda':
                show_progress(finding_bar)
                username = getuser()
                try:    
                    installer_progress = Spinner(message=f'Installing {package_name}...', max=100)
                    # sudo requires the flag '-S' in order to take input from stdin
                    for _ in range(1, 35):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system("wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh")
                    for _ in range(35, 61):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system('bash ~/anaconda.sh -b -p $HOME/anaconda3')
                    for _ in range(61, 91):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(f'echo "export PATH="/home/{username}/anaconda3/bin:$PATH"" >> ~/.bashrc')
                    # Popen only accepts byte-arrays so you must encode the string
                    proc.communicate(password.encode())
                    for _ in range(90, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
                except  subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo('An Error Occurred During Installation...', err = True)

            if package_name == 'miniconda':
                show_progress(finding_bar)
                username = getuser()
                try:    
                    installer_progress = Spinner(message=f'Installing {package_name}...', max=100)
                    # sudo requires the flag '-S' in order to take input from stdin
                    for _ in range(1, 35):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system("wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/miniconda.sh")
                    for _ in range(35, 61):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system('bash ~/anaconda.sh -b -p $HOME/anaconda3')
                    for _ in range(61, 91):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(f'echo "export PATH="/home/{username}/anaconda3/bin:$PATH"" >> ~/.bashrc')
                    for _ in range(90, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
                except  subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo('An Error Occurred During Installation...', err = True)

            elif package_name not in devpackages and package_name not in applications and package_name != 'chrome' and package_name != 'anaconda' and package_name != 'miniconda':
                click.echo('\n')
                click.echo(click.style(':( Package Not Found! :(', fg='red'))


@cli.command()
@click.argument('package_list', required=True)
def remove(package_list):
    '''
    Uninstall Applications And Packages
    '''
    uninstaller = Uninstaller()
    password = getpass('Enter your password: ')
    packages = package_list.split(',')
    for package in packages:
        if package in devpackages:
            uninstaller.uninstall(f'sudo -S apt-get remove -y {package}', password, package_name=devpackages[package])
        
        if package in applications:        
            uninstaller.uninstall(f'sudo snap remove {package}', password, package_name=applications[package])
        
        if package == 'anaconda':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling Anaconda...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()
                os.system('rm -rf ~/anaconda3 ~/.continuum ~/.conda')
                os.system('rm ~/anaconda.sh')
                with open('.bashrc', 'r') as file:
                    lines = file.read()

                with open('.bashrc', 'w') as file:
                    for line in lines:
                        if 'anaconda' in line or 'miniconda' in line:
                            return
                        else:
                            file.write(line)

                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(75, 101):
                    time.sleep(0.01)
                    installer_progress.next()
                click.echo(click.style(
                    f'\n\n 🎉 Successfully Uninstalled Anaconda! 🎉 \n', fg='green'))
            except CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Uninstallation...', err=True)

        if package == 'miniconda':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling Miniconda...', max=100)
                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()
                os.system('rm -rf ~/miniconda ~/.continuum ~/.conda ~/.condarc')
                os.system('rm ~/miniconda.sh')
                with open('.bashrc', 'r') as file:
                    lines = file.read()

                with open('.bashrc', 'w') as file:
                    for line in lines:
                        if 'anaconda' in line or 'miniconda' in line:
                            return
                        else:
                            file.write(line)
                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(1, 101):
                    time.sleep(0.01)
                    installer_progress.next()
                click.echo(click.style(
                    f'\n\n 🎉 Successfully Uninstalled Miniconda! 🎉 \n', fg='green'))
            except CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Uninstallation...', err=True)

                
@cli.command()
@click.argument('package_list', required=True)
def update(package_list):
    '''
    Updates Applications And Packages
    '''
    updater = Updater()
    password = getpass('Enter your password: ')
    packages = package_list.split(',')
    for package in packages:
        if package in devpackages:
            updater.updatepack(package, password)

        if package in applications:
            updater.updateapp(package, password)

        else:
            return

# Need To Install Large Packs Of Packages Example : Graphics Pack Installs Blender And Other Software
@cli.command()
@click.argument('hyperpack_list', required=True)
def hyperpack(hyperpack_list):
    '''
    Install Large Packs Of Applications And Packages
    '''   
    password = getpass('Enter your password: ')
    click.echo('\n')
    password_bar = IncrementalBar('Verifying Password...', max = 1)
    exitcode = is_password_valid(password)
    if exitcode == 1:
        click.echo('Wrong Password Entered... Aborting Installation!')
        return
    password_bar.next()
    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    os_bar.next()
    if platform == 'linux':
        turbocharge = Installer()
        updater = Updater()
        cleaner = Uninstaller()
        click.echo('\n')
        hyperpacks = hyperpack_list.split(',')
        for hyperpack in hyperpacks:
            hyper_pack = hyperpkgs[hyperpack]
            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            # Installing Required Packages
            for package in packages:
                turbocharge.install_task(devpackages[package], f'sudo -S apt-get install -y {package}', password, f'{package} --version', [f'{devpackages[package]} Version'])
                
            # Installing Required Applications    
            for app in apps:
                turbocharge.install_task(applications[app], f'sudo -S snap install --classic {app}', password, '', [])
            
            # Updating Required Packages
            for package in packages:
                updater.updatepack(package, password)
            
            for app in apps:
                updater.updateapp(app, password)
                
            cleaner.clean(password)

@cli.command()
def clean():
    '''
    Remove Junk Packages Which Are Not Needed
    '''
    uninstaller = Uninstaller()

    password = getpass('Enter your password: ')
    uninstaller.clean(password)


@cli.command()
def list():
    '''
    Applications And Packages TurboCharge Supports
    '''
    click.echo(click.style(
        '''
__________________________________________
| Applications      |Duration||   Size   |
------------------------------------------
| android-studio    |   5m   || 840.0 MB |
| atom              |   2m   || 224.8 MB |
| blender           |   2m   || 187.7 MB |
| brackets          |   1m   || 109.6 MB |
| clion             |   3m   || 502.0 MB |
| chrome            |   2m   || 70.2  MB |
| datagrip          |   2m   || 356.8 MB |
| discord           |   1m   || 60.1  MB |
| eclipse           |   2m   || 220.3 MB |
| figma-linux       |   2m   || 96.4  MB |
| libreoffice       |   1m   || 25.0  MB |
| librepcb          |   1m   || 98.8  MB |
| opera             |   1m   || 64.2 MB  |
| pycharm           |   3m   || 372.1 MB |
| powershell        |   1m   || 62.5  MB |
| rubymine          |   3m   || 363.2 MB |
| sublime-text      |   1m   || 70.8 MB  |
| webstorm          |   3m   || 343.8 MB |
| vscode            |   2m   || 162.5 MB |
| vscode-insiders   |   2m   || 153.3 MB |
------------------------------------------
________________
| Package      |
----------------    
|  anaconda    |
|  curl        |
|  docker      |
|  emacs       |
|  git         |
|  golang      |
|  htop        |
|  jq          |
|  kotlin      |
|  miniconda   |
|  ncdu        |
|  neovim      |
|  npm         |
|  patchelf    |
|  rust        |
|  sqlite      |
|  taskwarrior |
|  tldr        |
|  tmux        |
|  vim         |
|  zsh         |
|  zlib        |
----------------        
        ''',
        fg='white',
    ),
)
=======
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
from constants import applications_windows, devpackages_windows, applications_linux, devpackages_linux, apt_script, apt_remove, snap_script, snap_remove, display_list_linux, display_list_windows, display_list_macos, hyperpkgs, devpackages_macos, applications_macos
from miscellaneous import show_progress, is_password_valid
from HyperPack import HyperPack
from Debugger import Debugger
from Install import Installer
from Uninstall import Uninstaller
from Update import Updater
from Setup import Setup


@click.group()
def cli():
    pass

@cli.command()
def version():
    '''
    Current Turbocharged Version You Have
    '''
    click.echo(f'Version: 3.0.6 \nDistribution: {platform} Stable x86-64')

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
                    f'{constant.apt_script} {package_name}',
                    password,
                    f'{package_name} --version',
                    [f'{devpackages_linux[package_name]} Version'])

            if package_name in applications_linux:
                show_progress(finding_bar)
                turbocharge.install_task(
                    applications_linux[package_name],
                    f'{constant.snap_script} {package_name}',
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
        

        if platform == 'win32':
            click.echo('\n')
            finding_bar = IncrementalBar('Finding Requested Packages...', max=1)

            if package_name in devpackages_windows:
                show_progress(finding_bar)

                turbocharge.install_task(
                    package_name=devpackages_windows[package_name],
                    script=f"choco install {package_name} -y",
                    password="",
                    test_script=f"{package_name} --version",
                    tests_passed=[f'{devpackages_windows[package_name]} Version']
                )


            elif package_name in applications_windows:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=applications_windows[package_name],
                    script=f"choco install {package_name} -y",
                    password="",
                    test_script="",
                    tests_passed=[]
                )

            elif package_name not in devpackages_windows and package_name not in applications_windows:
                click.echo('\n')
                click.echo(click.style(':( Package Not Found! :(', fg='red'))
        
        if platform == 'darwin':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_windows:
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

            elif package_name in applications_windows:
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
                click.echo(click.style(':( Package Not Found! :(', fg='red'))

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
                    click.echo('An Error Occurred During Uninstallation...', err=True)

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
            print(arr[i%slen], end='\r')
    
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
>>>>>>> 417cd1d... Added Search With Python And Google Chrome

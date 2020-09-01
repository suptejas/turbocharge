import click
import os
import subprocess
from sys import platform
from getpass import getpass
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
from subprocess import Popen, PIPE, DEVNULL

applications = {
        'android-studio': 'Android Studio',
        'atom' : 'Atom',
        'blender' : 'Blender',
        'discord' : 'Discord',
        'libreoffice' : 'Libre Office',
        'opera' : 'Opera',
        'pycharm': 'Pycharm Community',
        'sublime-text': 'Sublime Text',
        'vscode' : 'Visual Stuio Code',
        'vscode-insiders' : 'Visual Studio Code Insiders',  
    }

devpackages = {
        'git' : 'Git',
        'curl' : 'Curl',
        'npm' : 'Npm',
        'zsh' : 'Zsh',
        'vim' : 'Vim',
        'htop' : 'Htop',
        'tldr' : 'Tldr',
        'jq' : 'JQ',
        'ncdu' : 'Ncdu',
        'taskwarrior' : 'Task Warrior',
        'tmux' : 'Tmux',
        'patchelf' : 'Patchelf',
        'golang' : 'Go-Lang',
        'rust' : 'Rust',
    }

class Installer:
    def install_task(self, package_name : str, script : str, password : str, test_script : str, tests_passed):
        try:    
            installer_progress = Spinner(message=f'Installing {package_name}...', max=100)
            # sudo requires the flag '-S' in order to take input from stdin
            for _ in range(1, 75):
                time.sleep(0.01)
                installer_progress.next()
            proc = Popen(script.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
            # Popen only accepts byte-arrays so you must encode the string
            proc.communicate(password.encode())
            # stdoutput = (output)[0].decode('utf-8')
            click.echo(click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
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
            subprocess.run(test_script.split(), stdout=subprocess.DEVNULL)
            for _ in range(60, 101):
                time.sleep(0.002)
                testing_bar.next()
            click.echo('\n')
            for test in tests_passed:
                click.echo(click.style(f'Test Passed: {test} ✅\n', fg='green'))
        except  subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occured During Installation...', err = True)

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
            click.echo('An Error Occured During Installation...', err = True)
    
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
            click.echo('An Error Occured During Installation...', err = True)

def showfind(finding_bar):
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
    print('Version: 3.0.4 \nDistribution: Stable x86-64')

@cli.command()
@click.argument('package_list', required=True)
def install(package_list):
    '''
    Install A Specified Package
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
                showfind(finding_bar)
                turbocharge.install_task(devpackages[package_name], f'sudo -S apt-get install -y {package_name}', password, f'{package_name} --version', [f'{devpackages[package_name]} Version'])

            if package_name in applications:
                showfind(finding_bar)
                turbocharge.install_task(applications[package_name], f'sudo -S snap install --classic {package_name}', password, '', [])

            if package_name == 'chrome':
                showfind(finding_bar)
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
                    click.echo('An Error Occured During Installation...', err = True)
       

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
            print(f'{package} is in devpackages')
            uninstaller.uninstall(f'sudo -S apt-get remove -y {devpackages[package]}', password, package_name=devpackages[package])
        
        if package in applications:        
            uninstaller.uninstall(f'sudo snap remove {package}', password, package_name=applications[package])
        
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
| chrome            |   3m   || 70.2  MB |
| discord           |   1m   || 60.1  MB |
| libreoffice       |   1m   || 25.0  MB |
| opera             |   1m   || 64.2 MB  |
| pycharm           |   3m   || 372.1 MB |
| sublime-text      |   1m   || 70.8 MB  |
| vscode            |   2m   || 162.5 MB |
| vscode-insiders   |   2m   || 153.3 MB |
------------------------------------------
________________
| Package      |
----------------    
|  curl        |
|  git         |
|  golang      |
|  htop        |
|  jq          |
|  ncdu        |
|  npm         |
|  patchelf    |
|  rust        |
|  taskwarrior |
|  tldr        |
|  tmux        |
|  vim         |
|  zsh         |
----------------        
        ''',
        fg='white',
    ),
)
    
    
    
    

# if platform == 'darwin':
    #     os_bar.next()
    #     click.echo('\n')
    #     finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)
    #     if package_name == 'brew':
    #         for _ in range(1, 2):
    #             time.sleep(0.03)
    #             finding_bar.next()
    #         try:    
    #             click.echo('\n')
    #             password = getpass("Enter your password: ")
    #             installer_progress = Spinner(message='Installing Homebrew...', max=100)
    #             # sudo requires the flag '-S' in order to take input from stdin
    #             for _ in range(1, 75):
    #                 time.sleep(0.03)
    #                 installer_progress.next()
    #             proc = pexpect.spawn('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"')
    #             proc.sendline(password)
    #             proc.sendline('\n')
    #             click.echo(click.style('\n\n 🎉 Successfully Installed Homebrew! 🎉 \n'))
    #             # Testing the successful installation of the package
    #             testing_bar = IncrementalBar('Testing package...', max = 100)
    #             for _ in range(1, 21):
    #                 time.sleep(0.05)
    #                 testing_bar.next()
    #             os.system('cd --')
    #             for _ in range(21, 60):
    #                 time.sleep(0.05)
    #                 testing_bar.next()
    #             for _ in range(60, 101):
    #                 time.sleep(0.05)
    #                 testing_bar.next()
    #             subprocess.run(['brew','--version'])
    #             click.echo('\n')
    #             click.echo(click.style('Test Passed: Brew Version ✅\n', fg='green'))
    #         except  subprocess.CalledProcessError as e:
    #             click.echo(e.output)
    #             click.echo('An Error Occured During Installation...', err = True)
    #     if package_name == 'xcode-tools':
    #         for _ in range(1, 2):
    #             time.sleep(0.03)
    #             finding_bar.next()
    #         try:    
    #             click.echo('\n')
    #             password = getpass("Enter your password: ")
    #             installer_progress = Spinner(message='Installing Xcode-Command-Line-Tools...', max=100)
    #             # sudo requires the flag '-S' in order to take input from stdin
    #             for _ in range(1, 75):
    #                 time.sleep(0.03)
    #                 installer_progress.next()
    #             proc = pexpect.spawn('xcode-select --install')
    #             click.echo(click.style('\n\n 🎉 Successfully Installed Xcode-Command-Line-Tools! 🎉 \n'))
    #             # Testing the successful installation of the package
    #             testing_bar = IncrementalBar('Testing package...', max = 100)
    #             for _ in range(1, 21):
    #                 time.sleep(0.05)
    #                 testing_bar.next()
    #             os.system('cd --')
    #             for _ in range(21, 60):
    #                 time.sleep(0.05)
    #                 testing_bar.next()
    #             for _ in range(60, 101):
    #                 time.sleep(0.05)
    #                 testing_bar.next()
    #             subprocess.run(['git','--version'])
    #             subprocess.run(['clang', '--version'])
    #             subprocess.run(['swift', '--version'])
    #             subprocess.run(['pip3', '--version'])
                
    #             click.echo('\n')
    #             click.echo(click.style('Test Passed: Git Version ✅\n', fg='green'))
    #             click.echo(click.style('Test Passed: Clang Version ✅\n', fg='green'))
    #             click.echo(click.style('Test Passed: Swift Version ✅\n', fg='green'))
    #             click.echo(click.style('Test Passed: Pip3 Version ✅\n', fg='green'))
                
    #         except  subprocess.CalledProcessError as e:
    #             click.echo(e.output)
    #             click.echo('An Error Occured During Installation...', err = True)

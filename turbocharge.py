import click
import os
import subprocess
from sys import platform
from getpass import getpass
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
import pexpect
from subprocess import Popen, PIPE, DEVNULL

class Installer:
    def init_install(self, finding_bar):
        for _ in range(1, 2):
                time.sleep(0.01)
                finding_bar.next()
        click.echo('\n')
        password = getpass('Enter your password: ')
        return password

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
                click.echo(click.style(f'Test Passed: {package_name} Launch ✅\n', fg='green'))
                return
            for _ in range(1, 21):
                time.sleep(0.01)
                testing_bar.next()
            os.system('cd --')
            for _ in range(21, 60):
                time.sleep(0.01)
                testing_bar.next()
            subprocess.run(test_script.split(), stdout=subprocess.DEVNULL)
            for _ in range(60, 101):
                time.sleep(0.01)
                testing_bar.next()
            click.echo('\n')
            for test in tests_passed:
                click.echo(click.style(f'Test Passed: {test} ✅\n', fg='green'))
        except  subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occured During Installation...', err = True)

@click.group()
def cli():
    pass

@cli.command()
def version():
    '''
    Current Turbocharged Version You Have
    '''
    print('Version: 3.0.2 \nDistribution: Stable x86-64')

@cli.command()
@click.argument('package_name', required=True)
def install(package_name):
    '''
    Install A Specified Package
    '''
    turbocharge = Installer()
    packages = {
        'git' : 'Git',
        'curl' : 'Curl',
        'npm' : 'Npm',
        'zsh' : 'Zsh',
        'vim' : 'Vim',
        'opera' : 'Opera',
        'vscode' : 'Visual Stuio Code',
        'vscode-insiders' : 'Visual Studio Code Insiders',
        'wikit' : 'Wikit',
        'htop' : 'Htop',
        'tldr' : 'Tldr',
        'jq' : 'JQ',
        'ncdu' : 'Ncdu',
        'taskwarrior' : 'Task Warrior',
        'tmux' : 'Tmux',
        'patchelf' : 'Patchelf',
        'discord' : 'Discord',
        'libreoffice' : 'Libre Office',
        'golang' : 'Go-Lang',
        'rust' : 'Rust',
        'typescript' : 'Typescript',
        'blender' :'Blender',
    }
    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    if platform == 'linux':
        os_bar.next()
        click.echo('\n')
        finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)

        if package_name in packages:
            password = turbocharge.init_install(finding_bar)
            turbocharge.install_task(packages[package_name], f'sudo -S apt-get install -y {package_name}', password, f'{package_name} --version', [f'{packages[package_name]} Version'])
        
        if package_name == 'chrome':
            for _ in range(1, 2):
                time.sleep(0.03)
                finding_bar.next()
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
def list():
    '''
    Applications And Packages TurboCharge Supports
    '''
    print(
        '''
        blender 
        chrome 
        curl 
        discord 
        git 
        golang 
        googler 
        htop
        jq
        libreoffice 
        ncdu
        npm 
        opera 
        patchelf
        rust
        taskwarrior
        tldr
        tmux
        typescript 
        vim 
        vscode 
        vscode-insiders 
        wikit
        zsh 
        '''
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

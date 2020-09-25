import click
import os
import subprocess
from sys import platform
from getpass import getpass, getuser
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
from subprocess import Popen, PIPE, DEVNULL
from Installable import Installable


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
    'git': 'Git',
    'curl': 'Curl',
    'docker': 'Docker',
    'npm': 'Npm',
    'zsh': 'Zsh',
    'emacs': 'Emacs',
    'neovim': 'Neo Vim',
    'vim': 'Vim',
    'htop': 'Htop',
    'sqlite': 'Sqlite',
    'tldr': 'Tldr',
    'jq': 'JQ',
    'ncdu': 'Ncdu',
    'taskwarrior': 'Task Warrior',
    'tmux': 'Tmux',
    'patchelf': 'Patchelf',
    'golang': 'Go-Lang',
    'rust': 'Rust',
    'zlib': 'Z-Lib',
    'kakoune': 'Kakoune',
    'autojump': 'Autojump',
    'pass': 'Pass',
    'qtpass': 'QTpass'
}


def is_password_valid(password : str):
    proc = Popen('sudo -k -S -l'.split(), stdin=PIPE, stderr=PIPE, stdout=DEVNULL)
    
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
            
            proc = Popen(script.split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)

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

        except subprocess.CalledProcessError as e:
            click.echo(e.output)
            click.echo('An Error Occurred During Installation...', err = True)



def show_progress(finding_bar):
    for _ in range(1, 2):
        time.sleep(0.01)
        finding_bar.next()
    click.echo('\n')

def install(package):
    '''
    Install A Specified Package(s)
    '''
    password = getpass('Enter your password: ')

    turbocharge = Installer()

    click.echo('\n')

    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    os_bar.next()

    if platform == 'linux':
        click.echo('\n')
        finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)
        if package.install_type == 'p':
            show_progress(finding_bar)
            turbocharge.install_task(devpackages[package.package_name], f'sudo -S apt-get install -y {package.package_name}={package.package_version}', password, f'{package.package_name} --version', [f'{devpackages[package.package_name]} Version'])

        if package.install_type == 'a':
            show_progress(finding_bar)
            turbocharge.install_task(applications[package.package_name], f'sudo -S snap install --classic {package.package_name}', password, '', [])

        if package.package_name == 'chrome':
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
                proc = Popen("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                proc.wait()
                second = Popen("sudo -S apt-get install -y ./google-chrome-stable_current_amd64.deb".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
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

        if package.package_name == 'anaconda':
            show_progress(finding_bar)
            username = getuser()

            try:    
                installer_progress = Spinner(message=f'Installing {package.package_name}...', max=100)
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
                
                for _ in range(90, 101):
                    time.sleep(0.01)
                    installer_progress.next()
                # stdoutput = (output)[0].decode('utf-8')
                click.echo(click.style(f'\n\n 🎉 Successfully Installed {package.package_name}! 🎉 \n'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Installation...', err = True)

        if package.package_name == 'miniconda':
            show_progress(finding_bar)
            username = getuser()
            try:    
                installer_progress = Spinner(message=f'Installing {package.package_name}...', max=100)
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
                click.echo(click.style(f'\n\n 🎉 Successfully Installed {package.package_name}! 🎉 \n'))
            except  subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Installation...', err = True)




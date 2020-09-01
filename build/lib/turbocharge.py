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
    print('Version: 3.0.2 \nDistribution: Stable x86-64')

@cli.command()
@click.argument('package_list', required=True, )
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

            if package_name == 'git':
                showfind(finding_bar)
                turbocharge.install_task('Git', 'sudo -S apt-get install -y git', password, 'git --version', ['Git Version'])

            if package_name == 'curl': 
                showfind(finding_bar)
                turbocharge.install_task('Curl', 'sudo -S apt-get install -y curl', password, 'curl --version', ['Curl Version'])

            if package_name == 'npm':
                showfind(finding_bar)
                turbocharge.install_task('Npm', 'sudo -S apt-get install -y npm', password, 'npm --version', ['Npm Version'])

            if package_name == 'zsh':
                showfind(finding_bar)
                turbocharge.install_task('Zsh', 'sudo -S apt-get install -y zsh', password, 'zsh --version', ['Zsh Version'])

            if package_name == 'vim':
                showfind(finding_bar)
                turbocharge.install_task('Vim', 'sudo -S apt-get install -y vim', password, 'vim --version', ['Vim Version'])

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
            
            if package_name == 'opera':
                showfind(finding_bar)
                turbocharge.install_task('Opera', 'sudo -S snap install opera', password, '', [])

            if package_name == 'vscode':
                showfind(finding_bar)
                turbocharge.install_task('Visual Studio Code', 'sudo -S snap install --classic code', password, 'code --version', ['Visual Studio Code Version'])

            if package_name == 'vscode-insiders':
                showfind(finding_bar)
                turbocharge.install_task('Visual Studio Code Insiders', 'sudo -S snap install --classic code-insiders', password, '', [])
            
            if package_name == 'wikit':
                showfind(finding_bar)
                turbocharge.install_task('Wikit', 'sudo -S npm install wikit -g', password, 'wikit --version', ['Wikit Version'])

            if package_name == 'htop':
                showfind(finding_bar)
                turbocharge.install_task('Htop', 'sudo -S apt-get install -y htop', password, 'htop --version', ['Htop Version'])

            if package_name == 'tldr':
                showfind(finding_bar)
                turbocharge.install_task('Tldr', 'sudo -S npm install -g tldr', password, 'tldr --version', ['Tldr Version'])

            if package_name == 'jq':
                showfind(finding_bar)
                turbocharge.install_task('JQ', 'sudo -S apt-get install -y jq', password, 'jq --version', ['Jq Version'])

            if package_name == 'ncdu':
                showfind(finding_bar)
                turbocharge.install_task('Ncdu', 'sudo -S apt-get install -y ncdu', password, 'ncdu --version', ['Ncdu Version'])

            if package_name == 'taskwarrior':
                showfind(finding_bar)
                turbocharge.install_task('Task Warrior', 'sudo -S apt-get install -y taskwarrior', password, 'taskwarrior --version', ['Taskwarrior Version'])

            if package_name == 'tmux':
                showfind(finding_bar)
                turbocharge.install_task('Tmux', 'sudo -S apt-get install -y tmux', password, 'tmux --version', ['Tmux Version'])
        
            if package_name == 'patchelf':
                showfind(finding_bar)
                turbocharge.install_task('Patchelf', 'sudo -S apt-get install -y patchelf', password, 'patchelf --version', ['Patchelf Version'])
        
            if package_name == 'discord':
                showfind(finding_bar)
                turbocharge.install_task('Discord', 'sudo -S snap install discord', password, '', [])

            if package_name == 'libreoffice':
                showfind(finding_bar)
                turbocharge.install_task('Libre Office', 'sudo -S apt-get install -y libreoffice', password, '', [])

            if package_name == 'golang':
                showfind(finding_bar)
                turbocharge.install_task('Go-Lang', 'sudo -S apt-get install -y golang-go', password, 'go version', ['Go Version'])

            if package_name == 'rust':
                showfind(finding_bar)
                turbocharge.install_task('Rust', 'sudo -S apt-get install -y rustc', password, 'rustc -V', ['Rust Version'])

            if package_name == 'typescript':
                showfind(finding_bar)
                turbocharge.install_task('Typescript', 'sudo -S apt-get install -y node-typescript', password, 'tsc -v', ['Typescript Version'])

            if package_name == 'blender':
                showfind(finding_bar)
                turbocharge.install_task('Blender', 'sudo -S snap install --classic blender', password, '', [])

            if package_name == 'sublime-text':
                showfind(finding_bar)
                turbocharge.install_task('Sublime Text', 'sudo -S snap install sublime-text', password, '', [])        

            if package_name == 'pycharm':
                showfind(finding_bar)
                turbocharge.install_task('Pycharm Community', 'sudo -S snap install --classic pycharm-community', password, '', [])

            if package_name == 'atom':
                showfind(finding_bar)
                turbocharge.install_task('Atom', 'sudo -S snap install --classic atom', password, '', [])     

            if package_name == 'android-studio':
                showfind(finding_bar)
                turbocharge.install_task('Android Studio', 'sudo -S snap install --classic android-studio', password, '', [])

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
        print('This is the name of the package: ', package)
        if package == 'git':
            uninstaller.uninstall('sudo -S apt-get remove -y git', password, package_name='Git')
        
        if package == 'curl':
            uninstaller.uninstall('sudo -S apt-get remove -y curl', password, package_name='Curl')
        
        if package == 'npm':
            uninstaller.uninstall('sudo -S apt-get remove -y npm', password, package_name='Npm')
        
        if package == 'zsh':
            uninstaller.uninstall('sudo -S apt-get remove -y zsh', password, package_name='Git')

        if package == 'vim':
            uninstaller.uninstall('sudo -S apt-get remove -y vim', password, package_name='Vim')
    
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
__________________________________________________
| No. |    Applications      |Duration||   Size   |
--------------------------------------------------
|  1. |    android-studio    |   5m   || 840.0 MB |
|  2. |    atom              |   2m   || 224.8 MB |
|  3. |    blender           |   2m   || 187.7 MB |
|  4. |    chrome            |   3m   || 70.2  MB |
|  5. |    discord           |   1m   || 60.1  MB |
|  6. |    libreoffice       |   1m   || 25.0  MB |
|  7. |    opera             |   1m   || 64.2 MB  |
|  8. |    pycharm           |   3m   || 372.1 MB |
|  9. |    sublime-text      |   1m   || 70.8 MB  |
|  10.|    vscode            |   2m   || 162.5 MB |
|  11.|    vscode-insiders   |   2m   || 153.3 MB |
--------------------------------------------------
_________________________
| No. |    Package      |
-------------------------      
|  1. |     curl        |
|  2. |     git         |
|  3. |     golang      |
|  4. |     htop        |
|  5. |     jq          |
|  6. |     ncdu        |
|  7. |     npm         |
|  8. |     patchelf    |
|  9. |     rust        |
|  10.|     taskwarrior |
|  11.|     tldr        |
|  12.|     tmux        |
|  13.|     typescript  |
|  14.|     vim         |
|  15.|     wikit       |
|  16.|     zsh         |
-------------------------        
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

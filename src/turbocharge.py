import click
import os
import subprocess
from sys import platform, stderr
from getpass import getpass, getuser
from progress.spinner import Spinner
from progress.bar import IncrementalBar
import time
from subprocess import Popen, PIPE, DEVNULL, run

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


class HyperPack:
    def __init__(self, packages, applications):
        self.packages = packages
        self.applications = applications


hyperpkgs = {
    'essential' : HyperPack('git,curl,npm,zsh,vim', 'code,atom,sublime-text'),
    'office' : HyperPack('sqlite', 'libreoffice')
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
        if platform == 'linux':
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

                

                for _ in range(60, 81):
                    time.sleep(0.002)
                    testing_bar.next()

                os.system('cd ~')

                def subprocess_cmd(command):
                    process = subprocess.Popen(command,stdout=subprocess.PIPE, stdin=PIPE, stderr=PIPE)
                    proc_stdout = process.communicate()[0].strip()
                    decoded = proc_stdout.decode("utf-8")
                    version_tag = decoded.split("\n")[1]
                    cleaned_version = version_tag.split(": ")[1] # using [1:] might be useful in some scenario where the version has multiple colons in it.
                    return cleaned_version

                package_type = None
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'

                def get_key(val):
                    for key, value in devpackages.items():
                        if val == value:
                            return key
                    
                    return 'Key doesn\'t exist'
                    
                package_version = subprocess_cmd(f'apt show {get_key(package_name)}'.split())
                os.system('cd ~')

                with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                line_exists = False

                for line in lines:
                    if get_key(package_name) in line:
                        line_exists = True

                with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                    if line_exists == False:
                        file.write(f'{get_key(package_name)} {package_version} {package_type} \n')

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
                

        elif platform == 'win32':
            try:
                installer_progress = Spinner(message=f'Installing {package_name}...', max=100)
                
                for _ in range(1, 75):
                    time.sleep(0.01)
                    installer_progress.next()

                run(script, stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()

                # Haven't implemented debug because .run() doesn't offer communicate() function

                click.echo(click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n', fg='green', bold=True))

                testing_bar = IncrementalBar('Testing package...', max = 100)
            
                if tests_passed == [] and test_script == '':
                    click.echo('\n')
                    click.echo(click.style(f'Test Passed: {package_name} Launch ✅\n', fg='green'))

                    return
                
                for _ in range(1, 64):
                    time.sleep(0.002)
                    testing_bar.next()
                
                run(test_script, stdout=PIPE, stderr=PIPE)

                for _ in range(1, 36):
                    time.sleep(0.002)
                    testing_bar.next()
                
                click.echo('\n')

                for test in tests_passed:
                    click.echo(click.style(f'Test Passed: {test} ✅\n', fg='green'))

                return
            
            except Exception as e:
                click.echo(e)
                click.echo('An Error Occured During Installation...', err = True)



class Uninstaller:
    def uninstall(self, script : str, password : str, package_name : str):
        if platform == 'linux':
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
                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(click.style(f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n', fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        

        elif platform == 'win32':
            try:
                installer_progress = Spinner(message=f'Uninstalling {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()
                
                run(script, stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                click.echo(click.style(f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n', fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)


    def clean(self, password : str):
        if platform == 'linux':
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
            
            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err = True)
        
        elif platform == 'win32':
            pass # chocolatey auto removes files


class Updater:
    def updatepack(self, package_name: str, password: str):
        if platform == 'linux':
            try:
                installer_progress = Spinner(message=f'Updating {package_name}...', max=100)
                
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

                def subprocess_cmd(command):
                    process = subprocess.Popen(command,stdout=PIPE, stdin=PIPE, stderr=PIPE)
                    proc_stdout = process.communicate()[0].strip()
                    decoded = proc_stdout.decode("utf-8")
                    version_tag = decoded.split("\n")[1]
                    cleaned_version = version_tag.split(": ")[1] # using [1:] might be useful in some scenario where the version has multiple colons in it.
                    return cleaned_version

                package_type = 'p'
                
                package_version = subprocess_cmd(f'apt show {package_name}'.split())
                os.system('cd ~')

                with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                line_exists = False

                for line in lines:
                    if package_name in line:
                        line_exists = True

                with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                    if line_exists == False:
                        file.write(f'{package_name} {package_version} {package_type} \n')

                for _ in range(1, 26):
                    time.sleep(0.01)
                    installer_progress.next()
                
                click.echo(click.style(f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n', fg='green'))
            
            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)
        
        elif platform == 'win32':
            try:
                installer_progress = Spinner(message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()
                
                run(f'choco upgrade {package_name} -y', stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()
                
                click.echo(click.style(f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n', fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)


    def updateapp(self, package_name: str, password: str):
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
            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating...', err=True)
        
        elif platform == 'win32':
            try:
                installer_progress = Spinner(message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()
                
                run(f'choco upgrade {package_name} -y', stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()
                
                click.echo(click.style(f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n', fg='green'))

            except subprocess.CalledProcessError as e:
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
        

        elif platform == 'win32':
            click.echo('\n')
            finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)

            if package_name in devpackages:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=devpackages[package_name],
                    script=f"choco install {package_name} -y",
                    password="",
                    test_script=f"{package_name} --version",
                    tests_passed=[f'{devpackages[package_name]} Version']
                )

            elif package_name in applications:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=applications[package_name],
                    script=f"choco install {package_name} -y",
                    password="",
                    test_script="",
                    tests_passed=[]
                )
            
            elif package_name not in devpackages and package_name not in applications:
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
        if platform == 'linux':
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
                except subprocess.CalledProcessError as e:
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
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo('An Error Occurred During Uninstallation...', err=True)
        
        elif platform == 'win32':
            if package in devpackages:
                uninstaller.uninstall(
                    f'choco uninstall {package} -y',
                    password="",
                    package_name=devpackages[package]
                )
            
            elif package in applications:
                uninstaller.uninstall(
                    f'choco uninstall {package}',
                    password="",
                    package_name=applications[package]
                )

                
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
        if platform == "linux":
            if package in devpackages:
                updater.updatepack(package, password)

            if package in applications:
                updater.updateapp(package, password)

            else: return
        
        elif platform == "win32":
            if package in devpackages:
                updater.updatepack(package, "")
            
            if package in applications:
                updater.updateapp(package, "")
            
            else: return


# Need To Install Large Packs Of Packages Example : Graphics Pack Installs Blender And Other Software
@cli.command()
@click.argument('hyperpack_list', required=True)
def hyperpack(hyperpack_list):
    '''
    Install Large Packs Of Applications And Packages
    '''
    os_bar = IncrementalBar('Getting Operating System...', max = 1)
    os_bar.next()

    installer = Installer()
    updater = Updater()
    cleaner = Uninstaller()

    hyperpacks = hyperpack_list.split(',')
    
    if platform == 'linux':
        password = getpass('Enter your password: ')
        click.echo('\n')

        password_bar = IncrementalBar('Verifying Password...', max = 1)

        exitcode = is_password_valid(password)

        if exitcode == 1:
            click.echo('Wrong Password Entered... Aborting Installation!')
            return

        password_bar.next()

        click.echo('\n')

        for hyperpack in hyperpacks:
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            # Installing Required Packages
            for package in packages:
                installer.install_task(devpackages[package], f'sudo -S apt-get install -y {package}', password, f'{package} --version', [f'{devpackages[package]} Version'])

            # Installing Required Applications    
            for app in apps:
                installer.install_task(applications[app], f'sudo -S snap install --classic {app}', password, '', [])

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
                    package_name=devpackages[package],
                    script=f'choco install {package} -y',
                    password="",
                    test_script=f'{package} --version',
                    tests_passed=[f'{devpackages[package]} Version']
                )

            for package in packages:
                updater.updatepack(package, password="")
            
            for app in apps:
                installer.install_task(
                    package_name=applications[app],
                    script=f'choco install {app} -y',
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
|  autojump    |
|  curl        |
|  docker      |
|  emacs       |
|  git         |
|  golang      |
|  htop        |
|  jq          |
|  kotlin      |
|  kakoune     |
|  miniconda   |
|  ncdu        |
|  neovim      |
|  npm         |
|  pass        |
|  patchelf    |
|  qtpass      |
|  rust        |
|  sqlite      |
|  taskwarrior |
|  tldr        |
|  tmux        |
|  vim         |
|  zsh         |
|  zlib        |
----------------

_______________________________________________________________________
| HyperPacks  |  Content                                              |
-----------------------------------------------------------------------
|  essential  |  git, curl, npm, zsh, vim, code, atom, sublime-text   |
|  office     |  sqlite, libreoffice                                  |
-----------------------------------------------------------------------
        ''',
        fg='white',
    ),
)

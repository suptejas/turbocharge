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


def show_progress(finding_bar):
    for _ in range(1, 2):
        time.sleep(0.01)
        finding_bar.next()
    click.echo('\n')

def install(package:str, version: str, type:str):
    '''
    Install A Specified Package(s)
    '''
    pass
    # password = getpass('Enter your password: ')

    # turbocharge = Installer()

    # click.echo('\n')

    # os_bar = IncrementalBar('Getting Operating System...', max = 1)
    # os_bar.next()

    # if platform == 'linux':
    #     click.echo('\n')
    #     finding_bar = IncrementalBar('Finding Requested Packages...', max = 1)
    #     if package.install_type == 'p':
    #         show_progress(finding_bar)
    #         turbocharge.install_task(c.devpackages_linux[package.package_name], f'sudo -S apt-get install -y {package.package_name}={package.package_version}', password, f'{package.package_name} --version', [f'{devpackages[package.package_name]} Version'])

    #     if package.install_type == 'a':
    #         show_progress(finding_bar)
    #         turbocharge.install_task(c.applications_linux[package.package_name], f'sudo -S snap install --classic {package.package_name}', password, '', [])

    #     if package.package_name == 'chrome':
    #         show_progress(finding_bar)
    #         try:    
    #             click.echo('\n')
    #             password = getpass("Enter your password: ")
    #             installer_progress = Spinner(message='Installing Chrome...', max=100)
    #             # sudo requires the flag '-S' in order to take input from stdin
    #             for _ in range(1, 75):
    #                 time.sleep(0.03)
    #                 installer_progress.next()
    #             click.echo(click.style('\n Chrome Will Take 2 to 4 Minutes To Download... \n', fg='yellow'))
    #             proc = Popen("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    #             proc.wait()
    #             second = Popen("sudo -S apt-get install -y ./google-chrome-stable_current_amd64.deb".split(), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    #             # Popen only accepts byte-arrays so you must encode the string
    #             second.communicate(password.encode())
                
    #             # stdoutput = (output)[0].decode('utf-8') 
    #             click.echo(click.style('\n\n 🎉 Successfully Installed Chrome! 🎉 \n'))             
    #             # Testing the successful installation of the package
    #             testing_bar = IncrementalBar('Testing package...', max = 100)
    #             for _ in range(1, 21):
    #                 time.sleep(0.045)
    #                 testing_bar.next()
    #             os.system('cd --')
    #             for _ in range(21, 60):
    #                 time.sleep(0.045)
    #                 testing_bar.next()
    #             for _ in range(60, 101):
    #                 time.sleep(0.03)
    #                 testing_bar.next()
    #             click.echo('\n')
    #             click.echo(click.style('Test Passed: Chrome Launch ✅\n', fg='green'))
    #         except  subprocess.CalledProcessError as e:
    #             click.echo(e.output)
    #             click.echo('An Error Occurred During Installation...', err = True)

    #     if package.package_name == 'anaconda':
    #         show_progress(finding_bar)
    #         username = getuser()

    #         try:    
    #             installer_progress = Spinner(message=f'Installing {package.package_name}...', max=100)
    #             # sudo requires the flag '-S' in order to take input from stdin
    #             for _ in range(1, 35):
    #                 time.sleep(0.01)
    #                 installer_progress.next()
    #             os.system("wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh")
    #             for _ in range(35, 61):
    #                 time.sleep(0.01)
    #                 installer_progress.next()

    #             os.system('bash ~/anaconda.sh -b -p $HOME/anaconda3')

    #             for _ in range(61, 91):
    #                 time.sleep(0.01)
    #                 installer_progress.next()

    #             os.system(f'echo "export PATH="/home/{username}/anaconda3/bin:$PATH"" >> ~/.bashrc')
                
    #             for _ in range(90, 101):
    #                 time.sleep(0.01)
    #                 installer_progress.next()
    #             # stdoutput = (output)[0].decode('utf-8')
    #             click.echo(click.style(f'\n\n 🎉 Successfully Installed {package.package_name}! 🎉 \n'))
    #         except  subprocess.CalledProcessError as e:
    #             click.echo(e.output)
    #             click.echo('An Error Occurred During Installation...', err = True)

    #     if package.package_name == 'miniconda':
    #         show_progress(finding_bar)
    #         username = getuser()
    #         try:    
    #             installer_progress = Spinner(message=f'Installing {package.package_name}...', max=100)
    #             # sudo requires the flag '-S' in order to take input from stdin
    #             for _ in range(1, 35):
    #                 time.sleep(0.01)
    #                 installer_progress.next()
    #             os.system("wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/miniconda.sh")
    #             for _ in range(35, 61):
    #                 time.sleep(0.01)
    #                 installer_progress.next()
    #             os.system('bash ~/anaconda.sh -b -p $HOME/anaconda3')
    #             for _ in range(61, 91):
    #                 time.sleep(0.01)
    #                 installer_progress.next()
    #             os.system(f'echo "export PATH="/home/{username}/anaconda3/bin:$PATH"" >> ~/.bashrc')
    #             for _ in range(90, 101):
    #                 time.sleep(0.01)
    #                 installer_progress.next()
    #             # stdoutput = (output)[0].decode('utf-8')
    #             click.echo(click.style(f'\n\n 🎉 Successfully Installed {package.package_name}! 🎉 \n'))
    #         except  subprocess.CalledProcessError as e:
    #             click.echo(e.output)
    #             click.echo('An Error Occurred During Installation...', err = True)
    
    # elif platform == 'win32':
    #     click.echo('\n')
    #     finding_bar = IncrementalBar('Finding Requested Packages...', max=1)

    #     if package_name in devpackages_windows:
    #         show_progress(finding_bar)

    #         turbocharge.install_task(
    #             package_name=devpackages_windows[package_name],
    #             script=f"choco install {package_name} -y",
    #             password="",
    #             test_script=f"{package_name} --version",
    #             tests_passed=[f'{devpackages_windows[package_name]} Version']
    #         )


    #     elif package_name in applications_windows:
    #         show_progress(finding_bar)
    #         turbocharge.install_task(
    #             package_name=applications_windows[package_name],
    #             script=f"choco install {package_name} -y",
    #             password="",
    #             test_script="",
    #             tests_passed=[]
    #         )

    #     elif package_name not in devpackages_windows and package_name not in applications_windows:
    #         click.echo('\n')
    #         click.echo(click.style(':( Package Not Found! :(', fg='red'))
            
    #         suggestions = find(package_name)
    #         if suggestions != []:
    #             click.echo('\n')
    #             click.echo('Turbocharge found similar packages: \n')
    #             for suggestion in suggestions:
    #                 click.echo(f'{suggestion} \n')
    #         else:
    #             click.echo('Turbocharge couldn\'t find similar packages...')
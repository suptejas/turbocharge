from sys import platform
import click
import subprocess
from subprocess import Popen, PIPE, DEVNULL, run
import time
from progress.spinner import Spinner
from getpass import getuser

class Updater:
    def updatepack(self, package_name: str, password: str):
        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(
                    f'sudo -S apt-get install --only-upgrade -y {package_name}'.split(
                    ),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE
                )

                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())

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

                package_type = 'p'

                package_version = subprocess_cmd(
                    f'apt show {package_name}'.split())
                

                with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                line_exists = False

                for line in lines:
                    if package_name in line:
                        line_exists = True

                with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                    if line_exists == False:
                        file.write(
                            f'{package_name} {package_version} {package_type} \n')

                for _ in range(1, 26):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

        elif platform == 'win32':
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

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

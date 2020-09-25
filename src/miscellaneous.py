from subprocess import Popen, PIPE, DEVNULL
import time
import click
from sys import platform
from constants import applications_linux, applications_macos, applications_windows, devpackages_linux, devpackages_macos, devpackages_windows

def is_password_valid(password: str):
    proc = Popen(
        'sudo -k -S -l'.split(),
        stdin=PIPE,
        stderr=PIPE,
        stdout=DEVNULL)

    output = proc.communicate(password.encode())

    if 'incorrect password' in output[1].decode():
        return 1
    else:
        return 0

def show_progress(finding_bar):
    for _ in range(1, 2):
        time.sleep(0.01)
        finding_bar.next()
        
    click.echo('\n')
    
    def find(text):
    suggestions = []
    if platform == 'linux':
        for app in applications_linux:
            if text in app:
                suggestions.append(app)

        for package in devpackages_linux:
            if text in package:
                suggestions.append(app)

    if platform == 'win32':
        for app in applications_windows:
            if text in app:
                suggestions.append(app)

        for package in devpackages_windows:
            if text in package:
                suggestions.append(app)

    if platform == 'darwin':
        for app in applications_macos:
            if text in app:
                suggestions.append(app)

        for package in devpackages_macos:
            if text in package:
                suggestions.append(app)
    return suggestions

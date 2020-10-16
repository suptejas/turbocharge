from subprocess import Popen, PIPE, DEVNULL
import time
import click
from sys import platform
from src.constants import applications_linux, applications_macos, applications_windows, devpackages_linux, devpackages_macos, devpackages_windows
import difflib

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
        application_matches = difflib.get_close_matches(text, applications_linux)
        package_matches = difflib.get_close_matches(text, devpackages_linux)
        suggestions = application_matches + package_matches

    if platform == 'win32':
        application_matches = difflib.get_close_matches(text, applications_windows)
        package_matches = difflib.get_close_matches(text, devpackages_windows)
        suggestions = application_matches + package_matches

    if platform == 'darwin':
        application_matches = difflib.get_close_matches(text, applications_macos)
        package_matches = difflib.get_close_matches(text, devpackages_macos)
        suggestions = application_matches + package_matches

    return suggestions

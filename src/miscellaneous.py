from subprocess import Popen, PIPE, DEVNULL
import time
import click

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
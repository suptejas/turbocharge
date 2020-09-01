import getpass
import subprocess
import time

def is_password_valid():
    password = getpass.getpass()
    proc = subprocess.Popen('sudo -k -S -l'.split(), stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = proc.communicate(password.encode())
    if 'incorrect password' in output[1].decode():
        return 1
    else:
        return 0

print(is_password_valid())

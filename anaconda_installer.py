from subprocess import Popen, PIPE
from getpass import getuser
import os

username = getuser()
os.system("wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh")
os.system('bash ~/anaconda.sh -b -p $HOME/anaconda3')
os.system(f'echo "export PATH="/home/{username}/anaconda3/bin:$PATH"" >> ~/.bashrc')
print('Installation Finished')

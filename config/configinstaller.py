from installer import install
from Installable import Installable

def configInstaller(file_address: str):
    with open(file_address) as file:
        lines = file.readlines()
    for i in range(2, len(lines)):
        data_string = lines[i].split('\n')[0]
        install(data_string)
             
configInstaller()
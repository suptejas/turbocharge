from installer import install
from Installable import Installable

with open('config.tcc') as file:
    counter = 0
    is_valid = False
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        if counter == 0:
            if 'tcinstallconfig' in line:
                is_valid = True
            counter = 1
        if is_valid:
            if 'tcinstallconfig' in line:
                continue
            install(Installable(line.split()[0], line.split()[1], line.split()[2]))
            counter += 1 
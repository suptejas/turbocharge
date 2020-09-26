from installer import install
from Installable import Installable

with open('config.tcc') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        install(Installable(line.split()[0], line.split()[1], line.split()[2]))
             

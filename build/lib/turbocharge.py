  # Copyright 2020 Turbocharge
  #
  # Licensed under the Apache License, Version 2.0 (the "License");
  # you may not use this file except in compliance with the License.
  # You may obtain a copy of the License at
  #
  #    http://www.apache.org/licenses/LICENSE-2.0
  #
  # Unless required by applicable law or agreed to in writing, software
  # distributed under the License is distributed on an "AS IS" BASIS,
  # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  # See the License for the specific language governing permissions and
  # limitations under the License.


import os
import subprocess
import difflib
import time
import click
from halo import Halo
from getpass import getpass, getuser
from progress.spinner import Spinner
from progress.bar import IncrementalBar
from subprocess import Popen, PIPE, DEVNULL, run
from os.path import isfile
from sys import platform
from getpass import getuser
from time import sleep

class HyperPack:
    def __init__(self, packages, applications):
        self.packages = packages
        self.applications = applications

applications_linux = {
    '1password-linux': '1Password',
    'android-studio': 'Android Studio',
    'atom': 'Atom',
    'beekeeper-studio': 'BeeKeeper-Studio',
    'blender': 'Blender',
    'brackets': 'Brackets',
    'cacher': 'Cacher',
    'clion': 'C Lion',
    'code': 'Visual Studio Code',
    'code-insiders': 'Visual Studio Code Insiders',
    'datagrip': 'Data Grip',
    'discord': 'Discord',
    'disk-space-saver': 'Disk Space Saver',
    'easy-disk-cleaner': 'Easy Disk Cleaner',
    'eclipse': 'Eclipse',
    'figma-linux': 'Figma',
    'flutter': 'Flutter',
    'gimp': 'GIMP',
    'gitkraken': 'Gitkraken',
    'goland': 'Go Land',
    'inkscape': 'Inkscape',
    'intellij-idea-educational': 'IntelliJ Idea Educational',
    'kotlin': 'Kotlin',
    'libreoffice': 'Libre Office',
    'librepcb': 'Libre PCB',
    'notepad-plus-plus': 'Notepad++',
    'obs-studio': 'OBS Studio',
    'opera': 'Opera',
    'phpstorm': 'PHPStorm',
    'postman': 'Postman',
    'powershell': 'Powershell',
    'pycharm': 'Pycharm Community',
    'rubymine': 'RubyMine',
    'skype': 'Skype',
    'slack': 'Slack',
    'space': 'Space',
    'spotify': 'Spotify',
    'sublime-text': 'Sublime Text',
    'todoist': 'Todoist',
    'webstorm': 'Web Storm',
}

devpackages_linux = {
    'ansible': 'Ansible',
    'autojump': 'Autojump',
    'chromium-browser': 'Chromium',
    'curl': 'Curl',
    'docker': 'Docker',
    'emacs': 'Emacs',
    'git': 'Git',
    'git-secret': 'Git-secret',
    'golang': 'Go-Lang',
    'htop': 'Htop',
    'jq': 'JQ',
    'julia': 'Julia',
    'kakoune': 'Kakoune',
    'krita': 'Krita',
    'librecad': 'LibreCAD',
    'ncdu': 'Ncdu',
    'neovim': 'Neo Vim',
    'npm': 'Npm',
    'pass': 'Pass',
    'patchelf': 'Patchelf',
    'qtpass': 'QTpass',
    'restic': 'Restic',
    'ruby-full': 'Ruby',
    'rust': 'Rust',
    'sqlite': 'Sqlite',
    'steam': 'Steam',
    'synaptic': 'Synaptic',
    'taskwarrior': 'Task Warrior',
    'tldr': 'Tldr',
    'tmux': 'Tmux',
    'ubuntu-cleaner': 'Ubuntu-cleaner',
    'vim': 'Vim',
    'zlib': 'Z-Lib',
    'zsh': 'Zsh',
}

applications_windows = {
    '7zip': '7 Zip',
    'adobe-reader': 'Adobe Reader DC',
    'androidstudio': 'Android Studio',
    'atom': 'Atom',
    'audacity': 'Audacity',
    'blender': 'Blender',
    'brackets': 'Brackets',
    'ccleaner': 'CCleaner',
    'clion-ide': 'C Lion',
    'cutepdf': 'CutePDF',
    'datagrip': 'Data Grip',
    'discord': 'Discord',
    'dropbox': 'Dropbox',
    'eclipse': 'Eclipse',
    'figma': 'Figma',
    'firefox': 'Firefox',
    'flash-player-plugin': 'Flash Player Plugin',
    'gimp': 'GIMP',
    'goland': 'Go Land',
    'googlechrome': 'Google Chrome',
    'itunes': 'iTunes',
    'kotlinc': 'Kotlin',
    'libreoffice-fresh': 'Libre Office',
    'malwarebytes': 'Malwarebytes',
    'microsoft-edge': 'Microsoft Edge',
    'microsoft-windows-terminal': 'Windows Terminal',
    'mingw': 'MinGW',
    'notepadplusplus': 'Notepad++',
    'opera': 'Opera',
    'postman': 'Postman',
    'pycharm-community': 'Pycharm Community',
    'rubymine': 'RubyMine',
    'skype': 'Skype',
    'sourcetree': 'Source Tree',
    'spotify': 'Spotify',
    'sublimetext3': 'Sublime Text',
    'teamviewer': 'Teamviewer',
    'thunderbird': 'Thunderbird',
    'virtualbox': 'VirtualBox',
    'vlc': 'VLC Media Player',
    'vscode': 'Visual Studio Code',
    'vscode-insiders': 'Visual Studio Code Insiders',
    'webstorm': 'Web Storm',
    'winrar': 'WinRAR',
    'wireshark': 'Wireshark',
    'zoom': 'Zoom',
    'discord': 'Discord',
}

devpackages_windows = {
    'autoruns': 'Autoruns',
    'awscli': 'AwsCLI',
    'azure-cli': 'Azure-CLI',
    'boxstarter': 'BoxStarter',
    'cgywin': 'CGYWin',
    'curl': 'Curl',
    'docker': 'Docker',
    'emacs': 'Emacs',
    'fzf': 'Fzf',
    'git': 'Git',
    'golang': 'Go-Lang',
    'jq': 'JQ',
    'julia': 'Julia',
    'neovim': 'Neo Vim',
    'ninja': 'Ninja',
    'nodejs': 'Npm',
    'ntop.portable': 'Ntop',
    'openssh': 'OpenSSH',
    'pass': 'Pass',
    'php': 'PHP',
    'putty': 'Putty',
    'python': 'Python Latest Version',
    'python2': 'Python 2',
    'python3': 'Python 3',
    'qtpass': 'QTpass',
    'ruby': 'Ruby',
    'rust': 'Rust',
    'sqlite': 'Sqlite',
    'tldr': 'Tldr',
    'vim': 'Vim',
    'wget': 'Wget',
    'yarn': 'Yarn',
}

hyperpkgs = {
    'essential': HyperPack('git,curl,npm,zsh,vim,synaptic', 'code,atom,sublime-text,1password-linux'),
    'office': HyperPack('vim,synaptic', 'libreoffice,todoist,slack,skype,1password-linux'),
    'artist': HyperPack('krita,', 'gimp,inkscape,figma-linux'),
    'pccare': HyperPack('ubuntu-cleaner,restic', 'easy-disk-cleaner,disk-space-saver'),
    'gamer': HyperPack('steam', 'discord'),
    'godev': HyperPack('golang', 'goland'),
    'flutter': HyperPack('git', 'android-studio,figma-linux'),
}

applications_macos = {
    '1password': '1Password',
    'adoptopenjdk8': 'AdoptOpenJDK8',
    'alfred': 'Alfred',
    'anaconda': 'Anaconda',
    'android-platform-tools': 'Android Platform Tools',
    'android-studio': 'Android Studio',
    'atom': 'Atom',
    'beekeeper-studio': 'BeeKeeper-Studio',
    'blender': 'Blender',
    'brackets': 'Brackets',
    'cacher': 'Cacher',
    'chromedriver': 'ChromeDriver',
    'chromium': 'Chromium',
    'clion': 'C Lion',
    'datagrip': 'Data Grip',
    'discord': 'Discord',
    'docker': 'Docker',
    'figma': 'Figma',
    'firefox': 'Firefox',
    'flash-player': 'Adobe Flash Player',
    'flutter': 'Flutter',
    'gimp': 'GIMP',
    'gitkraken': 'Gitkraken',
    'goland': 'Go Land',
    'google-chrome': 'Google Chrome',
    'hyper': 'Hyper',
    'inkscape': 'Inkscape',
    'intellij-idea-ce': 'IntelliJ Idea Community',
    'iterm2': 'iTerm 2',
    'java': 'Java',
    'julia': 'Julia',
    'kotlin': 'Kotlin',
    'krita': 'Krita',
    'librecad': 'LibreCAD',
    'libreoffice': 'Libre Office',
    'librepcb': 'Libre PCB',
    'lnkd-ecl': 'ECL',
    'microsoft-office': 'Microsoft Office',
    'microsoft-teams': 'Microsoft Teams',
    'miniconda': 'Miniconda',
    'obs': 'OBS',
    'opera': 'Opera',
    'osxfuse': 'OSXFuse',
    'phpstorm': 'PHPStorm',
    'postman': 'Postman',
    'powershell': 'Powershell',
    'pycharm': 'Pycharm Community',
    'rubymine': 'RubyMine',
    'skype': 'Skype',
    'slack': 'Slack',
    'sourcetree': 'Source Tree',
    'spotify': 'Spotify',
    'steam': 'Steam',
    'sublime-text': 'Sublime Text',
    'teamviewer': 'Team Viewer',
    'telegram': 'Telegram',
    'vagrant': 'Vagrant',
    'virtualbox': 'Virtual Box',
    'visual-studio-code': 'Visual Studio Code',
    'vlc': 'VLC Media Player',
    'webstorm': 'Web Storm',
    'whatsapp': 'Whatsapp',
    'wine-stable': 'Wine',
    'xquartz': 'XQuartz',
    'zoomus': 'Zoom.us',
}

devpackages_macos = {
    'ansible': 'Ansible',
    'autojump': 'Autojump',
    'curl': 'Curl',
    'docker': 'Docker',
    'emacs': 'Emacs',
    'git': 'Git',
    'git-secret': 'Git-secret',
    'go': 'Go-Lang',
    'htop': 'Htop',
    'jq': 'JQ',
    'kakoune': 'Kakoune',
    'ncdu': 'Ncdu',
    'neovim': 'Neo Vim',
    'node': 'Node',
    'pass': 'Pass',
    'patchelf': 'Patchelf',
    'qtpass': 'QTpass',
    'restic': 'Restic',
    'ruby': 'Ruby',
    'rust': 'Rust',
    'sqlite': 'Sqlite',
    'tldr': 'Tldr',
    'tmux': 'Tmux',
    'vim': 'Vim',
    'zlib': 'Z-Lib',
    'zsh': 'Zsh',
}


apt_script = 'sudo -S apt-get install -y'
apt_remove = 'sudo -S apt-get remove -y'

snap_script = 'sudo -S snap install --classic'
snap_remove = 'sudo -S snap remove'

chrome_link = 'wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'
chrome_move = f'mv google-chrome-stable_current_amd64.deb /home/{getuser()}'
chrome_setup = 'sudo -S apt-get install -y /home/{getuser()}/google-chrome-stable_current_amd64.deb'

anaconda_download = 'wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh'
anaconda_setup = 'bash ~/anaconda.sh -b -p $HOME/anaconda3'
anaconda_PATH = f'echo "export PATH="/home/{getuser()}/anaconda3/bin:$PATH"" >> ~/.bashrc'
anaconda_remove_folder = 'rm -rf ~/anaconda3 ~/.continuum ~/.conda'
anaconda_remove_file = 'rm ~/anaconda.sh'

miniconda_download = 'wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh'
miniconda_setup = 'bash ~/miniconda.sh -b -p $HOME/miniconda'
miniconda_PATH = f'echo "export PATH="/home/{getuser()}/miniconda/bin:$PATH"" >> ~/.bashrc'
miniconda_remove_folder = 'rm -rf ~/miniconda ~/.continuum ~/.conda ~/.condarc'
miniconda_remove_file = 'rm ~/miniconda.sh'


display_list_linux = '''
_______________________________________________________
| Applications                   |Duration||   Size   |
-------------------------------------------------------
| 1password-linux                |   1m   || 114.9 MB |
| android-studio                 |   5m   || 840.0 MB |
| atom                           |   2m   || 224.8 MB |
| beekeeper-studio               |   1m   || 79.1  MB |
| blender                        |   2m   || 187.7 MB |
| brackets                       |   1m   || 109.6 MB |
| cacher                         |   1m   || 73.8  MB |
| clion                          |   3m   || 502.0 MB |
| chromium-browser               |   1m   || 169.9 MB |
| chrome                         |   1m   || 70.2  MB |
| datagrip                       |   2m   || 356.8 MB |
| discord                        |   1m   || 60.1  MB |
| eclipse                        |   2m   || 220.3 MB |
| figma-linux                    |   2m   || 96.4  MB |
| gimp                           |   2m   || 263.2 MB |
| gitkraken                      |   1m   || 171.2 MB |
| inkscape                       |   1m   || 14.9  MB |
| intellij-idea-educational      |   1m   || 14.9  MB |
| krita                          |   1m   || 147.0 MB |
| libreoffice                    |   1m   || 25.0  MB |
| librecad                       |   1m   || 2.6   MB |
| librepcb                       |   1m   || 98.8  MB |
| notepad++                      |   1m   || 79.1  MB |
| obs-studio                     |   1m   || 179.2 MB |
| opera                          |   1m   || 64.2 MB  |
| pycharm                        |   3m   || 372.1 MB |
| postman                        |   1m   || 184.8 MB |
| phpstorm                       |   3m   || 373.9 MB |
| powershell                     |   1m   || 62.5  MB |
| rubymine                       |   3m   || 363.2 MB |
| space                          |   1m   || 67.1  MB |
| spotify                        |   1m   || 171.6 MB |
| slack                          |   1m   || 144.1 MB |
| sublime-text                   |   1m   || 70.8  MB |
| skype                          |   1m   || 188.2 MB |
| todoist                        |   1m   || 66.2  MB |
| webstorm                       |   3m   || 343.8 MB |
| vscode                         |   2m   || 162.5 MB |
| vscode-insiders                |   2m   || 153.3 MB |
-------------------------------------------------------
_____________________
| Package           |
---------------------
|  anaconda         |
|  ansible          |
|  autojump         |
|  curl             |
|  docker           |
|  emacs            |
|  flutter          |
|  git              |
|  golang           |
|  htop             |
|  julia            |
|  jq               |
|  kotlin           |
|  kakoune          |
|  miniconda        |
|  ncdu             |
|  neovim           |
|  npm              |
|  pass             |
|  patchelf         |
|  qtpass           |
|  ruby             |
|  restic           |
|  rust             |
|  steam            |
|  synaptic         |
|  sqlite           |
|  taskwarrior      |
|  tldr             |
|  tmux             |
|  ubuntu-cleaner   |
|  vim              |
|  zsh              |
|  zlib             |
---------------------
_________________________________________________________________________________
| HyperPacks  |  Content                                                        |
---------------------------------------------------------------------------------
|  essential  |  git, curl, npm, zsh, vim, code, atom, sublime-text             |
|  office     |  sqlite, libreoffice                                            |
---------------------------------------------------------------------------------
'''


display_list_windows = '''
_______________________________
| Applications                |
| 7zip                        |
| adobe-reader                |
| androidstudio               |
| atom                        |
| audacity                    |
| blender                     |
| brackets                    |
| ccleaner                    |
| clion-ide                   |
| cutepdf                     |
| datagrip                    |
| discord                     |
| dropbox                     |
| eclipse                     |
| figma                       |
| firefox                     |
| flash-player-plugin         |
| gimp                        |
| goland                      |
| googlechrome                |
| itunes                      |
| kotlinc                     |
| libreoffice-fresh           |
| malwarebytes                |
| microsoft-edge              |
| microsoft-windows-terminal  |
| mingw                       |
| notepadplusplus             |
| opera                       |
| postman                     |
| pycharm-community           |
| rubymine                    |
| skype                       |
| sourcetree                  |
| spotify                     |
| sublimetext3.app            |
| teamviewer                  |
| thunderbird                 |
| virtualbox                  |
| vlc                         |
| vscode                      |
| vscode-insiders             |
| webstorm                    |
| winrar                      |
| wireshark                   |
| zoom                        |
-------------------------------

____________________
| Package           |
---------------------
| autoruns          |
| awscli            |
| azure-cli         |
| boxstarter        |
| cgywin            |
| curl              |
| docker            |
| emacs             |
| fzf               |
| git               |
| golang            |
| jq                |
| julia             |
| neovim            |
| ninja             |
| nodejs            |
| ntop.portable     |
| openssh           |
| pass              |
| php               |
| putty             |
| python            |
| python2           |
| python3           |
| qtpass            |
| ruby              |
| rust              |
| sqlite            |
| tldr              |
| vim               |
| wget              |
| yarn              |
---------------------

_______________________________________________________________________
| HyperPacks  |  Content                                              |
-----------------------------------------------------------------------
|  essential  |  git, curl, npm, vim, vscode, atom, sublimetext3      |
|  office     |  sqlite, libreoffice                                  |
-----------------------------------------------------------------------
'''


display_list_macos = '''
_____________________________
| Applications              |
-----------------------------
| 1password                 |
| adoptopenjdk8             |
| alfred                    |
| anaconda                  |
| android-platform-tools    |
| android-studio            |
| atom                      |
| beekeeper-studio          |
| blender                   |
| brackets                  |
| cacher                    |
| chromedriver              |
| chromium                  |
| clion                     |
| datagrip                  |
| discord                   |
| docker                    |
| figma                     |
| firefox                   |
| flash-player              |
| flutter                   |
| gimp                      |
| gitkraken                 |
| goland                    |
| google-chrome             |
| hyper                     |
| inkscape                  |
| intellij-idea-ce          |
| iterm2                    |
| java                      |
| julia                     |
| kotlin                    |
| krita                     |
| librecad                  |
| libreoffice               |
| librepcb                  |
| lnkd-ecl                  |
| microsoft-office          |
| microsoft-teams           |
| miniconda                 |
| obs                       |
| opera                     |
| osxfuse                   |
| phpstorm                  |
| postman                   |
| powershell                |
| pycharm                   |
| rubymine                  |
| skype                     |
| slack                     |
| sourcetree                |
| spotify                   |
| steam                     |
| sublime-text              |
| teamviewer                |
| telegram                  |
| vagrant                   |
| virtualbox                |
| visual-studio-code        |
| vlc                       |
| webstorm                  |
| whatsapp                  |
| wine-stable               |
| xquartz                   |
| zoomus                    |
-----------------------------
_____________________
| Package            |
---------------------
| ansible            |
| autojump           |
| curl               |
| docker             |
| emacs              |
| git                |
| git-secret         |
| go                 |
| htop               |
| jq                 |
| kakoune            |
| ncdu               |
| neovim             |
| node               |
| pass               |
| patchelf           |
| qtpass             |
| restic             |
| ruby               |
| rust               |
| sqlite             |
| tldr               |
| tmux               |
| vim                |
| zlib               |
| zsh                |
---------------------
_________________________________________________________________________________
| HyperPacks  |  Content                                                        |
---------------------------------------------------------------------------------
|  essential  |  git, curl, npm, zsh, vim, code, atom, sublime-text             |
|  office     |  sqlite, libreoffice                                            |
---------------------------------------------------------------------------------
'''

class Updater:
    # the pacakage name here is directly as typed by user, hence like the keys of
    # dictionaries we have in constants.py . So no need on using getKey() here.

    def updatepack(self, package_name: str, password: str):
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

        def parse(string):
            var1 = string.split(": ")
            if len(var1[1]) > 7:
                var2 = var1[1].split(" ")
                return var2[1]
            else:
                var2 = var1[1].split("\n")
                return var2[0]

        def getWinVer(output: str, name: str):
            lines = output.split('\n')
            for line in lines:
                line = line.split()
                version = line[1]
                package_name = line[0]
                if name == package_name:
                    return version

                return

        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Updating {devpackages_linux[package_name]}...', max=100)

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

                package_type = 'p'

                package_version = subprocess_cmd(
                    f'apt show {package_name}'.split())

                if isfile(f'/home/{getuser()}/config.tcc'):
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()

                    package_exists = False
                    package_idx = -1
                    for i in range(len(lines)):
                        if (package_name in lines[i]):
                            package_exists = True
                            package_idx = i
                            break
                    lines[package_idx] = f'{package_name} {package_version} {package_type} 1 {1 if package_name in devpackages_windows.keys() else 0} {1 if package_name in devpackages_macos.keys() else 0}\n'

                    # The order for the package compatiblity numbers is
                    # Linux, Windows, MacOS
                    if package_exists == False:
                        with open(f'/home/{getuser()}/config.tcc', 'w') as file:
                            file.writelines(lines)

                for _ in range(1, 26):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {devpackages_linux[package_name]}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

        if platform == 'win32':
            try:
                installer_progress = Spinner(
                    message=f'Updating {devpackages_windows[package_name]}...', max=100)

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
                        f'\n\n 🎉 Successfully Updated {devpackages_windows[package_name]}! 🎉 \n',
                        fg='green'))

                with open(os.path.join("C:\\Turbocharge", "config.tcc"), 'r') as file:
                    lines = file.readlines()

                package_exists = False

                w_version = subprocess.Popen(
                    "clist -l", stdin=PIPE, stderr=PIPE, stdout=PIPE)
                output = w_version.communicate()
                version = getWinVer(output, package_name)
                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} p {1 if package_name in devpackages_linux.keys() else 0} 1 {1 if package_name in devpackages_macos.keys() else 0}\n'

                with open(os.path.join("C:\\Turbocharge", "config.tcc"), 'w') as file:
                    file.writelines(lines)

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(f'brew upgrade {package_name}'.split(),
                    stdout=PIPE, stderr=PIPE)

                package_type = 'p'

                proc = Popen(f'brew info {package_name}'.split(
                ), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output = proc.communicate()
                parsable = output[0].decode('utf-8')

                package_version = parse(parsable)

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} p {1 if package_name in devpackages_linux.keys() else 0} {1 if package_name in devpackages_windows.keys() else 0} 1\n'

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    file.writelines(lines)

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

        def getWinVer(output: str, name: str):
            lines = output.split('\n')
            for line in lines:
                line = line.split()
                version = line[1]
                package_name = line[0]
                if name == package_name:
                    return version

                return

        def parse(string):
            var1 = string.split(": ")
            if len(var1[1]) > 7:
                var2 = var1[1].split(" ")
                return var2[1]
            else:
                var2 = var1[1].split("\n")
                return var2[0]
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

                # TODO: possible bug here because the command gives a different output than what the function was designed to parse.
                package_version = subprocess_cmd(
                    f'snap info {package_name}'.split())

                if isfile(f'/home/{getuser()}/config.tcc'):
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()

                    package_exists = False
                    package_idx = -1
                    for i in range(len(lines)):
                        if (package_name in lines[i]):
                            package_exists = True
                            package_idx = i
                            break
                    lines[package_idx] = f'{package_name} {package_version} a 1 {1 if package_name in devpackages_windows.keys() else 0} {1 if package_name in devpackages_macos.keys() else 0}\n'

                    # The order for the package compatiblity numbers is
                    # Linux, Windows, MacOS
                    if package_exists == False:
                        with open(f'/home/{getuser()}/config.tcc', 'w') as file:
                            file.writelines(lines)

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating...', err=True)

        if platform == 'win32':
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

                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'r') as file:
                    lines = file.readlines()

                package_exists = False

                w_version = subprocess.Popen(
                    "clist -l", stdin=PIPE, stderr=PIPE, stdout=PIPE)
                output = w_version.communicate()
                version = getWinVer(output, package_name)
                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} p {1 if package_name in devpackages_linux.keys() else 0} 1 {1 if package_name in devpackages_macos.keys() else 0}\n'

                with open(os.path.join(os.path.abspath(os.getcwd()), "config.tcc"), 'w') as file:
                    file.writelines(lines)

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)

        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Updating {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(f'brew cask upgrade {package_name}',
                    stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(f'brew info {package_name}'.split(
                ), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                output = proc.communicate()
                parsable = output[0].decode('utf-8')

                package_version = parse(parsable)

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    lines = file.readlines()

                package_exists = False
                package_idx = -1
                for i in range(len(lines)):
                    if (package_name in lines[i]):
                        package_exists = True
                        package_idx = i
                        break
                lines[package_idx] = f'{package_name} {version} a {1 if package_name in devpackages_linux.keys() else 0} {1 if package_name in devpackages_windows.keys() else 0} 1\n'

                with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                    file.writelines(lines)

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Updated {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occurred During Updating..', err=True)


class Setup:
    def setup(self):
        user = getuser()
        if platform == 'darwin':
            # Installing and setting up Homebrew
            click.echo(click.style(
                'Setting Up Turbocharge on your Mac...', fg='green'))

            os.system(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" < /dev/null')

            file_exists = bool(isfile(f'/Users/{getuser()}/config.tcc'))
            if not file_exists:
                with open(f'/Users/{getuser()}/config.tcc', 'w+') as f:
                    f.write(f'darwin\n{user}\n')

        elif platform == 'linux':
            # Creating the config file
            setup_progress = IncrementalBar(
                message='Setting Up Your Turbocharge Config...', max=100)
            for _ in range(1, 101):
                sleep(0.02)
                setup_progress.next()

            file_exists = None
            file_exists = bool(isfile(f'/home/{getuser()}/config.tcc'))
            if not file_exists:
                with open(f'/home/{getuser()}/config.tcc', 'w+') as f:
                    f.write(f'linux\n{user}\n')

        elif platform == 'win32':
            # Install Chocolatey And Setup
            home = os.path.expanduser('~')
            with Halo(text='Setting Up Turbocharge Configuration ') as h:
                file_exists = None
                os.system(rf'mkdir {home}\Turbocharge')
                if isfile(os.path.join(rf"{home}\Turbocharge\config.tcc")):
                    file_exists = True
                else:
                    file_exists = False

                if not file_exists:
                    with open(os.path.join(rf"{home}\Turbocharge", "config.tcc"), 'w+') as f:
                        f.write(f'win32\n{user}\n')

        click.echo('\n')
        click.echo(click.style('Succesfully Setup Turbocharge!', 'green'))


class Debugger:
    def debug(self, password: str, error: bytes):
        error = error.decode('utf-8')

        if 'sudo: 1 incorrect password attempt' in error:
            click.echo(
                click.style(
                    '✅ Successful Debugging! ✅ \n',
                    fg='green',
                    bold=True))
            click.echo(
                click.style(
                    f'Cause: Wrong Password Entered. Code: 001',
                    fg='yellow',
                    bold=True,
                    blink=True))

        else:
            click.echo(click.style(':( Failed To Debug... :(', fg='red'))


        return


class Installer:
    def install_task(self, package_name: str, script: str,
                     password: str, test_script: str, tests_passed):

        def get_key(val, dictionary):
            final = ''
            for key, value in dictionary.items():
                if val == value:
                    final = key
                    break

            if final != '':
                return final
            else:
                return -1

        def getWinVer(output: str, name: str):
            lines = output.split('\n')
            for line in lines:
                line = line.split()

                version = line[1]
                package_name = line[0]

                if name == package_name:
                    return version

                return

        def subprocess_cmd(command):
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stdin=PIPE, stderr=PIPE)
            proc_stdout = process.communicate()[0].strip()
            decoded = proc_stdout.decode("utf-8")
            version_tag = decoded.split("\n")[1]
            # using [1:] might be useful in some scenario where the
            # version has multiple colons in it.
            cleaned_version = version_tag.split(": ")[1]
            return cleaned_version

        def parse(string):
            var1 = string.split(": ")
            if len(var1[1]) > 7:
                var2 = var1[1].split(" ")
                return var2[1]
            else:
                var2 = var1[1].split("\n")
                return var2[0]

        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Installing {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.01)
                    installer_progress.next()

                proc = Popen(
                    script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

                # Popen only accepts byte-arrays so you must encode the string
                output, error = proc.communicate(password.encode())

                if proc.returncode != 0:
                    click.echo(
                        click.style(
                            '❎ Installation Failed... ❎',
                            fg='red',
                            blink=True,
                            bold=True))

                    debug = click.prompt(
                        'Would you like us to debug the failed installation?[y/n]')

                    if debug == 'y':
                        debugger = Debugger()
                        debugger.debug(password, error)

                        logs = click.prompt(
                            'Would you like to see the logs?[y/n]', type=str)

                        if logs == 'y':
                            final_output = error.decode('utf-8')

                            if final_output == '':
                                click.echo('There were no logs found...')

                                return
                            else:
                                click.echo(final_output)

                                return
                        return
                    else:
                        logs = click.prompt(
                            'Would you like to see the logs?[y/n]', type=str)

                        if logs == 'y':
                            final_output = output.decode('utf-8')

                            if final_output == '':
                                click.echo('There were no logs found...')

                                return
                            else:
                                click.echo(final_output)

                                return
                        return

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n',
                        fg='green',
                        bold=True))

                package_type = None

                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'

                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max=100)

                if tests_passed == [] and test_script == '':
                    if package_type == 'a':

                        if isfile(f'/home/{getuser()}/config.tcc'):
                            with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                                lines = file.readlines()

                            package_exists = False

                            for line in lines:
                                if get_key(package_name, applications_linux) in line:
                                    package_exists = True

                            # The order for the package compatiblity numbers is
                            # Linux, Windows, MacOS
                            if package_exists == False:
                                with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                                    file.write(
                                        f'{get_key(package_name, applications_linux)} None {package_type} 1 {0 if get_key(package_name, applications_windows)==-1 else 1} {0 if get_key(package_name, applications_macos)==-1 else 1}\n')

                    click.echo('\n')
                    click.echo(
                        click.style(
                            f'Test Passed: {package_name} Launch ✅\n',
                            fg='green'))

                    return

                for _ in range(1, 21):
                    time.sleep(0.002)
                    testing_bar.next()

                for _ in range(21, 60):
                    time.sleep(0.002)
                    testing_bar.next()

                proc = Popen(
                    test_script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

                package_type = None
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'

                if package_type == 'p':

                    file_exists = False
                    if isfile(f'/home/{getuser()}/config.tcc'):
                        file_exists = True

                    package_version = subprocess_cmd(
                        f'apt show {get_key(package_name, devpackages_linux)}'.split())

                    if file_exists:
                        with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                            lines = file.readlines()

                        package_exists = False

                        for line in lines:
                            if get_key(package_name, devpackages_linux) in line:
                                package_exists = True

                        if package_exists == False:
                            with open(f'/home/{getuser()}/config.tcc', 'a+') as file:
                                file.write(
                                    f'{get_key(package_name, devpackages_linux)} {package_version} {package_type} 1 {0 if get_key(package_name, devpackages_windows)==-1 else 1} {0 if get_key(package_name, devpackages_macos)==-1 else 1}\n')

                for _ in range(60, 101):
                    time.sleep(0.002)
                    testing_bar.next()

                click.echo('\n')

                for test in tests_passed:
                    click.echo(
                        click.style(
                            f'Test Passed: {test} ✅\n',
                            fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

        elif platform == 'win32':
            try:
                installer_progress = Spinner(
                    message=f'Installing {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.01)
                    installer_progress.next()

                run(script, stdout=PIPE, stderr=PIPE)  # first time

                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n',
                        fg='green',
                        bold=True))

                testing_bar = IncrementalBar('Testing package...', max=100)

                # this condition will be true for all applications

                if tests_passed == [] and test_script == '':
                    # Dont run any tests, just exit

                    click.echo('\n')
                    click.echo(
                        click.style(
                            f'Test Passed: {package_name} Launch ✅\n',
                            fg='green'))

                    return

                for _ in range(1, 64):
                    time.sleep(0.002)
                    testing_bar.next()

                run(test_script, stdout=PIPE, stderr=PIPE)

                in_app = get_key(package_name, applications_windows)
                in_dev = get_key(package_name, devpackages_windows)

                w_version = subprocess.Popen(
                    "clist -l", stdin=PIPE, stderr=PIPE, stdout=PIPE)

                output = w_version.communicate()[0].decode()

                package_exists = False

                with open(os.path.join(f"C:\\Users\\{getuser()}\Turbocharge", "config.tcc"), 'r') as f:
                    lines = f.readlines()

                for i in range(len(lines)):
                    if (str(in_app) in lines[i]) or (str(in_dev) in lines[i]):
                        package_exists = True
                        break

                if not package_exists:
                    if in_app != -1:
                        version = getWinVer(output, in_app)
                        with open(os.path.join(f"C:\\Users\\{getuser()}\Turbocharge", "config.tcc"), 'a+') as f:
                            f.write(
                                f'{in_app} {version} a {0 if get_key(package_name, applications_windows)==-1 else 1} 1 {0 if get_key(package_name, applications_macos)==-1 else 1}\n')

                    elif in_dev != -1:
                        version = getWinVer(output, in_dev)
                        with open(os.path.join(f"C:\\Users\\{getuser()}\Turbocharge", "config.tcc"), 'a+') as f:
                            f.write(
                                f'{in_dev} {version} p {0 if get_key(package_name, devpackages_windows)==-1 else 1} 1 {0 if get_key(package_name, devpackages_macos)==-1 else 1}\n')

                for _ in range(64, 101):
                    time.sleep(0.002)
                    testing_bar.next()

                click.echo('\n')

                for test in tests_passed:
                    click.echo(
                        click.style(
                            f'Test Passed: {test} ✅\n',
                            fg='green'))

                return

            except Exception as e:
                click.echo(e)
                click.echo('An Error Occured During Installation...', err=True)

        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Installing {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.01)
                    installer_progress.next()

                proc = Popen(
                    script.split(),
                    stdout=PIPE,
                    stdin=PIPE,
                    stderr=PIPE)

                # Popen only accepts byte-arrays so you must encode the string
                output, error = proc.communicate(password.encode())

                if proc.returncode != 0:
                    click.echo(
                        click.style(
                            '❎ Installation Failed... ❎',
                            fg='red',
                            blink=True,
                            bold=True))

                    debug = click.prompt(
                        'Would you like us to debug the failed installation?[y/n]')

                    if debug == 'y':
                        debugger = Debugger()
                        debugger.debug(password, error)

                        logs = click.prompt(
                            'Would you like to see the logs?[y/n]', type=str)

                        if logs == 'y':
                            final_output = error.decode('utf-8')

                            if final_output == '':
                                click.echo('There were no logs found...')

                                return
                            else:
                                click.echo(final_output)

                                return
                        return
                    else:
                        logs = click.prompt(
                            'Would you like to see the logs?[y/n]', type=str)

                        if logs == 'y':
                            final_output = output.decode('utf-8')

                            if final_output == '':
                                click.echo('There were no logs found...')

                                return
                            else:
                                click.echo(final_output)

                                return
                        return

                click.echo(
                    click.style(
                        f'\n\n 🎉  Successfully Installed {package_name}! 🎉 \n',
                        fg='green',
                        bold=True))

                package_type = None

                if 'brew install' in script:
                    package_type = 'p'
                elif 'brew cask install' in script:
                    package_type = 'a'

                # Testing the successful installation of the package
                testing_bar = IncrementalBar('Testing package...', max=100)

                if tests_passed == [] and test_script == '':
                    if package_type == 'a':
                        file_exists = False
                        if isfile(f'/Users/{getuser()}/config.tcc'):
                            file_exists = True

                        if file_exists:
                            with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                                lines = file.readlines()

                            package_exists = False

                            for line in lines:
                                if get_key(package_name, applications_macos) in line:
                                    package_exists = True

                            # The order for the package compatiblity numbers is
                            # Linux, Windows, MacOS
                            if package_exists == False:
                                with open(f'/Users/{getuser()}/config.tcc', 'a+') as file:
                                    file.write(
                                        f'{get_key(package_name, applications_macos)} None {package_type} {0 if get_key(package_name, applications_linux)==-1 else 1} {0 if get_key(package_name, applications_windows)==-1 else 1} 1\n')

                    click.echo('\n')
                    click.echo(
                        click.style(
                            f'Test Passed: {package_name} Launch ✅\n',
                            fg='green'))

                    return

                for _ in range(1, 21):
                    time.sleep(0.002)
                    testing_bar.next()

                for _ in range(21, 60):
                    time.sleep(0.002)
                    testing_bar.next()

                proc = Popen(
                    test_script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

                package_type = None
                if 'brew install' in script:
                    package_type = 'p'
                elif 'brew cask install' in script:
                    package_type = 'a'

                if package_type == 'p':
                    file_exists = False
                    if isfile(f'/Users/{getuser()}/config.tcc'):
                        file_exists = True

                    proc = Popen(f'brew info {package_name}'.split(
                    ), stdin=PIPE, stdout=PIPE, stderr=PIPE)
                    stdout = proc.communicate()
                    parsing = stdout[0].decode('utf-8')

                    package_version = parse(parsing)

                    if file_exists:
                        with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                            lines = file.readlines()

                        line_exists = False

                        for line in lines:
                            if get_key(package_name, devpackages_macos) in line:
                                line_exists = True

                        # TODO : Implement versioning for macOS
                        with open(f'/Users/{getuser()}/config.tcc', 'a+') as file:
                            if line_exists == False:
                                file.write(
                                    f'{get_key(package_name, devpackages_macos)} {package_version} {package_type} {0 if get_key(package_name, devpackages_linux)==-1 else 1} {0 if get_key(package_name, devpackages_windows)==-1 else 1} 1\n')

                for _ in range(60, 101):
                    time.sleep(0.002)
                    testing_bar.next()

                click.echo('\n')

                for test in tests_passed:
                    click.echo(
                        click.style(
                            f'Test Passed: {test} ✅\n',
                            fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)


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
    if platform == 'darwin':
        application_matches = difflib.get_close_matches(text, applications_macos)
        package_matches = difflib.get_close_matches(text, devpackages_macos)
        suggestions = application_matches + package_matches

    elif platform == 'linux':
        application_matches = difflib.get_close_matches(text, applications_linux)
        package_matches = difflib.get_close_matches(text, devpackages_linux)
        suggestions = application_matches + package_matches

    elif platform == 'win32':
        application_matches = difflib.get_close_matches(text, applications_windows)
        package_matches = difflib.get_close_matches(text, devpackages_windows)
        suggestions = application_matches + package_matches

    return suggestions


class Uninstaller:
    def uninstall(self, script: str, password: str, package_name: str):

        def get_key(val, dictionary):
            for key, value in dictionary.items():
                if val == value:
                    return key

        if platform == 'linux':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(
                    script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())

                file_exists = False
                if isfile(f'/home/{getuser()}/config.tcc'):
                    file_exists = True

                if file_exists:
                    with open(f'/home/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()
                else:
                    for _ in range(1, 25):
                        time.sleep(0.01)
                        installer_progress.next()

                    click.echo(
                        click.style(
                            f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                            fg='green'))
                    return

                package_type = None
                if 'sudo -S apt-get' in script:
                    package_type = 'p'
                elif 'sudo -S snap' in script:
                    package_type = 'a'

                dictionary = None
                if package_type == 'p':
                    dictionary = devpackages_linux

                elif package_type == 'a':
                    dictionary = applications_linux

                with open(f'/home/{getuser()}/config.tcc', 'w+') as file:
                    for line in lines:
                        if get_key(package_name, dictionary) in line:
                            continue
                        else:
                            file.write(line)

                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

        elif platform == 'win32':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling {package_name}...', max=100)

                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                run(script, stdout=PIPE, stderr=PIPE)

                for _ in range(1, 25):
                    time.sleep(0.007)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉 Successfully Uninstalled {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

        if platform == 'darwin':
            try:
                installer_progress = Spinner(
                    message=f'Uninstalling {package_name}...', max=100)

                # sudo requires the flag '-S' in order to take input from stdin
                for _ in range(1, 75):
                    time.sleep(0.007)
                    installer_progress.next()

                proc = Popen(
                    script.split(),
                    stdin=PIPE,
                    stdout=PIPE,
                    stderr=PIPE)

                # Popen only accepts byte-arrays so you must encode the string
                proc.communicate(password.encode())

                file_exists = False
                if isfile(f'/Users/{getuser()}/config.tcc'):
                    file_exists = True

                if file_exists:
                    with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
                        lines = file.readlines()
                else:
                    for _ in range(1, 25):
                        time.sleep(0.01)
                        installer_progress.next()

                    click.echo(
                        click.style(
                            f'\n\n 🎉  Successfully Uninstalled {package_name}! 🎉 \n',
                            fg='green'))
                    return

                package_type = None
                if 'brew uninstall' in script:
                    package_type = 'p'
                elif 'brew cask uninstall' in script:
                    package_type = 'a'

                dictionary = None
                if package_type == 'p':
                    dictionary = devpackages_macos

                elif package_type == 'a':
                    dictionary = applications_macos

                with open(f'/Users/{getuser()}/config.tcc', 'w+') as file:
                    for line in lines:
                        if get_key(package_name, dictionary) in line:
                            continue
                        else:
                            file.write(line)

                # stdoutput = (output)[0].decode('utf-8')
                for _ in range(1, 25):
                    time.sleep(0.01)
                    installer_progress.next()

                click.echo(
                    click.style(
                        f'\n\n 🎉  Successfully Uninstalled {package_name}! 🎉 \n',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

    def clean(self, password: str):
        if platform == 'linux':
            try:
                install_progress = Spinner(message='Cleaning Up Packages ')

                for _ in range(1, 75):
                    time.sleep(0.007)
                    install_progress.next()

                proc = Popen('sudo apt-get -y autoremove'.split(),
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)

                proc.communicate(password.encode())

                for _ in range(1, 26):
                    time.sleep(0.007)
                    install_progress.next()

                click.echo('\n')
                click.echo(
                    click.style(
                        '🎉 Successfully Cleaned Turbocharge! 🎉',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)

        elif platform == 'win32':
            pass  # chocolatey auto removes files

        elif platform == 'darwin':
            try:
                install_progress = Spinner(message='Cleaning Up Packages ')

                for _ in range(1, 75):
                    time.sleep(0.007)
                    install_progress.next()

                proc = Popen('brew cleanup'.split(),
                             stdin=PIPE, stdout=PIPE, stderr=PIPE)

                for _ in range(1, 26):
                    time.sleep(0.007)
                    install_progress.next()

                click.echo('\n')
                click.echo(
                    click.style(
                        '🎉  Successfully Cleaned Turbocharge! 🎉',
                        fg='green'))

            except subprocess.CalledProcessError as e:
                click.echo(e.output)
                click.echo('An Error Occured During Installation...', err=True)


__version__ = '1.0.0b'
setup = Setup()


@click.group()
@click.version_option(__version__)
@click.pass_context
def cli(ctx):
    if platform == 'linux':
        if not isfile(f'/home/{getuser()}/config.tcc'):
            setup.setup()

    elif platform == 'win32':
        if not isfile(os.path.join(f"C:\\Users\\{getuser()}\Turbocharge", "config.tcc")):
            setup.setup()

    elif platform == 'darwin':
        if not isfile(f'/Users/{getuser()}/config.tcc'):
            setup.setup()


@cli.command()
@click.argument('package_list', required=True)
def install(package_list):
    '''
    Install A Specified Package(s)
    '''
    if platform in ['linux', 'darwin']:
        password = getpass('Enter your password: ')
    else:
        password = ''
        # otherwise the variable would be undefined..

    packages = package_list.split(',')
    turbocharge = Installer()

    click.echo('\n')

    os_bar = IncrementalBar('Getting Operating System...', max=1)
    os_bar.next()

    for package_name in packages:
        package_name = package_name.strip(' ')

        if platform == 'darwin':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_macos:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=devpackages_macos[package_name],
                    script=f"brew install {package_name}",
                    password="",
                    test_script=f"{package_name} --version",
                    tests_passed=[
                        f'{devpackages_macos[package_name]} Version']
                )
                # test _scirpt is just a string here..

            elif package_name in applications_macos:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=applications_macos[package_name],
                    script=f"brew cask install {package_name}",
                    password="",
                    test_script="",
                    tests_passed=[]
                )

            else:
                click.echo('\n')
                click.echo(click.style(
                    ':( Package Not Found! :( \n', fg='red'))
                suggestions = find(package_name)
                if suggestions != []:
                    click.echo('\n')
                    click.echo('Turbocharge found similar packages: \n')
                    for suggestion in suggestions:
                        click.echo(f'{suggestion} \n')
                else:
                    click.echo(
                        'Turbocharge couldn\'t find similar packages...')

        elif platform == 'linux':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_linux:
                show_progress(finding_bar)
                turbocharge.install_task(
                    devpackages_linux[package_name],
                    f'{apt_script} {package_name}',
                    password,
                    f'{package_name} --version',
                    [f'{devpackages_linux[package_name]} Version'])

            if package_name in applications_linux:
                show_progress(finding_bar)
                turbocharge.install_task(
                    applications_linux[package_name],
                    f'{snap_script} {package_name}',
                    password,
                    '',
                    [])

            if package_name == 'chrome':
                show_progress(finding_bar)
                try:
                    click.echo('\n')

                    password = getpass("Enter your password: ")

                    installer_progress = Spinner(
                        message='Installing Chrome...', max=100)

                    for _ in range(1, 75):
                        time.sleep(0.03)
                        installer_progress.next()

                    click.echo(
                        click.style(
                            '\n Chrome Will Take 2 to 4 Minutes To Download... \n',
                            fg='yellow'))

                    os.system(constant.chrome_link)

                    os.system(constant.chrome_move)

                    second = Popen(
                        constant.chrome_setup.split(),
                        stdin=PIPE,
                        stdout=PIPE,
                        stderr=PIPE
                    )
                    # Popen only accepts byte-arrays so you must encode the
                    # string
                    second.communicate(password.encode())

                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(
                        click.style('\n\n 🎉 Successfully Installed Chrome! 🎉 \n'))
                    # Testing the successful installation of the package
                    testing_bar = IncrementalBar('Testing package...', max=100)
                    for _ in range(1, 21):
                        time.sleep(0.045)
                        testing_bar.next()

                    for _ in range(21, 60):
                        time.sleep(0.045)
                        testing_bar.next()
                    for _ in range(60, 101):
                        time.sleep(0.03)
                        testing_bar.next()
                    click.echo('\n')
                    click.echo(
                        click.style(
                            'Test Passed: Chrome Launch ✅\n',
                            fg='green'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Installation...', err=True)

            if package_name == 'anaconda':
                show_progress(finding_bar)

                try:
                    installer_progress = Spinner(
                        message=f'Installing {package_name}...', max=100)
                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 35):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.anaconda_download)
                    for _ in range(35, 61):
                        time.sleep(0.01)
                        installer_progress.next()

                    os.system(constant.anaconda_setup)

                    for _ in range(61, 91):
                        time.sleep(0.01)
                        installer_progress.next()

                    os.system(constant.anaconda_PATH)

                    for _ in range(90, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(
                        click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Installation...', err=True)

            if package_name == 'miniconda':
                show_progress(finding_bar)
                try:
                    installer_progress = Spinner(
                        message=f'Installing {package_name}...', max=100)
                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 35):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.miniconda_download)
                    for _ in range(35, 61):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.miniconda_setup)
                    for _ in range(61, 91):
                        time.sleep(0.01)
                        installer_progress.next()
                    os.system(constant.miniconda_PATH)
                    for _ in range(90, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    # stdoutput = (output)[0].decode('utf-8')
                    click.echo(
                        click.style(f'\n\n 🎉 Successfully Installed {package_name}! 🎉 \n'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Installation...', err=True)

            elif (
                package_name not in devpackages_linux
                and package_name not in applications_linux
                and package_name != 'chrome'
                and package_name != 'anaconda'
            ):
                click.echo('\n')
                click.echo(click.style(':( Package Not Found! :(', fg='red'))
                suggestions = find(package_name)
                if suggestions != []:
                    click.echo('\n')
                    click.echo('Turbocharge found similar packages: \n')
                    for suggestion in suggestions:
                        click.echo(f'{suggestion} \n')
                else:
                    click.echo(
                        'Turbocharge couldn\'t find similar packages...')

        elif platform == 'win32':
            click.echo('\n')
            finding_bar = IncrementalBar(
                'Finding Requested Packages...', max=1)

            if package_name in devpackages_windows:
                show_progress(finding_bar)

                turbocharge.install_task(
                    package_name=devpackages_windows[package_name],
                    script=f"choco install {package_name} -y --force",
                    password="",
                    test_script=f"{package_name} --version",
                    tests_passed=[
                        f'{devpackages_windows[package_name]} Version']
                )

            elif package_name in applications_windows:
                show_progress(finding_bar)
                turbocharge.install_task(
                    package_name=applications_windows[package_name],
                    script=f"choco install {package_name} -y --force",
                    password="",
                    test_script="",
                    tests_passed=[]
                )

            else:
                click.echo('\n')
                click.echo(click.style(':( Package Not Found! :(', fg='red'))

                suggestions = find(package_name)
                if suggestions != []:
                    click.echo('\n')
                    click.echo('Turbocharge found similar packages: \n')
                    for suggestion in suggestions:
                        click.echo(f'{suggestion} \n')
                else:
                    click.echo(
                        'Turbocharge couldn\'t find similar packages...')


@cli.command()
@click.argument('package_list', required=True)
def remove(package_list):
    '''
    Uninstall Applications And Packages
    '''
    uninstaller = Uninstaller()

    if platform in ['linux', 'darwin']:
        password = getpass('Enter your password: ')
    else:
        password = ''

    packages = package_list.split(',')

    for package in packages:
        if platform == 'darwin':
            if package in devpackages_windows:
                uninstaller.uninstall(
                    f'brew uninstall {package}',
                    password="",
                    package_name=devpackages_macos[package]
                )
            elif package in applications_windows:
                uninstaller.uninstall(
                    f'brew cask uninstall {package}',
                    password="",
                    package_name=applications_macos[package]
                )

        elif platform == 'linux':
            if package in devpackages_linux:
                uninstaller.uninstall(
                    f'{apt_remove} {package}',
                    password,
                    package_name=devpackages_linux[package])

            if package in applications_linux:
                uninstaller.uninstall(
                    f'{snap_remove} {package}',
                    password,
                    package_name=applications_linux[package])

            if package == 'anaconda':
                try:
                    installer_progress = Spinner(
                        message=f'Uninstalling Anaconda...', max=100)
                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 75):
                        time.sleep(0.007)
                        installer_progress.next()

                    os.system(constant.anaconda_remove_folder)
                    os.system(constant.anaconda_remove_file)

                    with open('.bashrc', 'r') as file:
                        lines = file.read()

                    with open('.bashrc', 'w') as file:
                        for line in lines:
                            if 'anaconda' in line or 'miniconda' in line:
                                continue
                            else:
                                file.write(line)

                    # stdoutput = (output)[0].decode('utf-8')
                    for _ in range(75, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    click.echo(click.style(
                        f'\n\n 🎉 Successfully Uninstalled Anaconda! 🎉 \n', fg='green'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Uninstallation...', err=True)

            if package == 'miniconda':
                try:
                    installer_progress = Spinner(
                        message=f'Uninstalling Miniconda...', max=100)

                    # sudo requires the flag '-S' in order to take input from
                    # stdin
                    for _ in range(1, 75):
                        time.sleep(0.007)
                        installer_progress.next()

                    os.system(constant.miniconda_remove_folder)
                    os.system(constant.miniconda_remove_file)

                    with open('.bashrc', 'r') as file:
                        lines = file.read()

                    with open('.bashrc', 'w') as file:
                        for line in lines:
                            if 'anaconda' in line or 'miniconda' in line:
                                continue
                            else:
                                file.write(line)

                    # stdoutput = (output)[0].decode('utf-8')
                    for _ in range(1, 101):
                        time.sleep(0.01)
                        installer_progress.next()
                    click.echo(click.style(
                        f'\n\n 🎉 Successfully Uninstalled Miniconda! 🎉 \n', fg='green'))
                except subprocess.CalledProcessError as e:
                    click.echo(e.output)
                    click.echo(
                        'An Error Occurred During Uninstallation...', err=True)

        elif platform == 'win32':
            if package in devpackages_windows:
                uninstaller.uninstall(
                    f'choco uninstall {package} --force -y',
                    password="",
                    package_name=devpackages_windows[package]
                )

            elif package in applications_windows:
                uninstaller.uninstall(
                    f'choco uninstall {package} --force -y',
                    password="",
                    package_name=applications_windows[package]
                )


@cli.command()
@click.argument('package_list', required=True)
def update(package_list):
    '''
    Update Applications And Packages
    '''
    updater = Updater()

    if platform in ['linux', 'darwin']:
        password = getpass('Enter your password: ')
    else:
        password = ''

    packages = package_list.split(',')

    for package in packages:
        if platform == "darwin":
            if package in devpackages_macos:
                updater.updatepack(package, password)

            if package in applications_macos:
                updater.updateapp(package, password)

            else:
                return

        elif platform == "linux":
            if package in devpackages_linux:
                updater.updatepack(package, password)

            if package in applications_linux:
                updater.updateapp(package, password)

            else:
                return
        elif platform == "win32":
            if package in devpackages_windows:
                updater.updatepack(package, "")

            if package in applications_windows:
                updater.updateapp(package, "")

            else:
                return


@cli.command()
@click.argument('hyperpack_list', required=True)
def hyperpack(hyperpack_list):
    '''
    Install Large Packs Of Applications And Packages
    '''
    os_bar = IncrementalBar('Getting Operating System...', max=1)
    os_bar.next()

    installer = Installer()
    updater = Updater()
    cleaner = Uninstaller()

    hyperpacks = hyperpack_list.split(',')

    password = ""

    if platform in ['linux', 'darwin']:
        password = getpass('Enter your password: ')
        click.echo('\n')

        password_bar = IncrementalBar('Verifying Password...', max=1)

        exitcode = is_password_valid(password)

        if exitcode == 1:
            click.echo('Wrong Password Entered... Aborting Installation!')
            return

        password_bar.next()

    click.echo('\n')
    for hyperpack in hyperpacks:
        if platform == 'linux':
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            # Installing Required Packages
            for package in packages:
                installer.install_task(
                    devpackages_linux[package],
                    f'sudo -S apt-get install -y {package}',
                    password,
                    f'{package} --version',
                    [f'{devpackages_linux[package]} Version'])

            # Installing Required Applications
            for app in apps:
                installer.install_task(
                    applications_linux[app],
                    f'sudo -S snap install --classic {app}',
                    password,
                    '',
                    [])

            # Updating Required Packages
            for package in packages:
                updater.updatepack(package, password)

            for app in apps:
                updater.updateapp(app, password)

            cleaner.clean(password)

        elif platform == 'win32':
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            for package in packages:
                installer.install_task(
                    package_name=devpackages_windows[package],
                    script=f'choco install {package} -y',
                    password="",
                    test_script=f'{package} --version',
                    tests_passed=[f'{devpackages_windows[package]} Version']
                )

            for package in packages:
                updater.updatepack(package, password="")

            for app in apps:
                installer.install_task(
                    package_name=applications_windows[app],
                    script=f'choco install {app} -y',
                    password="",
                    test_script='',
                    tests_passed=[]
                )

            for app in apps:
                updater.updateapp(app, password="")
        elif platform == 'darwin':
            hyper_pack = hyperpkgs[hyperpack]

            packages = hyper_pack.packages.split(',')
            apps = hyper_pack.applications.split(',')

            for package in packages:
                installer.install_task(
                    package_name=devpackages_macos[package],
                    script=f'brew install {package}',
                    password="",
                    test_script=f'{package} --version',
                    tests_passed=[f'{devpackages_macos[package]} Version']
                )

            for package in packages:
                updater.updatepack(package, password="")

            for app in apps:
                installer.install_task(
                    package_name=applications_macos[app],
                    script=f'brew cask install {app}',
                    password="",
                    test_script='',
                    tests_passed=[]
                )

            for app in apps:
                updater.updateapp(app, password="")


@cli.command()
@click.argument('text', required=True)
def search(text):
    '''
    Search For A Package To Install
    '''
    click.echo(f'Searching for packages...')

    suggestions = find(text)

    for suggestion in suggestions:
        click.echo(f'{suggestion} \n')


@cli.command()
def clean():
    '''
    Remove Junk Packages Which Are Not Needed
    '''
    if platform in ['linux', 'darwin']:
        uninstaller = Uninstaller()
        password = getpass('Enter your password: ')
        uninstaller.clean(password)

    elif platform == 'win32':
        arr = ['|', "/", "-", "\\"]

        slen = len(arr)

        print('Cleaning Your PC...')

        for i in range(1, 60):
            time.sleep(0.04)
            print(arr[i % slen], end='\r')


@cli.command()
def list():
    '''
    Applications And Packages TurboCharge Supports
    '''
    if platform == 'linux':
        click.echo(click.style(display_list_linux, fg='white'))

    elif platform == 'win32':
        click.echo(click.style(display_list_windows, fg='white'))

    elif platform == 'darwin':
        click.echo(click.style(display_list_macos, fg='white'))


@cli.command()
def local():
    '''
    Lists all the installed packages.
    '''

    if platform == 'darwin':
        packages = []
        applications = []

        lines = None

        with open(f'/Users/{getuser()}/config.tcc', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            line.split()
            try:
                package_name = line.split()[0]
            except IndexError:
                continue
            try:
                package_type = line.split()[2]
            except IndexError:
                continue
            if package_type == 'p':
                packages.append(package_name)

            if package_name == 'a':
                applications.append(package_name)

        click.echo('Packages : \n')

        if packages == []:
            click.echo('Turbocharge couldn\'t find any packages installed.')

        else:
            for package in packages:
                click.echo(package)

        click.echo('Applications : \n')

        if applications == []:
            click.echo('Turbocharge couldn\'t find any applications installed.')
        else:
            for app in applications:
                click.echo(app)

    elif platform == 'linux':
        packages = []
        applications = []

        lines = None

        with open(f'/home/{getuser()}/config.tcc', 'r') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            line.split()
            try:
                package_name = line.split()[0]
            except IndexError:
                continue
            try:
                package_type = line.split()[2]
            except IndexError:
                continue

            if package_type == 'a':
                applications.append(package_name)

            elif package_type == 'p':
                packages.append(package_name)

        click.clear()
        click.echo('Packages : \n')

        if packages != []:
            for package in packages:
                click.echo(package + '\n')

        else:
            click.echo('Turbocharge couldn\'t find any packages installed.')

        click.echo('Applications : \n')

        if applications == []:
            click.echo(
                'Turbocharge couldn\'t find any applications installed. \n')

        else:
            for app in applications:
                click.echo(app + '\n')

    elif platform == 'win32':
        cmd = run('clist -l', stdout=PIPE, stderr=PIPE)

        output = cmd.stdout.decode()

        lines = output.split('\n')

        packages = [
            line
            for line in lines
            if 'Chocolatey' not in line
            and 'chocolatey' not in line
            and 'packages installed' not in line
        ]


        result = "Packages installed:\n"

        for p in packages:
            result += p
            result += "\n"

        click.echo(result)

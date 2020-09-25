from getpass import getuser
from HyperPack import HyperPack

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

#     'librepcb' : 'Libre PCB', Doesn't exist for chocolatey they are too lazy
#   'powershell' : 'Powershell', Comes preinstalled with Windows.
applications_windows = {
    'androidstudio': 'Android Studio',
    'atom' : 'Atom',
    'blender' : 'Blender',
    'brackets' : 'Brackets',
    'clion-ide' : 'C Lion',
    'discord' : 'Discord',
    'datagrip' : 'Data Grip',
    'libreoffice-fresh' : 'Libre Office',
    'opera' : 'Opera',
    'webstorm' : 'Web Storm',
    'pycharm-community': 'Pycharm Community',
    'sublimetext3.app': 'Sublime Text',
    'vscode' : 'Visual Studio Code',
    'vscode-insiders.install' : 'Visual Studio Code Insiders',
    'eclipse' : 'Eclipse',
    'kotlinc' : 'Kotlin',
    'goland' : 'Go Land',
    'rubymine' : 'RubyMine',
    'figma' : 'Figma',
}

#     'zsh': 'Zsh', Not available on windows using chocolatey...
# 'ntop.portable' : 'NTop',  We could use this.... totally new. instead of htop
devpackages_windows = {
    'git': 'Git',
    'curl': 'Curl',
    'docker': 'Docker',
    'nodejs': 'Npm',
    'emacs': 'Emacs',
    'neovim': 'Neo Vim',
    'vim': 'Vim',
    # 'htop': 'Htop',
    'sqlite': 'Sqlite',
    'tldr': 'Tldr',
    'jq': 'JQ',
    # 'ncdu': 'Ncdu', Does not exist.
    # 'taskwarrior': 'Task Warrior', Does not exist
    # 'tmux': 'Tmux', Does not exist, possible counterpart is fzf
    # 'patchelf': 'Patchelf', not for windows
    'golang': 'Go-Lang',
    'rust': 'Rust',
    # 'zlib': 'Z-Lib', Rejected on Chocolatey .... some issue going on...
    # 'kakoune': 'Kakoune', no windows possibility
    # 'autojump': 'Autojump', not directly... can do from direct github repo using python
    'pass': 'Pass',
    'qtpass': 'QTpass'
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
chrome_setup = 'sudo -S apt-get install -y ./google-chrome-stable_current_amd64.deb'

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
___________________________________________
| Applications       |Duration||   Size   |
-------------------------------------------
| android-studio     |   5m   || 840.0 MB |
| atom               |   2m   || 224.8 MB |
| blender            |   2m   || 187.7 MB |
| brackets           |   1m   || 109.6 MB |
| clion-ide          |   3m   || 502.0 MB |
| chrome             |   2m   || 70.2  MB |
| datagrip           |   2m   || 356.8 MB |
| discord            |   1m   || 60.1  MB |
| eclipse            |   2m   || 220.3 MB |
| figma              |   2m   || 96.4  MB |
| libreoffice-fresh  |   1m   || 25.0  MB |
| opera              |   1m   || 64.2 MB  |
| pycharm-community  |   3m   || 372.1 MB |
| powershell         |   1m   || 62.5  MB |
| rubymine           |   3m   || 363.2 MB |
| sublimetext3       |   1m   || 70.8 MB  |
| webstorm           |   3m   || 343.8 MB |
| vscode             |   2m   || 162.5 MB |
| vscode-insiders    |   2m   || 153.3 MB |
-------------------------------------------
________________
| Package      |
----------------
|  anaconda    |
|  curl        |
|  docker      |
|  emacs       |
|  git         |
|  golang      |
|  jq          |
|  kotlin      |
|  miniconda   |
|  neovim      |
|  nodejs      |
|  pass        |
|  qtpass      |
|  rust        |
|  sqlite      |
|  tldr        |
|  vim         |
----------------
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

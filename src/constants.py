from getpass import getuser
from HyperPack import HyperPack

applications = {
    'android-studio': 'Android Studio',
    'atom': 'Atom',
    'blender': 'Blender',
    'brackets': 'Brackets',
    'clion': 'C Lion',
    'discord': 'Discord',
    'datagrip': 'Data Grip',
    'libreoffice': 'Libre Office',
    'librepcb': 'Libre PCB',
    'opera': 'Opera',
    'webstorm': 'Web Storm',
    'pycharm': 'Pycharm Community',
    'sublime-text': 'Sublime Text',
    'code': 'Visual Studio Code',
    'code-insiders': 'Visual Studio Code Insiders',
    'eclipse': 'Eclipse',
    'powershell': 'Powershell',
    'kotlin': 'Kotlin',
    'goland': 'Go Land',
    'rubymine': 'RubyMine',
    'figma-linux': 'Figma',
    'slack': 'Slack',
    'obs-studio': 'OBS Studio',
    'postman': 'Postman',
    'flutter': 'Flutter',
    'inkscape': 'Inkscape',
    'gimp': 'GIMP',
    '1password-linux': '1Password',
    'skype': 'Skype',
    'todoist': 'Todoist',
    'spotify': 'Spotify',
    'beekeeper-studio': 'BeeKeeper-Studio',
    'notepad-plus-plus': 'Notepad++',
    'gitkraken': 'Gitkraken',
    'cacher': 'Cacher',
    'space': 'Space',
    'intellij-idea-educational': 'IntelliJ Idea Educational',
    'phpstorm': 'PHPStorm',
}

devpackages = {
    'ansible': 'Ansible',
    'git': 'Git',
    'git-secret': 'Git-secret',
    'curl': 'Curl',
    'docker': 'Docker',
    'npm': 'Npm',
    'zsh': 'Zsh',
    'emacs': 'Emacs',
    'neovim': 'Neo Vim',
    'vim': 'Vim',
    'htop': 'Htop',
    'sqlite': 'Sqlite',
    'tldr': 'Tldr',
    'jq': 'JQ',
    'ncdu': 'Ncdu',
    'taskwarrior': 'Task Warrior',
    'tmux': 'Tmux',
    'patchelf': 'Patchelf',
    'golang': 'Go-Lang',
    'rust': 'Rust',
    'zlib': 'Z-Lib',
    'kakoune': 'Kakoune',
    'autojump': 'Autojump',
    'pass': 'Pass',
    'qtpass': 'QTpass',
    'ruby-full': 'Ruby',
    'julia': 'Julia',
    'librecad': 'LibreCAD',
    'krita': 'Krita',
    'chromium-browser': 'Chromium',
    'restic': 'Restic',
    'steam': 'Steam',
    'synaptic': 'Synaptic',
    'ubuntu-cleaner': 'Ubuntu-cleaner'
}

hyperpkgs = {
    'essential': HyperPack('git,curl,npm,zsh,vim', 'code,atom,sublime-text'),
    'office': HyperPack('sqlite', 'libreoffice')
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


display_list = '''
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
| chromium                       |   1m   || 169.9 MB |
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

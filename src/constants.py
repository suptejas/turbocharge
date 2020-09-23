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
}

devpackages = {
    'git': 'Git',
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
    'qtpass': 'QTpass'
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
__________________________________________
| Applications      |Duration||   Size   |
------------------------------------------
| android-studio    |   5m   || 840.0 MB |
| atom              |   2m   || 224.8 MB |
| blender           |   2m   || 187.7 MB |
| brackets          |   1m   || 109.6 MB |
| clion             |   3m   || 502.0 MB |
| chrome            |   2m   || 70.2  MB |
| datagrip          |   2m   || 356.8 MB |
| discord           |   1m   || 60.1  MB |
| eclipse           |   2m   || 220.3 MB |
| figma-linux       |   2m   || 96.4  MB |
| libreoffice       |   1m   || 25.0  MB |
| librepcb          |   1m   || 98.8  MB |
| opera             |   1m   || 64.2 MB  |
| pycharm           |   3m   || 372.1 MB |
| powershell        |   1m   || 62.5  MB |
| rubymine          |   3m   || 363.2 MB |
| sublime-text      |   1m   || 70.8 MB  |
| webstorm          |   3m   || 343.8 MB |
| vscode            |   2m   || 162.5 MB |
| vscode-insiders   |   2m   || 153.3 MB |
------------------------------------------
________________
| Package      |
----------------
|  anaconda    |
|  autojump    |
|  curl        |
|  docker      |
|  emacs       |
|  git         |
|  golang      |
|  htop        |
|  jq          |
|  kotlin      |
|  kakoune     |
|  miniconda   |
|  ncdu        |
|  neovim      |
|  npm         |
|  pass        |
|  patchelf    |
|  qtpass      |
|  rust        |
|  sqlite      |
|  taskwarrior |
|  tldr        |
|  tmux        |
|  vim         |
|  zsh         |
|  zlib        |
----------------
_______________________________________________________________________
| HyperPacks  |  Content                                              |
-----------------------------------------------------------------------
|  essential  |  git, curl, npm, zsh, vim, code, atom, sublime-text   |
|  office     |  sqlite, libreoffice                                  |
-----------------------------------------------------------------------
'''
import os
import time

import git

ZSH_UPDATE_FILE = os.path.expanduser('~/.zsh-update')
EPOCH_TARGET = -1


def _current_epoch():
    return int(time.time() / (60 * 60 * 24))


def _update_zsh_update():
    with open(ZSH_UPDATE_FILE, 'w') as f:
        f.write('LAST_EPOCH={}\n'.format(_current_epoch()))


def _upgrade_zsh():
    _upgrade_script()
    _update_zsh_update()


class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


def _upgrade_script():
    # Use colors, but only if connected to a terminal, and that terminal
    # supports them.
    """
        if which tput >/dev/null 2>&1; then
            ncolors=$(tput colors)

    if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
      RED="$(tput setaf 1)"
      GREEN="$(tput setaf 2)"
      YELLOW="$(tput setaf 3)"
      BLUE="$(tput setaf 4)"
      BOLD="$(tput bold)"
      NORMAL="$(tput sgr0)"
    """

    print bcolors.OKBLUE + "Upgrading Dotfiles from github.com/bufordsharkley/dotfiles" + bcolors.ENDC
    #gitpath = os.path.join(os.environ['DOTFILES'], 'dotfiles')
    repo = git.Repo(os.environ['DOTFILES'])
    if repo.is_dirty():
        print 'would you like to push?'
        repo.git.add(all=True)
        print repo.git.status()
        while True:
            key = raw_input('Type Y to commit and push these changes (d for diff):').strip().lower()
            if key == 'y':
                commit_message = raw_input('Commit message?').strip()
                repo.index.commit(commit_message)
                _push_to_origin(repo)
            elif key == 'd':
                print repo.git.diff(cached=True, color=True)
            else:
                break
    else:
        repo.remotes.origin.pull()

def _push_to_origin(repo):
    while True:
        try:
            a = repo.remotes.origin.push()
            print a
            return
        except git.exc.GitCommandError:
            print bcolors.FAIL + 'You are a bad typer.' + bcolors.ENDC


def _parse_zsh_update():
    file_contents = open(ZSH_UPDATE_FILE).read()
    try:
      return int(file_contents.split('=')[1])
    except ValueError:
      return 0


if __name__ == "__main__":
    if os.path.exists(ZSH_UPDATE_FILE):
        epoch = _parse_zsh_update()
        diff = _current_epoch() - epoch
        if diff > EPOCH_TARGET:
            _upgrade_zsh()
    else:
        _update_zsh_update()

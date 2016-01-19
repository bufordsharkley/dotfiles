import os
import time

import git

ZSH_UPDATE_FILE = os.path.expanduser('~/.zsh-update')
DAYS_BETWEEN_CHECKS = 1
COMMIT_QUERY = 'Type Y to commit and push these changes (d for diff):'


def _current_epoch_days():
    return int(time.time() / (60 * 60 * 24))


def _update_zsh_update():
    with open(ZSH_UPDATE_FILE, 'w') as f:
        f.write('LAST_EPOCH={}\n'.format(_current_epoch_days()))


def print_color(message, color):
    colors = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'FAIL': '\033[91m',
        'normal': '\033[0m',
    }
    #HEADER = '\033[95m'
    #WARNING = '\033[93m'
    #BOLD = '\033[1m'
    #UNDERLINE = '\033[4m'
    print colors[color] + message + colors['normal']


def _upgrade_script():
    # TODO - use colors only if connected to a terminal, and colors supported
    print_color('Upgrading Dotfiles from github.com/bufordsharkley/dotfiles',
                'blue')
    repo = git.Repo(os.environ['DOTFILES'])
    if repo.is_dirty():
        print 'would you like to push?'
        repo.git.add(all=True)
        print repo.git.status()
        while True:
            key = raw_input(COMMIT_QUERY).strip().lower()
            if key == 'y':
                commit_message = raw_input('Commit message:\n').strip()
                repo.index.commit(commit_message)
                _push_to_origin(repo)
                break
            elif key == 'd':
                print repo.git.diff(cached=True, color=True)
            else:
                break
    else:
        repo.remotes.origin.pull()


def _push_to_origin(repo):
    while True:
        try:
            print repo.remotes.origin.push()
            return
        except git.exc.GitCommandError:
            print_color('You are a bad typer.', 'red')


def _fetch_time_of_last_update():
    file_contents = open(ZSH_UPDATE_FILE).read()
    try:
        return int(file_contents.split('=')[1])
    except ValueError:
        return 0


if __name__ == '__main__':
    if os.path.exists(ZSH_UPDATE_FILE):
        last_update = _fetch_time_of_last_update()
        diff = _current_epoch_days() - last_update
        if diff > DAYS_BETWEEN_CHECKS:
            _upgrade_script()
            _update_zsh_update()
    else:
        _update_zsh_update()

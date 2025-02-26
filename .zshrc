# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Set name of the theme to load.
# Look in ~/.oh-my-zsh/themes/
ZSH_THEME="agnoster"

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

[[ -a "/etc/zsh_command_not_found" ]] && . /etc/zsh_command_not_found

# User configuration

export PATH="/home/mgm/repos/money:/usr/local/heroku/bin:/home/mgm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/texlive/2018/bin/x86_64-linux/:/home/mgm/.poetry/bin::/snap/bin:/home/mgm/.local/bin"
export DOTFILES=$HOME/repos/dotfiles

source $ZSH/oh-my-zsh.sh

prython() {
    if [[ -z "$@" ]]; then
        if [[ -z "$VIRTUAL_ENV" ]]; then
            command ipython3 -i ~/.ipythonrc
        else
            command python3
        fi
    else
        command python3 "$@"
    fi
}

alias envpython='/usr/bin/env python'
alias rm='rm -i'

export PYTHONPATH=$PYTHONPATH:.:/home/mgm/repos/kzsu-web

# for entering a dir immediately after making it!
function mkdircd () { mkdir -p "$@" && eval cd "\"\$$#\""; }
[ -z "$TMUX" ] && export TERM=xterm-256color
# vim it up:
bindkey -v
bindkey -M viins 'jk' vi-cmd-mode
bindkey -M viins 'JK' vi-cmd-mode
bindkey "^R" history-incremental-search-backward

function beginning-and-insert {
  zle beginning-of-line
  zle vi-insert
}
function end-and-insert {
  zle end-of-line
  zle vi-insert
}

zle -N beginning-and-insert
zle -N end-and-insert

bindkey -M vicmd 'ij' beginning-and-insert
bindkey -M vicmd 'IJ' beginning-and-insert
bindkey -M vicmd 'af' end-and-insert
bindkey -M vicmd 'AF' end-and-insert

bindkey "^?" backward-delete-char
bindkey -M vicmd "^K" run-help
bindkey -M viins "^K" run-help

if [[ -f ~/.zshrc_extra ]]; then
    source ~/.zshrc_extra
fi

if [[ -f /usr/local/bin/thefuck ]]; then
  eval $(thefuck --alias)
fi

man() {
    env \
        LESS_TERMCAP_mb=$(printf "\e[1;31m") \
        LESS_TERMCAP_md=$(printf "\e[1;31m") \
        LESS_TERMCAP_me=$(printf "\e[0m") \
        LESS_TERMCAP_se=$(printf "\e[0m") \
        LESS_TERMCAP_so=$(printf "\e[1;44;33m") \
        LESS_TERMCAP_ue=$(printf "\e[0m") \
        LESS_TERMCAP_us=$(printf "\e[1;32m") \
            man "$@"
}

alias doom='python $DOTFILES/scripts/doom.py'
alias clipboard='xclip -sel clip'

mplayerbg() { mplayer "$@" </dev/null >/dev/null 2>&1 & }

if [[ -z $PIPENV_ACTIVE ]]; then
  python3 $DOTFILES/scripts/doom.py
  todo-txt lsp | head
  # Previous methods to show how many terminals open:
  #echo $(ps ax | grep zsh | wc -l | cut -f1 -d' ')
  #if (( $(ps ax | grep zsh | wc -l) > 11)); then
fi

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
pyenv virtualenvwrapper

alias gam="/home/mgm/bin/gam7/gam"

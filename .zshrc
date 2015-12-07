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

export PATH="/home/mgm/repos/money:/usr/local/heroku/bin:/home/mgm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
export DOTFILES=$HOME/repos/dotfiles

source $ZSH/oh-my-zsh.sh

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."
alias .......="cd ../../../../../.."
alias ........="cd ../../../../../../.."
alias .........="cd ../../../../../../../.."
alias ..........="cd ../../../../../../../../.."
alias ...........="cd ../../../../../../../../../.."
alias ............="cd ../../../../../../../../../../.."
alias .............="cd ../../../../../../../../../../../.."
alias ..............="cd ../../../../../../../../../../../../.."

python() {
    if [[ -z "$@" ]]; then
        if [[ -z "$VIRTUAL_ENV" ]]; then
            command ipython -i ~/.ipythonrc
        else
            command python
        fi
    else
        command python "$@"
    fi
}

alias envpython='/usr/bin/env python'

export PYTHONPATH=$PYTHONPATH:/home/mgm/repos/kzsu-web

# for entering a dir immediately after making it!
function mkdircd () { mkdir -p "$@" && eval cd "\"\$$#\""; }
[ -z "$TMUX" ] && export TERM=xterm-256color
# vim it up:
bindkey -v
bindkey -M viins 'jk' vi-cmd-mode
bindkey -M viins 'JK' vi-cmd-mode

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

if [[ -f ~/.zshrc_extra ]]; then
    source ~/.zshrc_extra
fi

RPROMPT='${vim_mode}'

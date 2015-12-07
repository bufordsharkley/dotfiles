#!/usr/bin/env zsh

zmodload zsh/datetime

function _current_epoch() {
  echo $(( $EPOCHSECONDS / 60 / 60 / 24 ))
}

function _update_zsh_update() {
  echo "LAST_EPOCH=$(_current_epoch)" >! ~/.zsh-update
}

function _upgrade_zsh() {
  env ZSH=$ZSH /bin/sh $ZSH/tools/upgrade.sh
  # update the zsh file
  _update_zsh_update
}

epoch_target=1 # 1 day in between this stuff

if [ -f ~/.zsh-update ]
then
  . ~/.zsh-update

  if [[ -z "$LAST_EPOCH" ]]; then
    _update_zsh_update && return 0;
  fi

  epoch_diff=$(($(_current_epoch) - $LAST_EPOCH))
  if [ $epoch_diff -gt $epoch_target ]
  then
      _upgrade_zsh
  fi
else
  # create the zsh file
  _update_zsh_update
fi

# Use colors, but only if connected to a terminal, and that terminal
# supports them.
if which tput >/dev/null 2>&1; then
    ncolors=$(tput colors)
fi
if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
  RED="$(tput setaf 1)"
  GREEN="$(tput setaf 2)"
  YELLOW="$(tput setaf 3)"
  BLUE="$(tput setaf 4)"
  BOLD="$(tput bold)"
  NORMAL="$(tput sgr0)"
else
  RED=""
  GREEN=""
  YELLOW=""
  BLUE=""
  BOLD=""
  NORMAL=""
fi

printf "${BLUE}%s${NORMAL}\n" "Upgrading Dotfiles from github.com/bufordsharkley/dotfiles"
cd "$DOTFILES"
git status --porcelain >& /dev/null
if [ $? -eq 0 ]; then
  echo 'would you like to push?'
  git aa
  git s
  echo "Type Y to commit and push these changes:"
  read line
  if [ "$line" = Y ] || [ "$line" = y ]; then
    git commit
    if [ $? -ne 0 ]; then
      echo "not commiting"
      exit
    fi
    until `git push`
    do
      printf "${RED}%s${NORMAL}\n" 'You are a bad typer.'
    done
  fi
else
  git pull
fi

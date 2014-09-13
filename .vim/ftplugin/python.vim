setlocal tabstop=4
setlocal shiftwidth=4
setlocal expandtab
setlocal autoindent
match ErrorMsg '\%>80v.\+'
setlocal smarttab
setlocal cindent
highlight ExtraWhitespace ctermbg=red guibg=red
" Show trailing whitepace and spaces before a tab:
:autocmd Syntax * syn match ExtraWhitespace /\s\+$\| \+\ze\t/

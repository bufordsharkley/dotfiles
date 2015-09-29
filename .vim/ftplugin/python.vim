setlocal tabstop=2
setlocal shiftwidth=2
setlocal expandtab
setlocal autoindent
match ErrorMsg '\%>80v.\+'
setlocal smarttab
setlocal cindent
"autocmd nnoremap <buffer> <F5> :exec '!python' shellescape(@%, 1)<cr>

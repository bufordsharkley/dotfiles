setlocal tabstop=4
setlocal shiftwidth=4
setlocal expandtab
setlocal autoindent
match ErrorMsg '\%>80v.\+'
setlocal smarttab
setlocal cindent
"autocmd nnoremap <buffer> <F5> :exec '!python' shellescape(@%, 1)<cr>

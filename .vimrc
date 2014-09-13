nmap <c-s> :w<CR>
imap <c-s> <Esc>:w<CR>a
filetype plugin on
set ic
set hls is
nnoremap _ mao<esc>`a
nnoremap + maO<esc>`a
" Press F4 to toggle highlighting on/off, and show current value.
:noremap <F4> :set hlsearch! hlsearch?<CR>
" The best: jk for Esc replacement. 
:imap jk <Esc>
execute pathogen#infect()
syntax enable
set background=dark
let g:solarized_termcolors=16
colorscheme solarized

filetype plugin on
" searching stuff: ignore case and show all matches
set ic
set hls
" inserting blank lines above and below: I'm a fan.
nnoremap _ mao<esc>`a
nnoremap + maO<esc>`a
" f4 to toggle highlighting
:noremap <F4> :set hlsearch! hlsearch?<CR>
" The best: jk for Esc replacement. 
:imap jk <Esc>
" all the pathogen stuff: TODO make it work on any machine, whether
" or not pathogen is installed
"execute pathogen#infect()
syntax enable
set background=dark
"let g:solarized_termcolors=16
"colorscheme solarized

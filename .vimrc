" Pathogen
filetype off " Pathogen needs to run before plugin indent on
call pathogen#infect()
filetype plugin indent on
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
:imap JK <Esc>
syntax enable
set t_Co=256
"let g:solarized_termcolors=256
if has('gui_running')
    set background=dark
else
    set background=dark
endif
colorscheme solarized
"let all files use 4-space tabs. see if I care.
setlocal tabstop=4
setlocal shiftwidth=4
setlocal expandtab
let g:SuperTabDefaultCompletionType = "context"
let g:jedi#popup_on_dot = 0
python from powerline.vim import setup as powerline_setup
python powerline_setup()
python del powerline_setup
set laststatus=2

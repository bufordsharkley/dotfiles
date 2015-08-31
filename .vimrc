"GOAL: to have vim usable without pressing two keys at once, almost ever.
"It is the caps lock way.
"first, some to-be-sure stuff:
set nocompatible
set encoding=utf-8
" now fire up pathogen:
filetype off " Pathogen needs to run before plugin indent on
call pathogen#infect()
filetype plugin indent on
" searching stuff: ignore case and show all matches
set ic
set hls
set relativenumber
" the great un-capitalizer
noremap A a
noremap B b
noremap C c
noremap D d
noremap E e
noremap F f
noremap G g
noremap H h
noremap I i
noremap J j
noremap K k
noremap L l
noremap M m
noremap N n
noremap O o
noremap P p
noremap Q q
noremap R r
noremap S s
noremap T t
noremap U u
noremap V v
noremap X x
noremap Y y
noremap Z z
" fix -- add back capitals I use:
noremap <c-j> J
noremap <c-k> K
noremap <c-f> F
noremap <c-w> W
nnoremap oo O
nnoremap oi o
nnoremap OO O
nnoremap OI o
nnoremap ee E
nnoremap gh G
nnoremap GH G
noremap <c-d> D
noremap <c-n> N
" allow for insert and end without shift key.
nnoremap aa A
nnoremap af a
nnoremap AA A
nnoremap AF a
nnoremap ii I
nnoremap ij i
nnoremap II I
nnoremap IJ i
nnoremap <leader>A A
" inserting blank lines above and below: I'm a fan.
nnoremap _ mao<esc>`a
nnoremap + maO<esc>`a
:noremap <space> viw
:vnoremap <space> <Esc>
" f4 to toggle highlighting
:noremap <F4> :set hlsearch! hlsearch?<CR>
" The best: jk for Esc replacement. 
:inoremap jk <Esc>
:inoremap JK <Esc>
" execute python with f5:
autocmd FileType python nnoremap <buffer> <F5> :exec '!python' shellescape(@%, 1)<cr>
syntax enable
set t_Co=256
"let g:solarized_termcolors=256
if has('gui_running')
    set background=dark
else
    set background=dark
endif
"colorscheme solarized TODO - figure out how to use without headaches
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

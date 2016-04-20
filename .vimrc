" GOAL to have vim usable without pressing two keys at once, almost ever.
"It is the caps lock way.
" still a work in progress (but let me know if you find anybody else trying
" for this same concept)

"first, some to-be-sure stuff:

set nocompatible
set encoding=utf-8
set title
" now fire up pathogen:
filetype off " Pathogen needs to run before plugin indent on
call pathogen#infect()
filetype plugin indent on
" searching stuff: ignore case and show all matches
set ic
set hls
set number
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
" The best: jk for Esc replacement.
inoremap jk <esc>
inoremap JK <esc>
vnoremap jk <esc>
vnoremap JK <esc>
" fix -- add back capitals I use:
noremap <c-j> J
noremap <c-k> K
noremap <c-f> F
nnoremap oi O
nnoremap oo o
nnoremap OI O
nnoremap OO o
nnoremap ee E
nnoremap gh G
nnoremap GH G
vnoremap gh G$
vnoremap GH G$
noremap <c-d> D
" I don't want to use undo in visual-- cap is better:
vnoremap U U
vnoremap u U
" And same for reaching tilde:
vnoremap ` ~
vnoremap f $
vnoremap F $
vnoremap a 0
vnoremap A 0

nnoremap S %
" replace $ and 0 (which I hate pressing):
noremap ef $
noremap EF $
noremap ee e
noremap EE e
noremap bb b
noremap BB b
noremap bf 0
noremap BF 0
" change
noremap cc c
noremap CC c
noremap cf C
noremap CF C
" allow for insert and end without shift key.
nnoremap aa a
nnoremap AA a
nnoremap as a
nnoremap AS a
nnoremap ad a
nnoremap af A
nnoremap AD a
nnoremap AF A
nnoremap ii i
nnoremap II i
nnoremap ij I
nnoremap IJ I
" copying paragraph:"
" nnoremap cp yap<S-}>p  -- good, but cp is a bad shortcut b/c of parens
" inserting blank lines above and below: I'm a fan.
nnoremap _ mao<esc>`a
nnoremap + maO<esc>`a
" moving lines around.
nnoremap - ddp
nnoremap = kddpk
noremap <space> viw
vnoremap <space> <Esc>
" f4 to toggle highlighting
:noremap <F3> :set paste<CR>"*p:set nopaste<CR>
:noremap <F4> :set hlsearch! hlsearch?<CR>
"windows: allowing switching easily:
noremap <C-K> <C-W>k<C-W>_
noremap <C-L> <C-W>l<C-W>_
noremap <C-H> <C-W>h<C-W>_
noremap <C-A><C-A> <C-W><C-W>
" execute python with f5:
augroup filetype_python
    autocmd!
    autocmd FileType python nnoremap <buffer> <F5> :exec '!python' shellescape(@%, 1)<cr>
    autocmd FileType python nnoremap <buffer> <F6> :exec '!make unittest' shellescape(@%, 1)<cr>
    autocmd FileType python nnoremap <buffer> <F9> :exec '!make test' shellescape(@%, 1)<cr>
augroup END

syntax enable
set t_Co=256
cnoreabbrev W w
set background=dark
"All files in directory as current buffer:
cnoremap %% <C-R>=expand('%:h').'/'<cr>
"let all files use 2-space tabs. see if I care.
set tabstop=2
set shiftwidth=2
set expandtab
let g:SuperTabDefaultCompletionType = "context"
let g:jedi#popup_on_dot = 0
python from powerline.vim import setup as powerline_setup
python powerline_setup()
python del powerline_setup
set laststatus=2
" parentheses deletion as p, etc
onoremap p i(
" File navigation should have line numbers:
let g:netrw_bufsettings = 'noma nomod nu relativenumber nobl nowrap ro'
" Show trailing whitepace and spaces before a tab:
highlight ExtraWhitespace ctermbg=red guibg=red
autocmd Syntax * syn match ExtraWhitespace /\s\+$\| \+\ze\t/
" easy opening of this file:
noremap evev :vsplit $MYVIMRC<cr>
" meta-referential: source this very file
nnoremap svsv :write<cr>:source $MYVIMRC<cr>
" change the tabs when needed
noremap zvzv :set tabstop=2<cr>:set shiftwidth=2<cr>
" This disables ELP, allowing :E for explore
let g:loaded_logipat = 1
let hostfile=$HOME . '/.vimrc-specific'
if filereadable(hostfile)
    exe 'source ' . hostfile
endif

call plug#begin()

Plug 'tpope/vim-sensible'
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-commentary'
Plug 'junegunn/fzf.vim'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }

call plug#end()

set mouse=a
set number
set relativenumber

if !isdirectory($HOME."/.vim")
	call mkdir($HOME."/.vim", "", 0770)
endif
if !isdirectory($HOME."/.vim/undo-dir")
	call mkdir($HOME."/.vim/undo-dir", "", 0770)
endif
set undodir=~/.vim/undo-dir
set undofile

set hlsearch
set ignorecase

set updatetime=300


" My personal preferences for nvim. 
" Please refer to github.com/hiagofranco/dotfiles
" AUTHOR: Hiago De Franco
" Date: may-08-2022

" -- Basic config
set number                    " Enable line numbers

set noswapfile                " No swap
set nobackup                  " No auto backups
set nowritebackup             " Speaks for itself

set expandtab                 " Use spaces instead of tabs
set smarttab                  " Be smart using tabs
set shiftwidth=4              " One tab == four spaces
set tabstop=4                 " One tab == four spaces

set mouse=nicr                " Enable mouse scrolling

set wildmenu                  " Display all matches when tab complete

set autoindent                " Auto indentantion
set smartindent               " Speaks for itself

set clipboard=unnamedplus     " Set clipboard to system's clipboard

set updatetime=100            " Set update time for git plugin

set noshowmode                " Prevent non-normal modes showing in airline.

syntax on                     " Enable code highlighting

" -- Match brackets and quotation marks ("", {}...)
inoremap ( ()<Esc>i
inoremap { {}<Esc>i
inoremap [ []<Esc>i
inoremap ' ''<Esc>i
inoremap " ""<Esc>i

" -- Vim Plugins
call plug#begin('~/.vim/plugged')

Plug 'morhetz/gruvbox'	                " Nice theme 
Plug 'airblade/vim-gitgutter'           " Git 
Plug 'vim-airline/vim-airline'          " Tab
Plug 'vim-airline/vim-airline-themes'   " Enable airline themes
Plug 'preservim/nerdtree'               " File manager
Plug 'ryanoasis/vim-devicons'           " File manager icons

call plug#end()

colorscheme gruvbox             " Set vim theme
let g:airline_theme='gruvbox'   " Set airline theme

" -- Set custom keys for NERDTree
nnoremap <leader>n :NERDTreeFocus<CR>
nnoremap <C-n> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
nnoremap <C-f> :NERDTreeFind<CR>

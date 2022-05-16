set nowrap
set number relativenumber

let g:coc_filetype_map = {
			\ 'yaml.ansible': 'ansible',
			\}

call plug#begin()
" The default plugin directory will be as follows:
"   - Vim (Linux/macOS): '~/.vim/plugged'
"   - Vim (Windows): '~/vimfiles/plugged'
"   - Neovim (Linux/macOS/Windows): stdpath('data') . '/plugged'
" You can specify a custom plugin directory by passing it as the argument
"   - e.g. `call plug#begin('~/.vim/plugged')`
"   - Avoid using standard Vim directory names like 'plugin'

" Make sure you use single quotes
" Plug 'dracula/vim'
Plug 'shaunsingh/nord.vim'


Plug 'neoclide/coc.nvim', {'branch': 'release'}

Plug 'ncm2/ncm2'
Plug 'ncm2/ncm2-jedi'

"autocmd BufEnter * call ncm2#enable_for_buffer()

Plug 'ryanoasis/vim-devicons' 
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'scrooloose/nerdtree'

" Switch to beginning and end of block with %
Plug 'tmhedberg/matchit'

" Comment / Uncomment tool
Plug 'preservim/nerdcommenter'

" A fuzzy finder
Plug 'junegunn/fzf', {'dir': '~/.fzf', 'do': './install --all'}
"Plug 'junegunn/fzf.vim'

" Creates a nice start screen if nvim is called without a file
Plug 'mhinz/vim-startify'
" Plug 'tpope/vim-sleuth'
" Plug 'editorconfig/editorconfig-vim'
" Git Integration
Plug 'tpope/vim-fugitive'

Plug 'sheerun/vim-polyglot'

" LSP Plugins
" Plug 'neovim/nvim-lspconfig'
" Plug 'hrsh7th/cmp-nvim-lsp'
" Plug 'hrsh7th/cmp-buffer'
" Plug 'hrsh7th/nvim-cmp'
" TabNine Plugin
" Plug 'tzachar/cmp-tabnine', { 'do': './install.sh' }
"Plug 'onsails/lspkind-nvim'
"Plug 'nvim-lua/lsp_extensions.nvim'

" Shortcuts
" GoTo Definition
nmap <silent> qd <Plug>(coc-definition)
:tnoremap <Esc> <C-\><C-n>

call plug#end()

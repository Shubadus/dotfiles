local cmd = vim.cmd
local fn = vim.fn

vim.g['coc_global_extensions'] = {
	'coc-sumneko-lua',
	'coc-prettier',
	'coc-yaml',
	'coc-tsserver',
	'coc-toml',
	'coc-tabnine',
	'coc-sh',
	'coc-rust-analyzer',
	'coc-pydocstring',
	'coc-powershell',
	'coc-json',
	'coc-jedi',
	'coc-go',
	'coc-docker',
--	'coc-ansible',
	'coc-snippets',
	'coc-git'
}

-- Installs Packer if not present
local install_path = fn.stdpath('data').. '/site/pack/packer/start/packer.nvim'
if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
  vim.o.runtimepath = vim.fn.stdpath('data').. '/site/pack/*/start/*,' .. vim.o.runtimepath
end

cmd([[packadd packer.nvim]])

cmd([[
	augroup packer_user_config
		autocmd!
		autocmd BufWritePost plugins.lua source <afile> | PackerCompile
	augroup end
]])

-- Initialize Plugins
return require("packer").startup(function(use)
	use {'wbthomason/packer.nvim'}
	use {'onsails/lspkind-nvim'}
	use {
		'tami5/lspsaga.nvim',
	--	requires={'neovim/nvim-lspconfig'}
	}
	use {'neoclide/coc.nvim', branch='release'}
	use {'nvim-lua/lsp_extensions.nvim'}
	use {'ryanoasis/vim-devicons'}
	use {'honza/vim-snippets'}
	use {'scrooloose/nerdtree'}
	use {'tmhedberg/matchit'}
--	use {'perservim/nerdcommenter'}
	use {
		'junegunn/fzf',
		--requires='junegunn/fzf.vim'
	}
	use {'junegunn/fzf.vim'}
	use {'mhinz/vim-startify'}
	use {'tpope/vim-fugitive'}
	use {'sheerun/vim-polyglot'}
	use {'nvim-treesitter/nvim-treesitter'}
	use {'kyazdani42/nvim-web-devicons'}
	use {
		'nvim-lualine/lualine.nvim',
	-- 	requires='kyazdani42/nvim-web-devicons'
	}
	use {
		'romgrk/barbar.nvim',
--		requires='kyazdani42/nvim-web-devicons'
	}
	use {'lukas-reineke/indent-blankline.nvim'}
	use {'nvim-lua/plenary.nvim'}
	use {
		'nvim-telescope/telescope.nvim',
		--requires={'nvim-lua/plenary.nvim'}
	}

	if packer_bootstrap then
		require('packer').sync()
	end
end)

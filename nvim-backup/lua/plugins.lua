local cmd = vim.cmd
local fn = vim.fn

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
	use('wbthomason/packer.nvim')

	-- lsp fun
	use('neovim/nvim-lspconfig')
	use('hrsh7th/cmp-nvim-lsp')
	use('hrsh7th/cmp-buffer')
	use('hrsh7th/nvim-cmp')
	use({'tzachar/cmp-tabnine', run='./install.sh', requires='hrsh7th/nvim-cmp'})
	use('onsails/lspkind-nvim')
	use('nvim-lua/lsp_extensions.nvim')
	use('glepnir/lspsaga.nvim')
	use('L3MON4D3/LuaSnip')
	use('saadparwaiz1/cmp_luasnip')

	use('ryanoasis/vim-devicons')
	use('honza/vim-snippets')
	-- use('scrooloose/nerdtree')
	use('tmhedberg/matchit')
	use('junegunn/fzf')
	use('junegunn/fzf.vim')
	use('mhinz/vim-startify')
	use('tpope/vim-fugitive')
	use('sheerun/vim-polyglot')
	use('nvim-treesitter/nvim-treesitter')
	use('nvim-treesitter/nvim-treesitter-context')
	use('kyazdani42/nvim-web-devicons')
	use('nvim-lualine/lualine.nvim')
	use('romgrk/barbar.nvim')
	use('lukas-reineke/indent-blankline.nvim')

	use('nvim-lua/plenary.nvim')
	use('nvim-lua/popup.nvim')
	use('nvim-telescope/telescope.nvim')

	-- Themes
	use('folke/tokyonight.nvim')


	if packer_bootstrap then
		require('packer').sync()
	end
end)

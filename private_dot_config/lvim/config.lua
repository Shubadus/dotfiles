--[[
lvim is the global options object

Linters should be
filled in as strings with either
a global executable or a path to
an executable
]]
-- THESE ARE EXAMPLE CONFIGS FEEL FREE TO CHANGE TO WHATEVER YOU WANT

-- general
lvim.log.level = "warn"
lvim.format_on_save = true
lvim.colorscheme = "catppuccin"
lvim.transparent_window = true
-- to disable icons and use a minimalist setup, uncomment the following
lvim.use_icons = true
-- keymappings [view all the defaults by pressing <leader>Lk]
lvim.leader = "space"
-- add your own keymapping
lvim.keys.normal_mode["<C-s>"] = ":w<cr>"

-- TODO: User Config for predefined plugins
-- After changing plugin config exit and reopen LunarVim, Run :PackerInstall :PackerCompile
lvim.builtin.alpha.active = true
lvim.builtin.alpha.mode = "dashboard"
lvim.builtin.autopairs.active = false
-- lvim.builtin.notify.active = true
lvim.builtin.terminal.active = true
lvim.builtin.nvimtree.setup.view.side = "left"
lvim.builtin.nvimtree.setup.renderer.icons.show.git = false

-- if you don't want all the parsers change this to a table of the ones you want
lvim.builtin.treesitter.ensure_installed = {
	"bash",
	"c",
	"javascript",
	"json",
	"lua",
	-- "markdown",
	"python",
	"typescript",
	"tsx",
	"css",
	"rust",
	"java",
	"yaml",
}

lvim.builtin.treesitter.ignore_install = { "haskell" }
lvim.builtin.treesitter.highlight.enabled = true

-- Start my personal configuration
-- Additional Plugins
lvim.plugins = {
	{
		"iamcco/markdown-preview.nvim",
		run = ":call mkdp#util#install()",
		config = function()
			vim.g.mkdp_browser = "/var/lib/flatpak/exports/bin/org.chromium.Chromium"
			vim.g.mkdp_theme = "dark"
		end,
	},
	{
		"folke/trouble.nvim",
		cmd = "TroubleToggle",
	},
	{ "catppuccin/nvim" },
	{ "luckasRanarison/tree-sitter-hypr" },
	{
		"tzachar/cmp-tabnine",
		run = "./install.sh",
		requires = "hrsh7th/nvim-cmp",
		config = function()
			local tabnine = require("cmp_tabnine.config")
			tabnine:setup({
				max_lines = 1000,
				max_num_results = 10,
				sort = true,
			})
		end,
		opt = true,
		event = "InsertEnter",
	},
}

-- Plugin configurations
require("catppuccin").setup({
	flavor = "macchiato",
})

-- Autocommands (https://neovim.io/doc/user/autocmd.html)
vim.api.nvim_create_autocmd("BufEnter", {
	pattern = { "*.json", "*.jsonc" },
	-- enable wrap mode for json files only
	command = "setlocal wrap",
})

vim.api.nvim_create_autocmd("FileType", {
	pattern = "zsh",
	callback = function()
		-- let treesitter use bash highlight for zsh files as well
		require("nvim-treesitter.highlight").attach(0, "bash")
	end,
})

vim.opt.relativenumber = true
vim.opt.smartindent = true
vim.opt.colorcolumn = "120"
vim.opt.cmdheight = 1
vim.opt.wrap = false
-- Disable Yanking directly to clipboard, this is handled by a Leader keymap
-- vim.opt.clipboard = ""

-- keybinds
-- Yank to clipboard
vim.keymap.set({ "n", "v" }, "<Leader>y", '"*y')
vim.keymap.set({ "n", "v" }, "<Leader>d", '"_d') -- delete line without writing over buffer
vim.keymap.set("v", "<leader>P", '"_dP') -- Paste over entry without losing buffer
vim.keymap.set("n", "<leader>P", '"+p') -- Paste from clipboard

-- Tab navigation
vim.keymap.set("n", "<Tab>", ":bprev<cr>")
vim.keymap.set("n", "<S-Tab>", ":bnext<cr>")
vim.keymap.set("n", "<Leader>d", ":bdelete<cr>")

-- Custom Commands --
vim.api.nvim_create_user_command("ReverseLines", function()
	vim.api.nvim_command(":g/^/m0")
end, {})

local parser_config = require("nvim-treesitter.parsers").get_parser_configs()
parser_config.hypr = {
	install_info = {
		url = "https://github.com/luckasRanarison/tree-sitter-hypr",
		files = { "src/parser.c" },
		branch = "master",
	},
	filetype = "hypr",
}

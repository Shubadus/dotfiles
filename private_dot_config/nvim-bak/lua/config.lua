local set = vim.opt

vim.g.mapleader = "space"

-- Neovide Config --
vim.g.neovide_transparency=0.9

-- Set Theme --
vim.g.tokyonight_style = "night"
vim.g.tokyonight_transparent = true
vim.cmd[[colorscheme tokyonight]]

set.guicursor = ""

set.autoindent = true
set.colorcolumn = "120"
set.expandtab = true
set.wrap = false
set.nu = true
set.nu.relativenumber = true
set.ruler = true
set.smartindent = true
set.commandheight = 1

set.clipboard:append("unnamedplus")
set.shortmess:append("c")

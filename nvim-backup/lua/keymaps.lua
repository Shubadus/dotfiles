local key = vim.keymap

-- Terminal Exit Remap 
-- For some reason, this doesn't work
key.set('n', '<Esc>', '<C-\\><C-N>')

-- Telescope cmds
key.set('n', '<Leader>ff', '<cmd>Telescope find_files<cr>')
key.set('n', '<Leader>fg', '<cmd>Telescope live_grep<cr>')
key.set('n', '<Leader>fb', '<cmd>Telescope buffers<cr>')
key.set('n', '<Leader>fh', '<cmd>Telescope help_tags<cr>')

-- BarBar cmds
key.set('n', '<A-j>', '<cmd>BufferPrevious<cr>')
key.set('n', '<A-k>', '<cmd>BufferNext<cr>')
key.set('n', '<A-q>', '<cmd>BufferClose<cr>')

-- Netrw cmds
key.set('n', '<Leader>e', '<cmd>Explore<cr>')

-- LSP Config
--key.set('n', 'gd', function vim.lsp.buf.definition() end)
--key.set('n', 'K', function vim.lsp.buf.hover() end)


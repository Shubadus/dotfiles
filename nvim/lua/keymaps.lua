-- Telescope cmds
vim.keymap.set('n', '<Leader>ff', '<cmd>Telescope find_files<cr>')
vim.keymap.set('n', '<Leader>fg', '<cmd>Telescope live_grep<cr>')
vim.keymap.set('n', '<Leader>fb', '<cmd>Telescope buffers<cr>')
vim.keymap.set('n', '<Leader>fh', '<cmd>Telescope help_tags<cr>')

-- BarBar cmds
vim.keymap.set('n', '<A-j>', '<cmd>BufferPrevious<cr>')
vim.keymap.set('n', '<A-k>', '<cmd>BufferNext<cr>')
vim.keymap.set('n', '<A-q>', '<cmd>BufferClose<cr>')


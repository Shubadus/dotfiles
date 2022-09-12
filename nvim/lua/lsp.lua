local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

local cmp = require("cmp")
-- local lsp = require("lspconfig")
local lspkind = require("lspkind")
local tabnine = require('cmp_tabnine.config')

local source_mapping = {
	youtube = "[Suck it YT]",
	buffer = "[Buffer]",
	nvim_lsp = "[LSP]",
	nvim_lua = "[Lua]",
	cmp_tabnine = "[TN]",
	path = "[Path]",
}

local key = vim.keymap
local sumneko_root_path = "/home/cshumer/servers/sumneko"
local sumneko_binary = sumneko_root_path .. "/bin/lua-language-server"

cmp.setup({
	snippet = {
		expand = function(args)
			require("luasnip").lsp_expand(args.body)
		end,
	},
	mapping = cmp.mapping.preset.insert({
		['<C-y>'] = cmp.mapping.confirm({ select = true }),
		["<C-u>"] = cmp.mapping.scroll_docs(-4),
		["<C-d>"] = cmp.mapping.scroll_docs(4),
		["<C-Space>"] = cmp.mapping.complete(),
	}),

	formatting = {
		format = function(entry, vim_item)
			vim_item.kind = lspkind.presets.default[vim_item.kind]
			local menu = source_mapping[entry.source.name]
			if entry.source.name == "cmp_tabnine" then
				if entry.completion_item.data ~= nil and entry.completion_item.data.detail ~= nil then
					menu = entry.completion_item.data.detail .. " " .. menu
				end
				vim_item.kind = ""
			end
			vim_item.menu = menu
			return vim_item
		end,
	},

	sources = {
		-- tabnine completion? yayaya
		{ name = "cmp_tabnine" },

		{ name = "nvim_lsp" },

		-- For vsnip user.
		-- { name = 'vsnip' },

		-- For luasnip user.
		{ name = "luasnip" },

		-- For ultisnips user.
		-- { name = 'ultisnips' },
		{ name = "buffer" },

		{ name = "youtube" },
	},
})

local function config(_config)
	return vim.tbl_deep_extend("force", {
		capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities()),
			on_attach = function()
-- 				key('n', 'gd', function() vim.lsp.buf.definition() end)
-- 				key('n', 'K', function() vim.lsp.buf.hover() end)
-- 				key('n', '<leader>vws', function() vim.lsp.buf.workspace_symbol() end)
-- 				key('n', '<leader>vd', function() vim.diagnostic.open_float() end)
-- 				key('n', '[d', function() vim.diagnostic.goto_next() end)
-- 				key('n', ']d', function() vim.diagnostic.goto_prev() end)
-- 				key('n', '<leader>vca', function() vim.lsp.buf.code_action() end)
-- 				key('n', '<leader>vrr', function() vim.lsp.buf.reference() end)
-- 				key('n', '<leader>vrn', function() vim.lsp.buf.rename() end)
-- 				key('n', '<C-h>', function() vim.lsp.buf.signature_help() end)
			end,
	}, _config or {})
end


-- LSP Server setup
-- lsp['ansiblels'].setup(config())
-- require("lspconfig")['ansible-language-server'].setup(config())
-- lsp['bashls'].setup(config())
require("lspconfig").bashls.setup(config())
-- lsp['dockerls'].setup(config())
require("lspconfig").dockerls.setup(config())
-- lsp['gopls'].setup(config({
-- 	cmd = { "gopls", "serve" },
-- 	settings = {
-- 		gopls = {
-- 			analyses = {
-- 				unusedparams = true,
-- 			},
-- 			staticcheck = true,
-- 		},
-- 	},
-- }))
require("lspconfig").gopls.setup(config({
	cmd = { "gopls", "serve" },
	settings = {
		gopls = {
			analyses = {
				unusedparams = true,
			},
			staticcheck = true,
		},
	},
}))
--lsp['jedi_language_server'].setup(config())

require("lspconfig").jedi_language_server.setup(config())
require("lspconfig").jsonls.setup(config())
--lsp['jsonls'].setup(config({
--		capabilities = capabilities
--}))
--lsp['powershell'].setup(config())
--lsp['rust_analyzer'].setup(config())
require("lspconfig").rust_analyzer.setup(config({
	cmd = { 'rustup', 'run', 'nightly', 'rust-analyzer' },
}))
--lsp['sumneko_lua'].setup(config({
require("lspconfig").sumneko_lua.setup(config({
	cmd = { sumneko_binary, "-E", sumneko_root_path .. "/main.lua" },
	settings = {
		Lua = {
			runtime = {
				-- Tell the language server which version of Lua you're using (most likely LuaJIT in the case of Neovim)
				version = "LuaJIT",
				-- Setup your lua path
				path = vim.split(package.path, ";"),
			},
			diagnostics = {
				-- Get the language server to recognize the `vim` global
				globals = { "vim" },
			},
			workspace = {
				-- Make the server aware of Neovim runtime files
				library = {
					[vim.fn.expand("$VIMRUNTIME/lua")] = true,
					[vim.fn.expand("$VIMRUNTIME/lua/vim/lsp")] = true,
				},
			},
		},
	},
}))
require("lspconfig").tsserver.setup(config())
-- lsp['tsserver'].setup(config())
--lsp['yamlls'].setup(config())

tabnine.setup({
	max_lines = 1000,
	max_num_results = 20,
	sort = true,
	run_on_every_keystroke = true,
	snippet_placeholder = '..',
	ignored_file_types = {
		-- default is not to ignore
		-- uncomment to ignore in lua:
		-- lua = true
	},
	show_prediction_strength = false
})


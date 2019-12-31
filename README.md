# nvim-ipython-repl

A very simple [IPython](https://ipython.org/) [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) plugin for [Neovim](https://neovim.io/).

## Why?

There are currently some very nice, full-featured Neovim plugins focused on enabling a rich REPL experience across many languages.  In particular, here are a couple nicely maintained plugins:
  * [Vigemus/iron.nvim](https://github.com/Vigemus/iron.nvim)
  * [kassio/neoterm](https://github.com/kassio/neoterm)

I really focus on Python, and I like to control the aesthetics of my REPL experience.  I also often work on Windows, which is usually a second-class citizen for most Neovim plugins.  So I made this simple plugin to meet my needs.

## Installation

Should be able to install/setup with the tool of your choice (e.g. [tpope/vim-pathogen](https://github.com/tpope/vim-pathogen), [junegunn/vim-plug](https://github.com/junegunn/vim-plug).

## Configuration

This plugin will define some key mappings for Python filetypes by defaults.  Look in `ftplugin/python.vim` to see the defaults.  To disable the defaults, add `let g:ipython_repl_map_keys = 0` to your `init.vim`.

This plugin requires [IPython](https://ipython.org/) to be available.  If `ipython` isn't already available on your `$PATH`, or you want to use a specific `ipython` executable, you can set `g:ipython_repl_ipython_executable` in your `init.vim`.

## Implementation Details

This plugin only works on [Neovim](https://neovim.io/) (i.e. not Vim).  The current implementation uses the system clipboard to pass code between a buffer and the IPython interpreter.  I have directly piped the code into the IPython subprocess in the past, but that misbehaves on larger code snippets (among other issues).

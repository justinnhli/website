title: Open a Directory in Vim Terminal
date: 2020-05-05

I've never found (neo)vim's [netrw](https://neovim.io/doc/user/pi_netrw.html) to be particularly useful, and have generally much preferred to navigate via the [built-in terminal](https://neovim.io/doc/user/nvim_terminal_emulator.html). I've generally managed to avoid netrw, with the one exception being when I `:tabnew` a directory. I finally fixed that by configuring vim to open a terminal at that directory instead:

```vim
function s:isdir(dir) abort
	return !empty(a:dir) && isdirectory(a:dir)
endfunction

augroup justinnhli_open_directories
	autocmd!
	autocmd VimEnter * silent! autocmd! FileExplorer *
	autocmd BufEnter * if s:isdir(expand('%')) | execute ':terminal' | startinsert | endif
augroup END
```

I got the general idea from [this StackOverflow answer](https://vi.stackexchange.com/questions/10471/autocmd-on-directory-to-replace-netrw). The key are the two `autocmd` commands. The first disables netrw ("`FileExplorer`") from running. The second checks if the target is a directory, then opens `:terminal` if it is.

I have several more neovim terminal settings, available on my [dotfiles repo](https://github.com/justinnhli/dotfiles/blob/912a335bf72dc3e94a2ace8829d009b470888ec5/neovim/.config/nvim/plugin/terminal.vim).

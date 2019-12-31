if !exists("g:ipython_repl_map_keys")
    let g:ipython_repl_map_keys = 1
endif

if !exists("g:ipython_repl_ipython_executable")
    let g:ipython_repl_ipython_executable = "ipython"
endif

if g:ipython_repl_map_keys == 1
   noremap <Leader>si :call ipython_repl#LaunchIPython()<CR>
   noremap <Leader>sr :call ipython_repl#SendToTerminal()<CR>
   noremap <Leader>ss :call ipython_repl#SendNudgeToTerminal()<CR>
endif

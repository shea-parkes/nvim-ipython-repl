if !exists("g:ipython_repl_map_keys")
    let g:ipython_repl_map_keys = 1
endif

if g:ipython_repl_map_keys == 1
   nnoremap <Leader>si :call ipython_repl#LaunchIPython()<CR>
   nnoremap <Leader>sr :call ipython_repl#SendToTerminal()<CR>
   nnoremap <Leader>ss :call ipython_repl#SendNudgeToTerminal()<CR>
endif

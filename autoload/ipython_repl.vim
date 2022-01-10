let s:my_active_terminal_job_id = -1
let s:path_to_ipython_repl_init = expand('<sfile>:p:h') . "/ipython_repl_init.py"

function! ipython_repl#LaunchTerminal() range
  silent exe "normal! :vsplit\n"
  silent exe "normal! :terminal\n"
  exe "normal! G\n"
  call ipython_repl#SetActiveTerminalJobID()
endfunction

function! ipython_repl#LaunchIPython() range
  call ipython_repl#LaunchTerminal()
  call jobsend(s:my_active_terminal_job_id, g:ipython_repl_ipython_executable . " -i " . s:path_to_ipython_repl_init . "\r")
endfunction

function! ipython_repl#SetActiveTerminalJobID() range
  let s:my_active_terminal_job_id = b:terminal_job_id
  echom "Active terminal job ID set to " . s:my_active_terminal_job_id
endfunction

function! ipython_repl#SendToTerminal() range
  " Yank the last selection into an arbitrary register
  silent exe 'normal! gv"ry'
  " Write the contents of that register into a transfer file
  call writefile(split(getreg('r'), '\n'), $HOME . '/.vim_ipython_xfer.txt')
  " Tell IPython to read from the transfer file
  call jobsend(s:my_active_terminal_job_id, "run_from_xfer_file()")
  " Pause a moment, then send a carriage return to trigger its evaluation
  sleep 210ms
  call jobsend(s:my_active_terminal_job_id, "\r")
endfunction

function! ipython_repl#SendNudgeToTerminal() range
  " Send in a nudge.  Can help trigger IPython evaluation
  call jobsend(s:my_active_terminal_job_id, "\r")
endfunction

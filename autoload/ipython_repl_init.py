"""
Prepare an IPython interpreter for REPL use.

Note: shell.write() is depreciated for interactive shells; just print.
"""
import IPython
import IPython.terminal.magics

N_LINES_GLIMPSE = 2
IPYTHON_COLORIZE_ERROR_PREFIX = '*** ERROR:'  # From `IPython.utils.PyColorize`
TERMINAL_COLOR_CODE_PREFIX = '\x1b'  # Literally translates to ESC
IPYTHON_SHELL = IPython.get_ipython()
TERMINAL_MAGICS = IPython.terminal.magics.TerminalMagics(IPYTHON_SHELL)


def _colorize_code_snippet(code_snippet: str) -> str:
    """Colorize snippet safely"""
    colored_raw = IPYTHON_SHELL.pycolorize(code_snippet)

    # Manually extract the error messages inserted into the coloring.
    #  IPython unfortunately does not provide a way to disable these.
    try:
        first_error = colored_raw.index(IPYTHON_COLORIZE_ERROR_PREFIX)
        final_error = colored_raw.rindex(IPYTHON_COLORIZE_ERROR_PREFIX)
        final_color_start = colored_raw.index(TERMINAL_COLOR_CODE_PREFIX, final_error)
        return colored_raw[:first_error].rstrip() + colored_raw[final_color_start:].rstrip()
    except ValueError:
        return colored_raw.rstrip()


def run_from_clipboard():
    """Run code from the clipboard the way I want to"""
    code_raw = IPYTHON_SHELL.hooks.clipboard_get()
    code_split = code_raw.rstrip().split('\n')

    code_to_echo = []
    code_to_echo.append('# <<<< Grabbed {} line{} from the clipboard:'.format(
        len(code_split),
        's' if len(code_split) > 1 else '',
    ))
    if len(code_split) <= (2*N_LINES_GLIMPSE + 1):
        code_to_echo.extend(code_split)
    else:
        code_to_echo.extend(code_split[:N_LINES_GLIMPSE])
        code_to_echo.append('# ... omitting {} lines ...'.format(
            len(code_split) - 2*N_LINES_GLIMPSE,
        ))
        code_to_echo.extend(code_split[-N_LINES_GLIMPSE:])
    code_to_echo.append('# >>>>')
    print(_colorize_code_snippet('\n'.join(code_to_echo)))

    TERMINAL_MAGICS.store_or_execute('\n'.join(code_split), None)


def _test_colorize_code_snippet():
    """Some quick tests of colorizing code snippets with errors"""
    snippet_complete = [
        '# A simple list',
        'names = [',
        '"bob",',
        '"alice",',
        '"eve",',
        ']',
    ]

    colored_complete = _colorize_code_snippet('\n'.join(snippet_complete))
    assert IPYTHON_COLORIZE_ERROR_PREFIX not in colored_complete

    snippet_incomplete = snippet_complete[:-2]

    colored_incomplete = IPYTHON_SHELL.pycolorize('\n'.join(snippet_incomplete))
    assert IPYTHON_COLORIZE_ERROR_PREFIX in colored_incomplete

    colored_incomplete_cleaned = _colorize_code_snippet('\n'.join(snippet_incomplete))
    assert IPYTHON_COLORIZE_ERROR_PREFIX not in colored_incomplete_cleaned

_test_colorize_code_snippet()

""" some commonly occurring arguments
"""
from ._arg import required as _required
from ._arg import optional as _optional
from ._arg import flag as _flag

SUBCOMMAND_KEY = '_sc'
LOG_FILE_KEY = '_lf'
LOG_LEVEL_KEY = '_ll'
PRINT_STDOUT_KEY = '_pt'


# commondly occurring arguments
def subcommand(vals=None):
    """ subcommand argument
    """
    return _required(SUBCOMMAND_KEY, 'subcommand', vals=vals)


def log_file(default=None):
    """ log file
    """
    return _optional(LOG_FILE_KEY, 'log_file', 'l', default=default,
                     msgs=('log file path',))


def log_level():
    """ verbosity of the log file
    """
    return _optional(LOG_LEVEL_KEY, 'log_level', 'v', dtype=int, default=20,
                     vals=[10, 20])


def print_stdout():
    """ whether or not to print to stdout
    """
    return _flag(PRINT_STDOUT_KEY, 'print_stdout', 'p',
                 msgs=('print log to stdout as well?',))

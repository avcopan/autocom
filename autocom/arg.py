""" library for generating args and kwargs to ArgumentParser.add_argument
"""
# generic argument generators
from ._arg import required
from ._arg import required_list
from ._arg import optional
from ._arg import optional_list
from ._arg import flag
# functions operating on arguments
from ._arg import key_
# specific common arguments
from ._arglib import subcommand
from ._arglib import log_file
from ._arglib import log_level
from ._arglib import print_stdout


__all__ = [
    # generic argument generators
    'required',
    'required_list',
    'optional',
    'optional_list',
    'flag',
    # functions operating on arguments
    'key_',
    # specific common arguments
    'subcommand',
    'log_file',
    'log_level',
    'print_stdout',
]

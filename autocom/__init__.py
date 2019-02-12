""" command-line interface module
"""
from . import arg
from ._autocom import call_subcommand
from ._autocom import values_with_logger

__all__ = [
    'arg',
    'call_subcommand',
    'values_with_logger',
]

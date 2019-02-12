""" command-line interface module
"""
import sys
from .sysargv import expanded_base_command as _expanded_base_command
from .sysargv import command_line as _command_line
from .arg import subcommand as _subcommand
from .arg import log_file as _log_file
from .arg import log_level as _log_level
from .arg import print_stdout as _print_stdout
from .arg import key_ as _arg_key
from ._argparse import parser as _parser
from ._argparse import value_dictionary as _parser_value_dictionary
from ._argparse import exit_helpfully as _exit_parser_helpfully
from ._logger import logger as _logger


def call_subcommand(sysargv, calling_pos, subcmd_func_dct):
    """ parse a subcommand key and call the appropriate function
    """
    subcmd_pos = calling_pos + 1
    subcmd_keys = subcmd_func_dct.keys()
    subcmd_key = _subcommand_value(sysargv, subcmd_pos=subcmd_pos,
                                   subcmd_keys=subcmd_keys)
    subcmd_func_dct[subcmd_key](sysargv, subcmd_pos)


def values_with_logger(sysargv, first_arg_pos, arg_lst):
    """ call a function whose last argument is logger=logging.Logger() """
    exe_path = _expanded_base_command(sysargv)
    cmd_str = ' '.join(_command_line(sysargv))
    log_name_prefix = '_'.join(_command_line(sysargv[1:first_arg_pos]))
    log_name = '{:s}.log'.format(log_name_prefix)
    log_arg_lst = [_log_file(log_name), _log_level(), _print_stdout()]

    _arg_lst = arg_lst + log_arg_lst
    _val_dct = _value_dictionary(sysargv, first_arg_pos, _arg_lst)
    arg_vals = list(map(_val_dct.__getitem__, map(_arg_key, arg_lst)))

    # generate the logger and write some information about the command to it
    log_arg_vals = list(map(_val_dct.__getitem__, map(_arg_key, log_arg_lst)))
    logger = _logger(*log_arg_vals)
    logger.info('# cmd: {:s}'.format(cmd_str))
    logger.info('# exe: {:s}'.format(exe_path))

    arg_vals.append(logger)
    return arg_vals


def _value_dictionary(sysargv, first_arg_pos, arg_lst):
    """ parse the arguments list in order """
    cmd_str = ' '.join(_command_line(sysargv))
    parser = _parser(cmd_str, arg_lst)
    if '-h' in sysargv or '--help' in sysargv:
        _exit_parser_helpfully(parser)
    val_dct = _parser_value_dictionary(parser, sysargv[first_arg_pos:])
    return val_dct


def _subcommand_value(sysargv, subcmd_pos, subcmd_keys):
    """ parse the value of a positional subcommand """
    cmd_str = ' '.join(_command_line(sysargv[:subcmd_pos]))
    arg_lst = [_subcommand(vals=subcmd_keys)]
    parser = _parser(cmd_str, arg_lst)

    if subcmd_pos >= len(sysargv):
        _exit_parser_helpfully(parser)

    subcmd_key = sysargv[subcmd_pos]

    if subcmd_key in ('-h', '--help'):
        _exit_parser_helpfully(parser)
    elif subcmd_key not in subcmd_keys:
        sys.stderr.write("'{:s}' is not a subcommand of '{:s}'\n"
                         .format(subcmd_key, cmd_str))
        _exit_parser_helpfully(parser)

    return subcmd_key

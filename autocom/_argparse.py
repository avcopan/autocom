""" argparse interface
"""
from argparse import ArgumentParser as _Parser
from argparse import ArgumentDefaultsHelpFormatter as _HelpFormatter


def parser(cmd_str, arg_lst):
    """ an argparse parser object

    :param cmd_str: the command string
    :type cmd_str: str
    :param arg_lst: args and kwargs for ArgumentParser.add_argument
    :type arg_lst: tuple

    :returns: a parser object
    :rtype: argparse.ArgumentParser
    """
    par = _Parser(prog=cmd_str, formatter_class=_HelpFormatter, add_help=False)
    for args, kwargs in arg_lst:
        par.add_argument(*args, **kwargs)
    return par


def value_dictionary(prs_obj, sysargv):
    """ value dictionary for command-line arguments

    :param prs_obj: a parser object
    :type prs_obj: argparse.ArgumentParser
    :param sysargv: sys.argv
    :type sysargv: list

    """
    val_dct = vars(prs_obj.parse_args(sysargv))
    return val_dct


def exit_helpfully(prs_obj):
    """ print the help message for a parser object
    """
    prs_obj.print_help()
    prs_obj.exit()

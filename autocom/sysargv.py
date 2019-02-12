""" functions operating on sys.sys_argv
"""
import os


def expanded_base_command(sys_argv):
    """ the exectuable path
    """
    assert sys_argv
    base_cmd = sys_argv[0]
    return base_cmd


def base_command_name(sys_argv):
    """ the executable name
    """
    base_cmd = expanded_base_command(sys_argv)
    if os.path.isfile(base_cmd):
        base_cmd = os.path.basename(base_cmd)
    return base_cmd


def command_line(sys_argv):
    """ command line, replacing the base path with its command name
    """
    sys_argv = list(sys_argv).copy()
    sys_argv[0] = base_command_name(sys_argv)
    return tuple(sys_argv)

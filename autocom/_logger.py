""" logging interface
"""
import os
import sys
import time
import logging


def logger(log_name, log_level, print_out):
    """ create a logger with certain specifications
    """
    _logger = logging.getLogger()
    _logger.setLevel(log_level)

    _timestamp_if_exists(log_name)

    fhandler = logging.FileHandler(log_name, mode='w')
    fhandler.setLevel(log_level)

    formatter = logging.Formatter('%(message)s')
    fhandler.setFormatter(formatter)

    _logger.addHandler(fhandler)

    if print_out:
        shandler = logging.StreamHandler(sys.stdout)
        shandler.setLevel(log_level)
        shandler.setFormatter(formatter)
        _logger.addHandler(shandler)

    return _logger


def _timestamp_if_exists(file_pth):
    """ open a file, avoiding overwrites if requested
    """
    if os.path.isfile(file_pth):
        time_stamp = time.strftime("%Y%m%d-%H%M%S")
        new_file_pth = "{:s}_{:s}".format(file_pth, time_stamp)
        os.rename(file_pth, new_file_pth)

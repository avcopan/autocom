""" library for generating args and kwargs to ArgumentParser.add_argument
"""


def required(key, name, dtype=str, vals=None, msgs=()):
    """ specifications for a required argument
    """
    return _required(
        name=name,
        dest=key,
        type=dtype,
        choices=vals,
        help=_help_message(msgs, vals=vals)
    )


def required_list(key, name, dtype=str, msgs=()):
    """ specifications for a required argument
    """
    return _required(
        name=name,
        dest=key,
        type=dtype,
        nargs='+',
        help=_help_message(msgs)
    )


def optional(key, name, char, tag=None, dtype=None, default=None, vals=None,
             msgs=()):
    """ specifications for an optional argument
    """
    return _optional(
        name=_tagged_name(name, tag=tag),
        dest=key,
        char=char,
        metavar=name.upper(),
        type=dtype,
        default=default,
        choices=vals,
        help=_help_message(msgs, tag=tag, vals=vals)
    )


def optional_list(key, name, char, tag=None, dtype=None, default=None,
                  msgs=()):
    """ specifications for an optional argument
    """
    return _optional(
        name=_tagged_name(name, tag=tag),
        dest=key,
        char=char,
        metavar=name.upper(),
        type=dtype,
        default=default,
        nargs='+',
        help=_help_message(msgs, tag=tag)
    )


def flag(key, name, char, msgs=()):
    """ specifications for an optional argument
    """
    return _optional(
        name=name,
        dest=key,
        char=char,
        action='store_true',
        help=_help_message(msgs)
    )


# helper functions
def _required(name, **kwargs):
    args = ()
    kwargs = {key: val for key, val in kwargs.items() if val is not None}
    assert 'metavar' not in kwargs
    kwargs['metavar'] = '<{:s}>'.format(name)
    return args, kwargs


def _optional(name, char, **kwargs):
    assert isinstance(char, str) and len(char) == 1
    args = ('-{:s}'.format(char), '--{:s}'.format(name))
    kwargs = {key: val for key, val in kwargs.items() if val is not None}
    return args, kwargs


def _tagged_name(name, tag=None):
    """ an argument name with a tag to distinguish it
    """
    if tag is not None:
        assert isinstance(tag, str)
        name += '_{:s}'.format(tag)
    return name


def _help_message(msgs, tag=None, vals=None):
    """ extend a basic help message with a tag and a list of possible argument
    values
    """
    msgs = list(msgs)
    if vals is not None:
        msgs.append('options: {:s}'.format(', '.join(map(str, vals))))

    help_msg = '; '.join(msgs)
    if tag is not None:
        assert isinstance(tag, str)
        assert isinstance(help_msg, str)
        help_msg = '[{:s}] {:s}'.format(tag, help_msg)

    return help_msg


# functions operating on arguments
def key_(arg):
    """ get an argument's destiation key """
    _, kwargs = arg
    return kwargs['dest']

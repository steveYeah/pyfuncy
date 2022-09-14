from functools import partial, wraps
from inspect import signature


def curry(fn, *args):
    """
    Decorator for currying functions
    """
    @wraps(fn)
    def curried(*args):
        if len(args) + _get_num_args(fn) == _get_num_fn_params(fn):
            return fn(*args)

        return curry(partial(fn, *args))

    return curried

def _get_num_args(fn):
    """
    Get the number of arguments already applied to the given function
    """
    if not isinstance(fn, partial):
        return 0

    return len(fn.args)


def _get_num_fn_params(fn):
    """
    Get the number of parameters required by the given function
    """
    if isinstance(fn, partial):
        return len(signature(fn.func).parameters)

    return len(signature(fn).parameters)


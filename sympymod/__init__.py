import types
import sympy
import sys
from .equation import *
from .pick import *

from functools import wraps



this_module = sys.modules[__name__]


def _get_imported_names(module):
    names = module.__all__ if hasattr(module, '__all__') else dir(module)
    return [name for name in names if not name.startswith('_')]


def _wrap_function(func):

    @wraps(func)
    def f(*args, **kwargs):
        if isinstance(args[0], Eq):
            if len(args) > 1:
                other_args = tuple(args[1:])
            else:
                other_args = ()
            return args[0].apply('both', func, *other_args, **kwargs)
        else:
            return func(*args, **kwargs)
    return f



_names_from_sympy = _get_imported_names(sympy)


for name in _names_from_sympy:
    obj = getattr(sympy, name)
    if isinstance(obj, types.FunctionType) or isinstance(obj, sympy.FunctionClass):
        setattr(this_module, name, _wrap_function(obj))

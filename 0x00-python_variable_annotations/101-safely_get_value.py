#!/usr/bin/env python3
"""
This module has the function safely_get_value
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return value of a key in dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default

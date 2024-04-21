#!/usr/bin/env python3
"""
This module has the function safe_first_element
"""
from typing import List, Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list
    """
    if lst:
        return lst[0]
    else:
        return None

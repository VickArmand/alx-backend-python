#!/usr/bin/env python3
"""
This module has function sum_mixed_list
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and floats and
    returns their sum as a float.
    """
    return sum(mxd_lst)

#!/usr/bin/env python3
"""
This module has the function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Write a type-annotated function sum_list
    which takes a list input_list of floats as argument
    and returns their sum as a float.
    """
    total: float = 0.0
    for val in input_list:
        total += val
    return total

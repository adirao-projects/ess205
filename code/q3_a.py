# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:57:28 2023

@author: Aditya Rao
"""
import math


def part_a(n: int) -> float:
    """

    Parameters
    ----------
    n : int
        natural number (starting from 0).

    Returns
    -------
    c : float
        c for corresponding n.

    """
    # Used to check what n value is being calculated
    # print(f"Depth:{n}")

    if n == 1:
        # Base case 1: n=0 will always return 2
        
        return 1
    
    else: 
        # Notice a_{n} = a_{n}^{2} - 2a_{n}
        # Hence we have identified our recursion
        
        return part_a(int(math.sqrt(n)))*part_a(int(math.sqrt(n)))  \
            + 2*part_a(int(math.sqrt(n)))

if __name__ == "__main__":
    print(part_a(2))
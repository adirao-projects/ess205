# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:11:57 2023

@author: Aditya Rao
"""
import math


def part_b(n: int) -> float:
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

    # We must aways raise an exception if n=1. However, I have ASSUMED that
    # this does not apply if we are calculating a(n) n\neq 1
    if n == 1:
        # Base case 1: n=0 will always return 2
        raise Exception("n==1")
        
        return 1
    
    else: 
        # Notice a_{n} = a_{n}^{2} - 2a_{n}
        # Hence we have identified our recursion
        
        # Calculating n==1 is not allowed, hence, we straight calculate the
        # other values.
        if (int(math.sqrt(n))) == 1:
            return 3
        else:
            return part_b(int(math.sqrt(n)))*part_b(int(math.sqrt(n)))  \
                + 2*part_b(int(math.sqrt(n)))

if __name__ == "__main__":
    print(part_b(2))
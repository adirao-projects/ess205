# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:33:07 2023

@author: Aditya Rao
"""

def part_a(x: float, n: int) -> float:
    """

    Parameters
    ----------
    x : float
        non-zero real number.
    n : int
        natural number (starting from 0).

    Returns
    -------
    c : float
        c for corresponding n.

    """
    # Used to check what n value is being calculated
    # print(f"Depth:{n}")
    
    if n == 0:
        # Base case 1: n=0 will always return 2
        
        return 2
    
    elif n == 1:
        # Base case 2: n=1 will always return x + \frac{x}{1/x}
        
        return (x + (1/x))
    
    else: 
        # Notice c_{n} = (c_{n-1})*(c_{1}) - (c_{n-2})
        # Hence we have identified our recursion
        
        return ((part_a(x, (n-1))*part_a(x, 1)) - part_a(x, (n-2)))

if __name__ == "__main__":
    print(part_a(2, 10))
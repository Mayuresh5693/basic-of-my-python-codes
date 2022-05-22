#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 00:47:08 2022

@author: mayureshdhule
"""



"""power of function using recursion"""

def power(a, b):
    if b == 0:
        return 1

    else:
        return a * power(a, b - 1)




power(2,5)







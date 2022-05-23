#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 02:58:16 2022

@author: mayureshdhule
"""



""" factorial function using recursion  """



def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
    
    
fact(4)
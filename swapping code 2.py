#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:06:37 2022

@author: mayureshdhule
"""
#code for swapping two interger

m = int(input('please enter any number: m = '))
n = int(input('please enter any number: n = '))

m = m + n
n = m - n
m = m - n

print ('after swapping')

print ('m =',m)
print ('n =',n)

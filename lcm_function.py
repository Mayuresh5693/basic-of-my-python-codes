#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 13:44:22 2022

@author: mayureshdhule
"""

"""LCM - LIST COMMON MULTUPLYER """



def lcm(a,b):

    
    #a = int(input('enter first number'))
    #b = int(input('enter first number'))
    
    '''finding heigher value from input'''
    
    if a > b :
        higher = a
    else:
        higher = b
        
    temp = higher  # store higher value in temp variable 
    
    while(True):  # to repeat following condition till statisfy if statement 
        
        if higher % a == 0 and higher % b == 0 :
            print ('lcm of given number is',higher)
            
            break
        
        else:        # add higher itself to get next multiplyer
            
            higher = temp + higher
            
            
            
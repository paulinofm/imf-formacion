# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:47:29 2019

@author: FERMASOLAR
"""

# Program to multiply two matrices using list comprehension

# 3x7 matrix
X = [[12,7,3,5,8,9,2],
    [4,5,6,4,3,7,9],
    [7,8,9,10,11,56,7]]

# 7x4 matrix
Y = [[5,8,1,3],
    [6,7,4,7],
    [4,5,0,1],
    [1,2,1,9],
    [4,8,0,8],
    [0,5,4,5],
    [3,6,8,2]]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

for r in result:
   print(r)
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:17:00 2018

@author: Nakyilkim
"""

## pg216

import random

random.seed(1234)

num_size = 10
board = [[random.randint(1,3) for i in range(num_size)] for j in range(num_size)]


def jump(x,y):
    
    print("Starting Funcition",x,y)
    ## 기저 사례부터 밖으로 나간 경우
    if y >= num_size or x >= num_size: return False
    ## 기저 사례 마지막에 도착한 경우
    if y == num_size-1 and x == num_size-1: return True
    
    jump_size = board[x][y]
    print("jump size",jump_size)
    return jump(x+jump_size, y) or jump(x,y+jump_size)


## Dynamic Programming - using memoization
    
cache =  [[-1 for i in range(num_size)] for j in range(num_size)]



def jump2(x,y):
    
    print("Starting Funcition",x,y)
    ## 기저 사례부터 밖으로 나간 경우
    if y >= num_size or x >= num_size: return 0
    ## 기저 사례 마지막에 도착한 경우
    if y == num_size-1 and x == num_size-1: return 1
    
    ### Memoit
    ret = cache[x][y]
    if ret != -1 : return ret
    
    jump_size = board[x][y]
    print("jump size",jump_size)
    
    ret = jump2(x+jump_size, y) or jump2(x,y+jump_size)
    cache[x][y] = ret
    
    return ret


## pg 218 WILDCARD


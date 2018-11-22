# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:40:28 2018

@author: Nakyilkim
"""

### JongManBook 
##pg 94

import random

random.seed(1234)
rand_num = [random.randint(40,60) for x in range(10)]

def getMovingAverage(arr):
    
    mov_arv = []
    
    for i in range(len(arr)-3):
        mov_arv.append(sum(arr[i:i+3])/3)
        print(arr[i:i+3])
    
    
    return mov_arv

#mov_arv = getMovingAverage(rand_num)
#print(mov_arv)
#print(rand_num)


# pg 102 
# CanEverybodyEat
# 재귀 함수 형태로 그려보기
#  재귀를 일단 배우고 하자
    
#INF = 987654321
#
#canEverybodyEat = True
#foodNum = 0
#
## 먹을 수 있는 지 확인
#def canEverybodyEat(menu):
#    
#    
#    
#    return  pass
#
#def selectMenu(menu, food):
#    
#    if food == M :
#        if canEverybodyEat(menu): return menu.size()
#        
#        else : return INF
#    
#   return pass     
    
### Pg 117
### 연속된 숫자의 합이 가장 클 때 구하기

arr = [-7, 4 ,-3 ,6 ,3 ,-8, 3, 4]

def inefficientMaxSum(arr):
    
    
    max_sum = -100
    for length in range(1,len(arr)):
        
        for i in range(len(arr)-length +1 ):
            
            print("Length",length,"index",i)
            
            temp_sum = sum(arr[i:i+length])
            if temp_sum > max_sum :
                max_sum = temp_sum
                print("MAX Length",length, "index", i)
                print(max_sum)
        
    return max_sum

print(inefficientMaxSum(arr))


## 분할정복, 탐욕, 재귀 이용한 해결
## 둘로 쪼갠후 왼쪽 배열 오른쪽 배욜 혹은 걸쳐 있다
## arr가 홀수 일 때 문제가 됨

def fastMaxSum(arr, low=0, high=len(arr)-1):

    print("starting Function ")
    mid = (low + high) //2

    if low == high:
        return arr[low]
    print("low,high,mid",low,high,mid)
    
        

    
    left_max, right_max = -100, -100
    left_sum, right_sum = 0, 0
    
    ### Left max
    ## 이거 짜는 거 각별히 주의!
    temp_arr = arr[low:mid]
    temp_arr = temp_arr[::-1]
    print(len(temp_arr))
    
    if len(temp_arr) == 0:
        left_max = max(left_max,arr[0])
    
    
    for i in range(len(temp_arr)):
        print(temp_arr)
        left_sum += temp_arr[i]
        print("left_sum",left_sum)

        left_max = max(left_max, left_sum)
    
    
    ### Right max
    temp_arr = arr[mid:high]
    
    if len(temp_arr) == 0:
        right_max = max(right_max, arr[-1])
    
    for i in range(len(temp_arr)):
        right_sum += temp_arr[i]
        right_max = max(right_max, right_sum)
        
    print("left,right",left_max,right_max)
    single = max(fastMaxSum(arr,low,mid),
                 fastMaxSum(arr,mid+1,high))
    
    print("single",single)
    return max(left_max + right_max, single)
        
print(fastMaxSum(arr))


## Dynamic Programming 으로 구현
## 최적화 때 배운 개념을 익히자!!

def fastestMaxSum(arr):
    length = len(arr)
    temp_sum = 0
    max_sum = -100
    
    for i in range(length):
        temp_sum = max(temp_sum,0) + arr[i]
        max_sum = max(temp_sum, max_sum)
    
    return max_sum
        
        
print("FastestMaxSum",fastestMaxSum(arr))

    

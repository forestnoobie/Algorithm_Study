# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:29:42 2018

@author: Nakyilkim
"""

## Linear 


## pg 620


arr = [1 for i in range(10)]

## Fail

def survive(N,K):
    
    start = 0
    arr[0] = 0
    
    while sum(arr) != 2:
        
        print("start while",start)
        cnt = 0
        while cnt != K :
            
            ## 이 부분 연결리스트로 구현해야..
            ## 리스트가 끝 부분으로 가면 이어 붙이자 
            for i in range(N):
                
                if i + start >= N : i = i +start - N
                
                else: i = i + start
                
                if arr[i] == 1 :
                    cnt +=1
                
                    if cnt == K:
                        print('kill index',i)
                        arr[i] = 0
                        start = i 
                        print("Killed",arr)
                        
                        break
    ret = []
    for i , j in enumerate(arr):
        if j == 1:
           ret.append(i) 
    

    return ret

#def survive_sol(N,K):
#    
#    survivors = [i for i in range(N)]
#    
#    kill = iter(survivors)
#    
#    while N >2:
#        
#        start = next(kill)
#        del(survivors[kill])
#        kill = survivors[kill]
#        
#        if kill ==
#    
#    
#    
#    return
    


## Pg 636
## 19.7
    
a0 = 1983

signal = [1983]

N = 10

signal = {}
signal[0] = 1983
signal[1] = (214013* signal[0] + 2531011)%2**32

## Offline Algorithm

def signalAnaylsis(arr, K):
    
    cnt = 0 
    for start, arr in enumerate(arr):
        for tail in range(start+1, len(arr)):
            temp_sum = sum(arr[start:tail])
            if temp_sum == K:
                cnt+=1
            if temp_sum >= K:
                break
                
    return cnt


## Online Algorithm

## iterator....
def signalAnaylsisOnline(arr,K):
    
    
    
    return cnt
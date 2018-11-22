# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:24:57 2018

@author: Nakyilkim
"""

### pg 178
### Divide and Conquer
### 약간 점화식 형태, 수식으로 표현되지 않는 문제를 
### 풀 때 이 원리가 유용하게 사용 ex ) 행렬 거듭제곱

### pg 195
### 7.5 FENCE
###판자를 많이 덮으면 -> 높이 낮아짐
### 조금 덮으면 -> 폭이 좁음
### 적절히 타협해야!

def bruthforce(num,heights):
    
    max_area = 0
    left_heights = len(heights)
    
    for startIndex in range(len(heights)-1):
        
        left_heights = len(heights) - startIndex 
        
        for width in range(startIndex+1,len(left_heights)):
            min_h = min(heights[startIndex : width])
            temp_area = min_h * (width-startIndex)
            
            if temp_area > max_area :
                max_area = temp_area
                print("Changing Max Area",max_area,startIndex,width)
                
            
## Divide and Conquer solution

def divide_solution(num,heights,start=0,end=len(heights)):
    
    ##  Finding Place to divide
    ## Recursion on left and right
    ## solving the middle part
    
    if start == end : return heights[start]

    midIndex = (start + end) // 2

    ## Index 헷갈리지  말것
    ## midIndex + 1 항상 해야!!!
    ## 왼쪽도 사실 midIndex까지 커버하기 떄문.. :midIndex랑 헷갈리지 말자
    ret = max(divide_solution(num,heights,start,midIndex),
              divide_solution(num,heights,midIndex+1,end))
     
    ## Solving middle Part : Try Every Length
    
    low = midIndex
    high = midIndex + 1
    temp_height = min(heights[low], heights[high])

    while(start < low or end > high):
        if end > high and heights[high+1] > heights[low-1]:
            high +=1
            temp_height = min(temp_height,heights[high])
            
        else:
            low -= 1
            temp_height = min(temp_height,heights[low])

        ret = max(ret, height * (high - low + 1))
    
    return ret

            
    

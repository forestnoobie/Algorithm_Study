# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:16:36 2018

@author: Nakyilkim
"""

### chapter 6 Recursion

## pg 149
## 크기 순서대로 숫자 뽑기

## 재귀적구조
### 파라미터:  전체 원소들 번호, 뽑힌 숫자들, 뽑아야될 숫자 갯수
### 함수가 한번 돌때 기존에 있던 숫자들 보다 큰 숫자들  선택한다
### 그리고 재귀 (다시 그 숫자보다 큰 수 선택) + pop(숫자를 빼면서 for문 돈다)
### sort해서 넣어야
######## 완전 탐색에 유용한 도구다!

def pick(totalNum, picked, toPick):
    
    ## Base, 더 이상 고를 원소가 업을 때
    if(toPick == 0):
        print(picked) # 목적이 프린트에 있으므로 따로 리턴값이 없다
        return 
    
    if len(picked) == 0:
        #index
        smallest = 0
    else:
        smallest = picked[-1] + 1
        
    for index in range(smallest, len(totalNum)):
        picked.append(index)
        pick(totalNum, picked, toPick -1)
        picked.pop()



### PG 150
### 보글게임
## 보드판 y,x에서 시작할 때        
## word가 존재하는 지 여부를 찾는 문제

## 1.  첫글자 확인
## 2. 인접 글자 중 둘째 글자 확인
## 3. 반복
        
## 기저사례
    # 1. 첫글자가 해당 위치 X
    # 2. 글자수 자체가 한 글자 짜리 일떼


#### 탐색을 위한 도구


def hasword(y,x, word, board):
    
    ## 책에서는 board 인자를 안 넣고
    ## 아래 값을 밖에서 선언해서 일단 안에 넣었음 (전역변수 처리해야 될 듯)
    dx = [-1,-1,-1, 1, 1, 1, 0, 0]
    dy = [-1, 0, 1,-1, 0, 1, -1, -1]
    
    if len(board[0]) <= x + 1 or len(board) < y +1:
        return False
    if board[x][y] != word[0]:
        return False
    if len(word) == 1:
        return True
    
    ###### 인접한 8칸 탐색하는 법 중요
    
    for direction in range(8):
        nextY = y + dy[direction]
        nextX = x + dx[direction]
        
        if(hasword(nextY,nextX, word[1:], board)):
            return True
    return




### 159 pg
### 6.4 풀이 : 소풍

### 첫 학생에게 친구인 짝을 만든다
### 남은 학생들 대해 친구인 짝을 만든다
### 반복
    
import random

random.seed(1234)
num_student = 4
areFriends = [[1 for i in range(num_student)] for j in range(num_student)]

taken = [False for i in range(10)]

def countPairs(num_student,taken):
    
    firstFree = -1
    
    for i in range(num_student):
        if taken[i] != 1:
            firstFree = i
            break
        
    ## 기저 사례
    if firstFree == -1 :
        return 1 # 한 가지 방법이 완성되는 것이므로
    ret = 0
    ## firstfree의 짝을 찾아주자
    print("FirstFree",firstFree)
    for pairs in range(firstFree+1, num_student):
        if taken[pairs] != True and areFriends[firstFree][pairs] == 1:
            taken[pairs] = True
            taken[firstFree] = True
            print("FirstFree, pairs",firstFree,pairs)
            ret += countPairs(num_student,taken)
            taken[pairs] = False
            taken[firstFree] = False
            
    return ret


## 6.5 게임판 덮기 159
    
# 점 x,y,가 주어질 때 덮는 경우의 수
## my_code 미완성



board = [[random.choice(["#","."]) for i in range(7)] for j in range(3)]

cover_type = [[(0, 0) , (1, 0) , (0,1)],
               [(0, 0), (-1, 0) , (0, 1)],
               [(0, 0), (-1, 0), (0, -1)],
               [(0, 0), (1, 0), (0, -1)]]


def checkAvaliable(board):
    
    avaliable_list = []
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            print("x,y",x,y)
            if board[x][y] == ".":
                possible = 0
                for _, block1, block2 in cover_type:
                    try:
                        x1 = x + block1[0]
                        y1 = y + block1[1]
                        
                        x2 = x + block2[0]
                        y2 = y + block2[1]
                        
                        ## 인덱스가 뒤로 넘어가는거 주의해야!
                        ## 인덱스가 양수라는 걸 조건으로 주어야..
                        
                        if x1>=0 and y1>=0 and x2 >=0 and y2 >=0  and board[x1][y1] == '.' and board[x2][y2] =='.':
                            print("Possible", x,y)
                            print("Possible Block Type", block1,block2)
                            possible = True
                    except IndexError:
                        pass
                        
                    if possible :
                        avaliable_list.append((x,y))                  
    return avaliable_list
      
## Avaliable_list 재귀적으로 이용?        
    


### 책 코드
cover_type = [[(0, 0) , (1, 0) , (0,1)],
               [(0, 0), (0, 1) , (1, 1)],
               [(0, 0), (1, 0), (1, 1)],
               [(0, 0), (1, 0), (1, -1)]]


### 덮었던 블록을 없애는 알고리즘

    




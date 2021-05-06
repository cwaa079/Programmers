#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    temp = {}
    for c, t in clothes:
        if t not in temp:
            temp[t] = 2 #초기화
        else:
            temp[t] += 1
    
    cnt = 1
    for num in temp.values():
        cnt *= num
    
    return cnt - 1

#https://programmers.co.kr/learn/courses/30/lessons/42586

import math
def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-x)/y) for x,y in zip(progresses, speeds)] #올림해서 한번에 구하기
    f = 0
    
    for i in range(len(progresses)):
        if progresses[f] < progresses[i]:
            answer.append(i-f)
            f = i
    answer.append(len(progresses)-f)
    
    return answer
  
  
"""
<같은 코드>
progresses = [math.ceil((100-x)/y) for x,y in zip(progresses, speeds)]
--------------------------------------------------------------------------------
for i in range(len(progresses)):
    progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])
"""

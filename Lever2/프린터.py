#https://programmers.co.kr/learn/courses/30/lessons/42587
#큐 쓰지 않고 리스트로 풀이
def solution(priorities, location):
    answer = []
    lists = [i for i in range(1, len(priorities)+1)]
    f = lists[location] #찾는 값

    while lists:
        idx = lists.pop(0) #시간복잡도가 N임 근데 popleft()는 1이므로 큐를 쓰면 줄일 수 있음
        l = priorities.pop(0)

        if not lists : 
            answer.append(idx)
            return answer.index(f)+1

        if max(priorities) > l:
            lists.append(idx)
            priorities.append(l)
        else:
            answer.append(idx)
            
            
#큐를 활용한 풀이
from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([v, i] for i, v in enumerate(priorities))
    
    while len(q):
        item = q.popleft()
        
        if q and max(q)[0] > item[0]:
            q.append(item)
        else:
            answer += 1 #이부분은 
            if item[1] == location:
                break
    return answer

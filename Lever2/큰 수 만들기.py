#https://programmers.co.kr/learn/courses/30/lessons/42883

"""
처음에 조합을 이용해서 푼 코드
하지만 number는 1자리 이상, 1,000,000자리 이하인 숫자라는 조건때문에
시간 초과
"""
from itertools import combinations
def solution(number, k):
    answer = ''
    
    comb = list(combinations(number, len(number)-k))
    temp = []
    for num in comb:
        temp.append(''.join(num))
    
    return max(temp)
  
  
"""
다른 사람 풀이 참고
stack 원리 이용
"""

def solution(number, k):
    stack = [number[0]]
    
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k>0:
            k -= 1 #하나 뺌
            stack.pop()
        
        stack.append(num)
    
    if k!=0: #'999'처럼 같은 수 일 때 그냥 제거
        stack = stack[:-k]
    
    return ''.join(stack)

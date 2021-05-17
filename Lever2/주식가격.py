#https://programmers.co.kr/learn/courses/30/lessons/42584

#내풀이
"""
완전탐색 -> O(n*n)
"""
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1 #당장 떨어지는 것이 아니기 때문
                break
    return answer
  
  
  #더효율적인 풀이
  """
  스택 사용 -> O(1)
  """
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # stack이 비었이면 false
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer

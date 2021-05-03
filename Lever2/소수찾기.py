#https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations
def solution(numbers):
    answer = []

    def check(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    for i in range(1, len(numbers)+1):
        temp = list(map(''.join, permutations(numbers, i)))
        for j in list(set(temp)):
            if check(int(j)):
                answer.append(int(j))

    return len(set(answer))
  
  #입력
  numbers = "17" / "011"

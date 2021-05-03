#https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''

    s = s.split()
    temp = [int(word) for word in s]

    answer += str(min(temp))
    answer += str(max(temp))

    return answer
  
s = "-1 -2 -3 -4"
print(solution(s))


#더 나은 풀이
def solution(s):
  answer = list(map(int, s.split()))
  return str(min(answer)) + " " + str(max(answer))

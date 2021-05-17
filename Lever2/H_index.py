#https://programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    answer = 0
    citations.sort(reverse=True) #내림차순 정렬
    i = 0
    
    for num in citations: #인용수와 논문수 비교
        i += 1
        if i == num:
            return i
        elif i > num:
            return i-1
        else:
            answer = i
    return answer
  
  
  #다른 사람 풀이
  #로직은 같지만 오름차순으로 함.
  def solution(ciations):
    citations.sort()
    l = len(citations)

    for i in range(l):
        if citations[i] >= l-i:
            return l-i

    return 0

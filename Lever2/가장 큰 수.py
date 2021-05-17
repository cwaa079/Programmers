#https://programmers.co.kr/learn/courses/30/lessons/42746

#처음에 푼 코드 -> 시간초과
def solution(numbers):
    temp = list(permutations(numbers, len(numbers))) #numbers의 길이가 1 이상 100,000 이하라서 시간초과
    answer = []
    for num in temp:
        n = ''
        for i in num:
            n += str(i)
        answer.append(n)

    return str(max(answer))
  
  
  #해설을 통해 푼 코드
  def solution(numbers):
    
    num = list(map(str, numbers))
    num.sort(key = lambda x:x*3, reverse = True) #1000이하이므로 문자열 하나*3을 해줌
    #문자열 비교는 첫번쨰 인덱스를 ASCII로 비교
    
    return str(int(''.join(num)))

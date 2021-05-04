#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    
    hashmap = {} #딕셔너리의 key-value 이용
    for num in phone_book:
        hashmap[num] = 1 #key의 값이 존재한다를 저장
    
    for num in phone_book:
        temp = ""
        for i in num:
            temp += i
            #현재 검사하는 문자열이 key로 존재하는데 자기자신이 아니라면
            if temp in hashmap and temp != num: 
                answer = False
    
    return answer
  
  #입력
  phone_book = ["119", "97674223", "1195524421"]

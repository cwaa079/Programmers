#https://programmers.co.kr/learn/courses/30/lessons/43163
#BFS로 풀이
from collections import deque

def solution(begin, target, words):
    visited = [False] * len(words)
    
    if target not in words: #words안에 없는 경우
        return 0
    
    def check(now, word): #서로 다른 문자 수 리턴
        cnt = 0
        for i in range(len(now)):
            if now[i] != word[i]: cnt+=1
        return cnt
            
    
    def bfs(start, visited):
        q = deque([[start, 0]])
        
        while q:
            now, d = q.popleft()
            
            if now == target:	# target을 찾으면 depth 리턴 후 종료
                return d
            
            for i in range(len(words)):
                if visited[i]==False and check(now, words[i])==1:
                    q.append([words[i], d+1])
                    visited[i] = True
        
    return bfs(begin, visited)
  
  
#DFS로 풀이
def solution(begin, target, words):
    visited = [False] * len(words)
    mins = 1e9
    if target not in words:  # words안에 없는 경우
        return 0

    def check(now, word):  # 서로 다른 문자 수
        cnt = 0
        for i in range(len(now)):
            if now[i] != word[i]: cnt += 1
        return cnt

    def dfs(word, idx, visited):
        nonlocal mins
        if target == word:
            mins = min(mins, idx)
            return
        for i in range(len(words)):
            if visited[i] == False and check(word, words[i]) == 1:
                visited[i] = True
                dfs(words[i], idx+1, visited)
                visited[i] = False #돌아오고 나서 visited 처리 유의!!!

    dfs(begin, 0, visited)
    return mins

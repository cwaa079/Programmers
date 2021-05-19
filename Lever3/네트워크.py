#https://programmers.co.kr/learn/courses/30/lessons/43162

#DFS로 푼 코드
def solution(n, computers):
    answer = 0
    
    def dfs(v, visited):
        visited[v] = True
        for i in range(len(computers)):
            if visited[i]==False and computers[v][i] == 1:
                dfs(i, visited)
    
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited) #재귀로 이동가능한 경로 찾음
            answer += 1
            
    return answer
  
  
  #BFS로 푼 코드
from collections import deque
def solution(n, computers):
    answer = 0
    
    def bfs(v, visited):
        visited[v] = True
        q = deque([v])
        while q:
            now = q.popleft()
            for i in range(n):
                if visited[i]==False and computers[now][i]==1:
                    q.append(i)
                    visited[i]=True
                
    visited = [False] * n
    for i in range(n):
        if visited[i] == False:
            bfs(i, visited)
            answer += 1
            
    return answer

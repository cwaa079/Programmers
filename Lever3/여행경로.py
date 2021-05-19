#https://programmers.co.kr/learn/courses/30/lessons/43164
"""
BFS로 풀기 시도했으나 최적의 경로만을 찾는 BFS로는 이 문제를 풀 수 없었음.(알파벳 순서때문)
DFS로 모든 경로를 탐색하되 sort를 통해 미리 오름차순 정렬을 해둔 알고리즘 사용.
"""
from copy import deepcopy
def solution(tickets):
    answer = []
    temp = [] #임시 배열
    visited = [False] * len(tickets) #방문 여부
    start = tickets[0][0] #시작하는 도시
    tickets.sort() #오름차순 정렬

    def dfs(now, d, visited):
        nonlocal answer
        temp.append(now)
        if d == len(tickets):
            answer = deepcopy(temp)
            return True
        for i in range(len(tickets)):
            if tickets[i][0] == now and visited[i] == False:
                visited[i] = True
                if dfs(tickets[i][1], d+1, visited): return True
                visited[i] = False
        temp.pop()
        return False

    dfs(start, 0, visited)
    return answer

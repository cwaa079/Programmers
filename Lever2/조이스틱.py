#https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    answer = 0
    change = [min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1) for spell in name]
    answer += sum(change)

    idx = 0
    while True:
        change[idx] = 0
        if sum(change) == 0: break
        left, right = 1, 1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right

    return answer
  
#입력
name = 'JEROEN'
print(solution(name))

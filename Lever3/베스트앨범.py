#https://programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict
def solution(genres, plays):
    answer = []
    genres_plays = defaultdict(list) #키 : 장르별로 나눈 플레이횟수, 고유번호
    cnt_genres = defaultdict(lambda: 0) #키 : 각 장르별 총 플레이횟수 합계

    index = 0 #고유번호
    for genre, play in zip(genres, plays):
        cnt_genres[genre] += play
        genres_plays[genre].append((play, index))
        index += 1

    #정렬
    genres_order = sorted(cnt_genres.keys(), key=lambda x:cnt_genres[x], reverse=True)

    for genre in genres_order:
        #같은 키를 가지고 있는 value끼리 정렬(2개만)
        temp = sorted(genres_plays[genre], key=lambda x: x[0], reverse=True)
        for i in range(len(temp)):
            if i == 2: break #2개까지만 추출하기 위해
            answer.append(temp[i][1])

    return answer

#입력
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

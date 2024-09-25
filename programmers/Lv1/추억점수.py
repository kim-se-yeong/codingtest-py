# https://school.programmers.co.kr/learn/courses/30/lessons/176963

# 사고
# 1. name 과 yearning의 관계를 dictionary 로 정의한다.
# 2. photo 를 순회하면서 dictionary 에서 점수를 가져와서 계산한다.

def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    
    for p in photo:
        r = 0
        for name in p:
            if name in dic:
                r += dic[name]
        answer.append(r)
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))
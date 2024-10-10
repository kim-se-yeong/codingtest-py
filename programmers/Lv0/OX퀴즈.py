# https://school.programmers.co.kr/learn/courses/30/lessons/120907?language=python3

# 풀이 사고 (10분)
# 1. 문자열 공백 기준으로 자르기
# 0번 인덱스 -> x
# 1번 인덱스 -> 연산자
# 2번 인덱스 -> y
# 4번 인덱스 -> z

def solution(quiz):
    answer = []
    
    for q in quiz:
        s = q.split(" ")
        x = int(s[0])
        op = s[1]
        y = int(s[2])
        z = int(s[4])
        
        result = cal(x, y, op)
        if result == z:
            answer.append('O')
        else:
            answer.append('X')
    return answer

def cal(x, y, op):
    answer = 0
    if op == '+':
        answer = x + y
    else:
        answer = x - y
    return answer

quiz = ["3 - 4 = -3", "5 + 6 = 11"]
print(solution(quiz))
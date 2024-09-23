# https://softeer.ai/practice/6269/talk?page=0

import sys

m, n, k = map(int, sys.stdin.readline().split())
# 사용자의 버튼 조작이 비밀메뉴 조작법보다 짧은 경우
if n < m:
    print("normal")
    sys.exit()

secret_op = list(map(int, sys.stdin.readline().split()))
user_button_op = list(map(int, sys.stdin.readline().split()))

# 내 풀이
def solution():
    issecret = False
    for i in range(n - m + 1):
        if user_button_op[i] == secret_op[0]:
            issecret = True
            for j in range(m):
                if user_button_op[i + j] != secret_op[j]:
                    issecret = False
                    break
            if issecret:
                break
    if issecret:
        print("secret")
    else:
        print("normal")
    
# 다른 사람 풀이_1 (join 함수 사용..)
# def solution_1():
#     secret_key = "".join(list(map(str,input().split())))
#     user_input = "".join(list(map(str,input().split())))

#     if secret_key in user_input:
#         print("secret")
#     else:
#         print("normal")
    
# 다른 사람 풀이_2 (슬라이싱 사용..)
# def solution_2():
#     is_secret = False
#     for i in range(n - m + 1):
#         if user_button_op[i:i + m] == secret_op:
#             is_secret = True
#             break

#     if is_secret:
#         print("Secret pattern found!")
#     else:
#         print("No secret pattern.")

solution()
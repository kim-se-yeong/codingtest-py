import sys

n = int(sys.stdin.readline())

# 파이썬에서는 리스트로 스택 구현이 가능하다.
stack = []

for i in range(n):
    command = list(map(int, sys.stdin.readline().split()))
    num = command[0]
    if num == 1:
        stack.append(command[1])
    elif num == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif num == 3:
        print(len(stack))
    elif num == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif num == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
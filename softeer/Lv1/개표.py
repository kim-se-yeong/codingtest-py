# https://softeer.ai/practice/7698
import sys

t = int(sys.stdin.readline())
result = []

# 5로 나누었을 때
for i in range(t):
    n = int(sys.stdin.readline())
    n1 = int(n / 5)
    n2 = int(n % 5)
    result.append(("++++ " * n1) + ("|" * n2))
    
for i in range(t):
    print(result[i])

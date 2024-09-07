# https://www.acmicpc.net/problem/1764
import sys

n, m = map(int, sys.stdin.readline().split())
arr = {}
for i in range(n):
    name = sys.stdin.readline()
    arr[name] = i # value 는 임의로 index 값을 넣음

result = []
for i in range(m):
    name = sys.stdin.readline()
    if name in arr:
        result.append(name)
        
result.sort()
print(len(result))
print(''.join(result), end='')
# for i in result:
#     print(i)

# 다른 사람 풀이
# arr1 = []
# for i in range(n):
#     name = sys.stdin.readline()
#     arr1.append(name)
# arr2 = []
# for i in range(m):
#     name = sys.stdin.readline()
#     arr2.append(name)

# answer = list(set(arr1) & set(arr2))

# print(len(answer))
# print(''.join(answer), end='')

# https://softeer.ai/practice/7353
n = int(input())
_list = list(map(int, input().split()))

_list.sort()

r1 = _list[0] * _list[1]
r2 = _list[-1] * _list[-2]
print(max(r1, r2))
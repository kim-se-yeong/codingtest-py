# https://softeer.ai/practice/9657

import sys
n, m = map(int, sys.stdin.readline().split())

_map = []
for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    _map.append(line)
    
l1, r1 = map(int, sys.stdin.readline().split())
l2, r2 = map(int, sys.stdin.readline().split())

# 행 별로 돌면서 파괴범을 만났을 경우 0으로 변경하고, 다음 행을 탐색한다.
def attack(start_row, end_row):
    for i in range(l1 - 1, r1):
        for j in range(m):
            if _map[i][j] == 1:
                _map[i][j] = 0
                break

attack(l1, r1)
attack(l2, r2)

# 모든 맵을 탐색하면서 파괴범의 수를 가져온다.
cnt = sum(row.count(1) for row in _map)
print(cnt)
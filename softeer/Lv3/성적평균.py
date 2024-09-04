# https://softeer.ai/practice/6294
import sys

n, k = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())

    avg = sum(scores[x-1:y]) / (y - x + 1)
    print(f"{avg:.2f}")

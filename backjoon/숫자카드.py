import sys

n = sys.stdin.readline()
sg = set(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()
cards = list(map(int, sys.stdin.readline().split()))

result = []
for c in cards:
    if c in sg:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))
# https://softeer.ai/practice/7626
import sys

n = int(sys.stdin.readline())
positions = list(map(int, sys.stdin.readline().split()))

dis = []

for i in range(1, len(positions)):
    dis.append(positions[i] - positions[i-1])
    
mindis = min(dis)
print(dis.count(mindis))
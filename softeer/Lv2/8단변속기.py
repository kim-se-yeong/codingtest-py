# https://softeer.ai/practice/6283
import sys

numbers = list(map(int, sys.stdin.readline().split()))
ascending = sorted(numbers)
descending = sorted(numbers, reverse=True)

if numbers == ascending:
    print("ascending")
elif numbers == descending:
    print("descending")
else:
    print("mixed")
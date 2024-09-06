# https://www.acmicpc.net/problem/10808

# 1. 알파벳 개수만큼 배열 생성하기
# 2. 입력받은 문자열을 순회한다.
# 3. 각 알파벳에서 'a'를 빼준 값이 인덱스 이므로, 각 인덱스의 값을 1씩 증가시킨다.

alphabet = [0] * 26

s = input()
for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    alphabet[idx] += 1
    
for i in range(len(alphabet)):
    print(alphabet[i], end=' ')
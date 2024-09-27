# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    dic = {}
    
    for key in keymap:
        # enumerate 함수를 이용해서 인덱스를 사용한다.
        # start 옵션을 1로주면 idx는 1부터 시작하므로, idx + 1을 해주지 않아도 된다.
        # for idx, char in enumerate(key, start=1):
        for idx, char in enumerate(key):
            # 만약 dic에 char이 없으면 추가한다. key: char, value: idx + 1
            if char not in dic:
                dic[char] = idx + 1
            else:
                dic[char] = min(dic[char], idx + 1)
        
    for target in targets:
        count = 0
        
        for char in target:
            # dic에 char이 있으면 값을 가져와 count에 더한다.
            if char in dic:
                count += dic[char]
            else:
                count = -1
                break
        answer.append(count)
    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(solution(keymap, targets))
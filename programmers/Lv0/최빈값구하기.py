# https://school.programmers.co.kr/learn/courses/30/lessons/120812?language=python3

# 풀이 사고 (30분)
# 1. array 길이만큼 카운트 배열을 만든다.
# -> 원소의 크기만큼 카운트 배열을 만들어야 한다.
# -> 만약 array = [1, 20, 999, 999, 20] 이라고 했을 때 array 길이는 5이지만, 원소의 최대 크기는 999이므로 원소의 최대 크기만큼 배열의 길이를 초기화해야한다.
# 2. array의 원소는 result의 인덱스가되고, 개수만큼 카운트를 증가한다.
# 3. result의 가장 큰 값을 가지고 있는 인덱스를 가져온다.

# 틀린 부분
# 1. 원소를 index 로 설정했으니, index를 가져와야하는데 개수를 가져와서 틀림.
# 2. 정렬을 해서 0, 1 인덱스의 값을 비교했음, 인덱스는 변경되고 값을 가져오게 되는 코드로 틀림.
def solution(array):
    answer = 0
    
    # 카운트 배열 생성하기
    result = [0] * 1000
    
    print(len(result))
    
    # 원소별로 개수 세기
    for i in array:
        result[i] += 1

    # 인덱스를 가져와야 함.
    # 최대 값 가져오기
    max_value = max(result)
    max_value_count = result.count(max_value)
    
    if max_value_count > 1:
        answer = -1
    else:
        answer = result.index(max_value)
    return answer


array = [1, 1, 1, 1, 2, 2, 3, 3, 3]
print(solution(array))
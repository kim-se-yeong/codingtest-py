# https://school.programmers.co.kr/learn/courses/30/lessons/250121

# 출력 조건
# data에서 ext값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순으로 정렬

# 풀이 사고 (30분)
# 1. data 배열을 순회한다.
# 2. 기준에 대한 값을 찾는다.
# 3. 기준이 되는 값과 데이터에서 기준에 대한 값을 비교한다.
# **** 인덱스 활용 ****

# 다시 보기
# 정렬하는 코드 알기
def solution(data, ext, val_ext, sort_by):
    answer = []
    
    ext_dic = {"code": 0,
               "date": 1,
               "maximum": 2,
               "remain": 3}
    
    # 기준 데이터의 인덱스
    ext_idx = ext_dic[ext]
    sort_idx = ext_dic[sort_by]
    
    for element in data:
        # 기준 데이터와 비교할 값 가져오기
        value = element[ext_idx]
        
        # 비교하기
        if value <= val_ext:
            answer.append(element)
    
    return sorted(answer, key=lambda answer: answer[sort_idx])

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

print(solution(data, ext, val_ext, sort_by))
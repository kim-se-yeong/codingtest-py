# https://school.programmers.co.kr/learn/courses/30/lessons/340213

# 소요 시간 (45분)

# 조건 잘 못 체크함. prev 조건에 next 조건을 구현함

# 조건
# prev : 현 위치에서 10초전으로 이동하는데 현재 위치가 10초 미만이면 처음위치로
# next : 현 위치에서 10초후로 이동하는데 마지막 위치는 동영상 길이이다.
# 오프닝 건너뛰기 : op_start <= 현위치 <= op_end 경우 오프닝 끝나는 위치로 이동
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len = time_to_seconds(video_len)
    # 현재 위치 초로 바꿈
    pos = time_to_seconds(pos)
    
    op_start = time_to_seconds(op_start)
    op_end = time_to_seconds(op_end)
    
    for command in commands:
        # 오프닝 구간인지 확인        
        if op_start <= pos <= op_end:
            pos = op_end
            
        if command == "prev":
            # 10초 전으로 이동
            if pos < 10:
                pos = 0
            else:
                pos -= 10
        else:
            # 10초 후로 이동
            pos += 10
            pos = min(pos, video_len)
            
    if op_start <= pos <= op_end:
            pos = op_end

    # 현재 위치 mm:ss 로 나타내기
    answer = second_to_time(pos)
    return answer

def second_to_time(time):
    # 몫:분, 나머지:초
    # m = str(time // 60)
    # s = str(time % 60)
    
    # m = "0" + m if len(m) == 1 else m
    # s = "0" + s if len(s) == 1 else s
    m, s = divmod(time, 60)
    return f"{m:02}:{s:02}"

def time_to_seconds(time):
    m, s = map(int, time.split(":"))
    return m * 60 + s

video_len = "07:22"
pos = "04:05"
op_start = "00:15"
op_end = "04:07"
commands = ["next"]
print(solution(video_len, pos, op_start, op_end, commands))
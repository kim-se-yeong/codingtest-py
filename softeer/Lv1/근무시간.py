# https://softeer.ai/practice/6254
times = []
for i in range(5):
    start, end = input().split()
    times.append([start, end])

# 1시간 60분
# 10시간 600분
# 19시간 60 * 19 = 1140
# 1100 - 600 = 540

answer = 0
for start, end in times:
    starthour, startminute = map(int,start.split(":"))
    endhour, endminute = map(int, end.split(":"))
    
    # 시간을 분으로 변환
    starthour = starthour * 60
    endhour = endhour * 60
    
    t = (endhour + endminute) - (starthour + startminute)
    answer += t
print(answer)
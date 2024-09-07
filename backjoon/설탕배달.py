n = int(input())

answer = 0
while n >= 0:
    if n % 5 == 0:
        answer += int(n // 5)
        print(answer)
        break # 여기서 루프가 종료되면 else 블록은 실행되지 않음
    n -= 3
    answer += 1
else:
    print(-1) # 루프가 끝까지 돌고 break로 종료되지 않으면 else가 실행됨
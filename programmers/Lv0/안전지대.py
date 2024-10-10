# https://school.programmers.co.kr/learn/courses/30/lessons/120866

# 풀이 사고 (40분)
# 1. 보드를 순회하면서 지뢰를 찾는다.
# 2. 지뢰를 찾으면 상,하,좌,우,대각선에 대하여 위험지역으로 분류한다.
# 3. 보드를 순회하면서 안전지역에 대하여 카운트한다.

# 틀린 부분
# 1. 위험지역으로 분류할 때, 지뢰번호인 1로 설정하여 결과값 틀림
# 2. 범위 확인할 때 조건 잘못 체크하여 결과값이 항상 (n * n) - 지뢰 개수로 나옴.

def solution(board):
    answer = 0
    
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                y, x = i, j
                
                # 8방향으로 탐색
                for k in range(8):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    
                    # 범위를 벗어나면 패스
                    if ny > 0 or ny <= n or nx > 0 or nx <= n:
                        continue
                    
                    # 지뢰면 패스
                    if board[ny][nx] == 1:
                        continue

                    # 위험지역으로 분류
                    board[ny][nx] = 2
                    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    return answer

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
print(solution(board))
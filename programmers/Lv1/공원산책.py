# https://school.programmers.co.kr/learn/courses/30/lessons/172928

# 사고
# 1. park 기반으로 map 을 만든다.
# 2. 동서남북에 대한 이동 좌표를 만든다.
# 3. 시작 지점을 찾는다.
# 4. routes 기반으로 맵을 탐색한다.

# 북, 동, 남, 서
direction = {"N": [-1, 0],
             "E": [0, 1],
             "S": [1, 0],
             "W": [0, -1]}

def solution(park, routes):
    
    # park 기반으로 map 생성
    _map = [list(p) for p in park]
    
    # 시작 지점 가져오기
    x, y = get_start(_map)
    
    # 주어진 routes 기반으로 맵 탐색
    for route in routes:
        direct, dist = route.split(" ")
        dist = int(dist)
        
        dx, dy = direction[direct]
        nx, ny = x, y
        
        can_move = True
        # 거리만큼 이동하기
        for _ in range(dist):
            nx += dx
            ny += dy
            
            # 이동이 가능한지
            if nx < 0 or nx >= len(_map) or ny < 0 or ny >= len(_map[0]) or _map[nx][ny] == 'X':
                can_move = False
                break
            
        # 거리만큼 이동하는데 모두 갈수있어야지만 위치를 업데이트 할 수 있다.
        if can_move:
            x, y = nx, ny

    return [x, y]
    
def get_start(_map):
    for i in range(len(_map)):
        for j in range(len(_map[0])):
            if _map[i][j] == 'S':
                return i, j
        
park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

print(solution(park, routes))
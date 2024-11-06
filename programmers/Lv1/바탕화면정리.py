# https://school.programmers.co.kr/learn/courses/30/lessons/161990

# 소요 시간 (1시간)
# 다시 보기
# 컴프리헨션 사용 방법
# 리스트에 여러 원소 추가하는 방법 'extend'
# 
def solution(wallpaper):
    answer = []
    wall_paper_map = [list(line) for line in wallpaper]
    
    # 위치 초기화
    lux, luy = len(wall_paper_map), len(wall_paper_map[0])
    rdx, rdy = 0, 0
    
    for i in range(len(wall_paper_map)):
        for j in range(len(wall_paper_map[0])):
            if wall_paper_map[i][j] == '#':
                # 시작 위치 비교하기
                lux, luy = min(i, lux), min(j, luy)
                
                # 끝 위치 비교하기
                rdx, rdy = max(i+1, rdx), max(j+i, rdy)
                
    answer.extend([lux, luy, rdx, rdy])
    return answer

wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
print(solution(wallpaper))
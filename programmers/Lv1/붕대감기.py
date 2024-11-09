# 조건
# t초 동안 붕대 감으면 1초마다 x 회복
# t초 동안 연속 붕대 감는데 성공하면 y만큼 추가 회복
# 기술 도중 몬스터 공격 맞으면 기술 취소
# 공격 당하는 순간 체력 회복할 수 없음
# 몬스터에게 공격당해 기술 취소 시 붕대감기 다시 사용하면 연속 시간이 0으로 초기화됨
# 몬스터 공격 받을 시 피해량만큼 체력이 줄어듬
# 체력이 0이하면 죽음
# bandage : [기술 시전시간, 1초당 회복량, 추가 회복량]
# attacks : [몬스터 공격시간, 피해량]
# health = 최대 체력량

# 체력을 구하자!
def solution(bandage, health, attacks):
    
    # 최대 체력 저장하기
    max_health = health
    # 스킬 타임
    skill_time = 0
    
    # 몬스터의 마지막 공격까지의 체력을 확인한다.
    attack_dic = {row[0]: row[1] for row in attacks}
    print(attack_dic)
    
    # 마지막 공격 시간
    last_attack_time = attacks[-1][0]
    # 마지막 공격한 시간까지 시간별로 확인한다.
    for time in range(last_attack_time + 1):
        
        # 해당 시간에 공격이 있었다면
        if time in attack_dic:
            # 공격하기
            health -= attack_dic[time]
            skill_time = 0
            
            # 만약 체력이 0 이하로 떨어지면 죽음
            if health <= 0:
                return -1
        
        # 해당 시간에 공격이 없었다면
        else:
            # 체력이 최대인지 확인하기
            if max_health <= health:
                continue
            
            # 체력 회복하기
            health = min(max_health, health + bandage[1])
            # health += bandage[1]
            skill_time += 1
            
            # 시전 시간 확인해서 추가 회복량 주기
            if skill_time >= bandage[0]:
                health = min(max_health, health + bandage[2])
                skill_time = 0

    return health

bandage = [3, 10, 1]
health = 100
attacks = [[1,5],[3,5]]
print(solution(bandage, health, attacks))
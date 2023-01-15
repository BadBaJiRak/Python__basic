'''
    택시 이동 거리에 따른 요금을 구하세요
    
    기본 요금은 5,000 원이며
    구간당 10km 당 1000원의 추가요금이 발생하며
    
    오후 10시 ~ 오전 6시 사이에는 
    10km 당 1000원의 추가요금을 부과하세요
        거리        요금        할증
       0  ~ 10     5,000        0
       11 ~ 20     6,000        10 km당 350원 추가
       21 ~ 30     7,000
       31 ~ 40     8,000
       ...
'''
time = int(input('현재 시간만 입력 하세요 (1 ~ 24 시간) : '))
travelRange = (int(input('이동할 거리를 입력 하세요 : ')))
fee = 5000

addRange = travelRange - 10

print(addRange // 10)                       # 추가로 이동한 거리를 10으로 나눈 몫을 구한다
print(1000 * (addRange // 10))              # 10 km 단위 요금
print(5000 + 1000 * (addRange // 10))       # 기본요금 + 추가요금 10km 단위

print(addRange // 10 + 1 )                  # 추가로 이동한 거리를 10으로 나눈 몫에다가 + 1을 한다
print(1000 * (addRange // 10 + 1 ))         # 01 ~ 09 km 단위 요금 
print(5000 + 1000 * (addRange // 10 + 1 ))  # 기본요금 + 추가요금 1~9km

if travelRange <= 10:
    fee = 5000

else:

    if travelRange % 10 > 0:
        if 22 <= time <= 24 or 1 <= time <= 6:
            fee = 5000 + 1000 * (addRange // 10 + 1) + 350 * (addRange // 10 + 1)
        else: fee = 5000 + 1000 * (addRange // 10 + 1)

    else :
        fee = 5000 + 1000 * (addRange // 10)

print(f'{travelRange} km 를 이동했으며 요금은 {fee} 원 입니다')


# hmm ....
'''
    이용시간에 따른 요금을 계산합니다
    구간을 나누어서, 구간마다 500원이 추가로 부과됩니다

    기본 이용요금은 3000원이고,
    구간당 500원의 추가요금이 발생합니다

        시간        요금
        0 ~ 30      3,000
        31 ~ 40     3,500
        41 ~ 50     4,000
        ...
'''
from os import system

minute = (int(input('이용시간 입력 : ')))
addTime = minute - 30

if minute <= 30:
    fee = 3000

else:
    # 최종요금 = 기본요금 + 추가요금
    # 시간에 따라서, 추가요금이 발생하니까
    # n은 minute을 이용하여 계산해야 한다

    if minute % 10 != 0:    # 시간이 10으로 나누어 떨어지는가
        fee = 3000 + 500 * (addTime // 10 + 1)
    else:                   # 시간이 10으로 나누어 떨어지지 않는가
        fee = 3000 + 500 * (addTime // 10)


'''
if time > 30:
    if time % 10 != 0:             # 시간이 10으로 나누어 떨어지는가
        

    else:           # 시간이 10으로 나누어 떨어지지 않는가
        pass
    
'''
print('이용시간은 {}분 요금은 {}원 입니다'.format(minute,fee))

input()
system('cls')

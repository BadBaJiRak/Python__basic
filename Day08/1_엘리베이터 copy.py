'''
    현재 층수를 입력 받아서, 
    가장 가까운 엘리베이터가 이동하는
    코드를 만들어 보세요
'''
import random
from os import system
e1 = random.randrange(1,16)
e2 = random.randrange(1,16)
e3 = random.randrange(1,16)

# mov = e1

print(f'A : {e1}층, B : {e2}층, C : {e3}층')

# 1) 사용자에게 현재 층 수를 입력받는다
currentFloor = int(input('층 입력 : '))

# 2) 각 엘리베이터와 현재 층수의 거리를 구한다

d1 = currentFloor - e1  # 차이를 구하고
d2 = currentFloor - e2
d3 = currentFloor - e3

if d1 < 0: d1 = -d1     # 절댓값으로 처리한다
if d2 < 0: d2 = -d2
if d3 < 0: d3 = -d3

# d1이 음수인것과 상관없이, 이후 d2나 d3도 검사해야한다


# 3) 구해진 3개의 거리값 중 가장 작은 값을 구한다
minDistance = d1

if d2 < minDistance:    minDistance = d2
if d3 < minDistance:    minDistance = d3

# 4) 거리가 최소인 엘리베이터를 화면에 출력한다
# ex) A 엘리베이터가 이동합니다
# ex) B 엘리베이터가 이동합니다
# ex) C 엘리베이터가 이동합니다

if minDistance == d1: print('A', end = '')
elif minDistance == d2: print('B', end = '')
else:   print('C', end = '')

print('엘리베이터가 이동합니다')

input()
system('cls')


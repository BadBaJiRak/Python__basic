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
my = int(input('층 입력 : '))

# 2) 각 엘리베이터와 현재 층수의 거리를 구한다
e1 = my - e1
e2 = my - e2
e3 = my - e3

#if my > e1:
#    e1 = e1
if my < e1:
    e1 = -e1

#if my > e2:
#    e2 = e2
if my < e2:
    e2 = -e2

#if my > e3:
#    e3 = e3
if my < e3:
    e3 = -e3

if e1 < 0:
    e1 = -e1
if e2 < 0:
    e2 = -e2
if e3 < 0:
    e3 = -e3

'''
print('A는 {}층 차이난다',e1)
print('B는 {}층 차이난다',e2)
print('C는 {}층 차이난다',e3)
'''


# 3) 구해진 3개의 거리값 중 가장 작은 값을 구한다

if e2 > e1 < e3:
    a = 'A'
elif e1 > e2 < e3:
    a = 'B'
else:
    a = 'C'

if e1 == e2:
    a = 'A'
if e2 == e3:
    a = 'B'
if e1 == e3:
    a = 'A'

# 4) 거리가 최소인 엘리베이터를 화면에 출력한다
# ex) A 엘리베이터가 이동합니다
# ex) B 엘리베이터가 이동합니다
# ex) C 엘리베이터가 이동합니다

print('{:s} 엘리베이터가 이동합니다.'.format(a))

input()
system('cls')
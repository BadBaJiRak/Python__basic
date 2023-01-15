'''
엘리베이터 문제
현재 건물에는 엘리베이터가 2대 있고
A는 5층 B는 7층에 있다

현재 내가 있는 층수를 눌러 가장 가까운 엘리베이터를 움직이시오
(층 수의 차이가 같을경우 B 엘리베이터가 움직인다.)
*절대값 사용
'''

elA = 5
elB = 7

me = int(input('현재 층 수를 입력 하세요 : '))

elA -= me
elB -= me

if elA < 0:
    elA = -elA
if elB < 0:
    elB = -elB


if elA < elB:
    mov = 'A'
elif elB < elA:
    mov = 'B'
else:
    mov = 'B'

print(f'{mov} 엘리베이터가 움직입니다.')
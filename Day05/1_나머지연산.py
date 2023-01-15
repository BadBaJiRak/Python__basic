# from은 random 모듈에서 randrange를 불러와서 사용할 수 있게 한다.
from random import randrange

# 1) 홀짝 구분 가능
n1 = randrange(1, 100)

if n1 % 2 == 0:
    print('{} : {}'.format(n1, '짝수'))

if n1 % 2 != 0:
    print('{} : {}'.format(n1, '홀수'))

print('=' * 25)

# 2) 배수 확인 가능
n2 = randrange(1,100)
if n2 % 3 == 0:
    print('{} : 3의 배수입니다'.format(n2))

if n2 % 3 != 0:
    print('{} : 3의 배수가 아닙니다'.format(n2))

print('='*25)

# 3) 특정 범위 내의 값 추출 가능
n3 = randrange(1000)
t1 = n3 % 6         # 0 ~ 5
t2 = n3 % 11        # 0 ~ 10
t3 = n3 % 10 + 10   # (0 ~ 9) + 10 = 10 ~ 19
print('t1 (6보다 작은 수) : {}'.format(t1))
print('t2 (11보다 작은 수) : {}'.format(t2))
print('t3 (10이상 20미만의 수) : {}'.format(t3))
print('='*25)

# 4) 정수의 자릿수 구분 가능
n4 = randrange(1000000)
print('t4 : ', n4)
t1 = n4 % 10        # 0 ~ 9
t2 = n4 % 100       # 0 ~ 99
t3 = n4 % 1000      # 0 ~ 999

print('t1 : ', t1)
print('t2 : ', t2)
print('t3 : ', t3)
print('='*25)


# 5) 가상의 주민등록번호 자릿수 구분하기
idnumber = 9506231234567
num1 = idnumber // 10000000
num2 = idnumber % 10000000
f1 = idnumber / 10000000
print('num1 : ',num1)
print('num2 : ',num2)
print('f1 : ',f1)
print()
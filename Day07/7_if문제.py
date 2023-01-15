from os import system
# os 모듈에서 system을 가져와서 사용한다
#system(cmd) : cmd에 문자열로 명령어를 입력하면 운영체제 명령 실행
system('cls') # 출력창 청소

print('정수 하나를 입력받아 5의 배수인 경우 출력')

num1 = int(input('정수 입력 : '))

if (num1 % 5 == 0):
    print(num1,'은(는) 5의 배수가 맞습니다')
else:
    print('5의 배수가 아닙니다')

input()
system('cls')

print('정수 하나를 입력받아 홀 짝 구분')

num2 = int(input('정수 입력 : '))

if (num2 % 2 == 0):
    a1 = '짝수'
else:
    a1 = '홀수'

print(a1)

input()
system('cls')

print('두 수를 입력받아 첫번째 수가 두번째 수의 배수인지 출력')

num3, num4 = map(int,input('두 수를 입력하세요 : ').split())

if(num3 % num4 == 0):
    a2 = '배수 맞음 ㅇㅇ'
else:
    a2 = '배수 아님 ㄴㄴ'

print(a2)

input()
system('cls')

print('두 수를 입력받아 더 큰수가 짝수이면 출력')
num5, num6 = map(int,input('두 수를 입력하세요 : ').split())
bigN3 = num5 > num6
bugN4 = num6 > num5

if num5 > num6 and num5 % 2 == 0:
    a3 = num5 
    print('{}는(은) 짝수이면서 더 큰수'.format(a3))
elif num6 > num5 and num6 % 2 == 0:
    a3 = num6 
    print('{}는(은) 짝수이면서 더 큰수'.format(a3))


input()
system('cls')

print('두 수를 입력받아 합이 짝수이고, 3의 배수인 수를 출력')

num7, num8 = map(int,input('두 수를 입력하세요 : ').split())
a4 = num7 + num8
if a4 % 2 == 0 and a4 % 3 == 0:
    a5 = a4 * 3
else :
    a5 = '홀수입니다'
print(a5)

input()
system('cls')


print('정수 하나를 입력받아 절대값을 구하시오')
# 절댓값 : 수직선에서 0을 기준으로 떨어져 있는 거리값
# 따라서 -3과 +3의 절대값은 돌일하다
# 절대값을 구하려면, 음수인 경우 부호반전, 양수는 그대로 둔다

num9 = int(input('정수 입력 : '))

if num9 > 0:
    pass
else:
   # num9 = num9 * -1
    num9 = -num9    # 부호 반전 단항 연산자

print(f'{num9}의 절댓값은 {num9} 입니다')

input()
system('cls')



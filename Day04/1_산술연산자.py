# 1_산술연산자

# 어떤 수를 이용하여 덧셈 뺄셈 곱셈 나눗셈 등의 연산을 수행하는 기호
# +, -, *, /, //, %, **

n1 = 10
n2 = 3

print('{} + {} = {}'.format(n1, n2, n1 + n2))   
print('{} - {} = {}'.format(n1, n2, n1 - n2))
print('{} * {} = {}'.format(n1, n2, n1 * n2))
print('{} / {} = {}'.format(n1, n2, n1 / n2))
print('{} // {} = {}'.format(n1, n2, n1 // n2)) # 몫
print('{} % {} = {}'.format(n1, n2, n1 % n2))   # 나머지
print('{} ** {} = {}'.format(n1, n2, n1 ** n2)) # 제곱
print()

# 덧셈
# 숫자끼리 덧셈이 가능하다
# 문자열끼리 덧셈이 가능하다    (글자 이어붙이기)
# 리스트끼리 덧셈이 가능하다    (리스트 합치기)
# 그 외에는 자료형이 맞지않으면 덧셈이 불가능하다

print(10+20)        # 수의 덧셈
print('10'+'20')    # 글자의 덧셈
print([10]+[20])    # 리스트의 덧셈
print()

# 곱셈
# 숫자끼리 곱셈이 가능
# 문자열과 숫자사이 곱셈이 가능하다 (문자열 여러번 더하기)

print(3*7)
print('3' * 7)  # 문자열에 대한 반복문을 줄일 수 있다
print()

# 나눗셈
# 나눗셈을 수행한 결과는 실수이므로, {:.2f} 처럼 서식을 적용한다
print((100 + 99 + 87) / 3)
print('{:.2f}'.format((100 + 99 + 87) / 3))
print()

# 몫과 나머지
# 작은 단위가 모여서 큰 단위를 이루는 경우 사용할 수 있다
# 예를 들어 60분이 모이면 1시간이 되는데 이를 구분하여 출력할 때

et = 1920000000
print('{}시간 {}분'.format(et // 60, et % 60))
print()

# 몫과 나머지를 활용한 간단한 타이머 출력해보기
from os import system
from time import sleep

minute = float(input('몇분 체크할까요?'))
second = int(minute * 60)

for i in range(second, -1, -1):
    system('cls')
    print('[{:02d} : {:02d}]'.format (i // 60, i % 60))
    sleep(1)
print('끝')
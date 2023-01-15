# 입력받은 수가 양의 정수, 음의 정수인지 혹은 0인지 판별

num = int(input('정수 입력 : '))

if num > 0:
    print('양의 정수')
elif num < 0:
    print('음의 정수')
else:
    print('입력한 숫자는 0')



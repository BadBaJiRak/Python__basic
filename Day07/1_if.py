'''
    if는 프로그램의 흐름을 분기하는
    기초적인 제어문이며 자주 사용한다

    조건을 판별하여, 조건이 참이면 종속문장을 실행한다
'''

n1 = int(input('정수 입력 : '))

if n1 % 2 == 0:         # 조건절 
    result = '짝수'     # 종속문장
# if와 else 사이 다른 코드 금지
else :                  # 이전에 등장한 if가 모두 아닌 경우
    result = '홀수'

print(result)
print('=' * 30)


'''
    모든 경우에 if ~ elif ~ else 를 쓰는 것은 아니다

    이전 조건과 상관없이 다음 조건을 항상 체크하려면
    if를 나열할 수 있다
'''

# 세 정수를 입력 받아서 그 중 가장 큰 수만 출력하세요
n1, n2, n3 = map(int, input('세 정수 입력 : ').split())

maxNumber = n1

if maxNumber < n2:
    maxNumber = n2
if maxNumber < n3:
    maxNumber = n3

print('최대값 : ',maxNumber)





n1, n2, n3 = map(int,input('세 점수 입력 : ').split())
result1 = (n1+n2+n3)/3


# 입력받은 점수의 평균을 구하고, 등급을 매겨서 출력하세요
# 90 ~ 100  : A
# 80 ~ 89   : B
# 70 ~ 79   : C
# 60 ~ 69   : D
# 60미만    : F
# 당신의 평균은 ~ 이고, 등급은 ~ 입니다.

if result1 >= 90 and result1 <= 100:
    result = 'A'
elif result1 >= 80 and result1 < 90:
    result = 'B'
elif result1 >= 70 and result1 < 80:
    result = 'C'
elif result1 >= 60 and result1 < 70:
    result = 'D'
else:
    result = 'F'

print('당신의 평균은 {:.2f}점 이고, 등급은 {:s} 입니다'.format(result1, result))
print()

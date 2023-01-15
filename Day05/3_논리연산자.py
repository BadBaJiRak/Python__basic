# bool 타입의 값에 대하여 작동하는 연산자
# 서로 다른 두 조건을 함께 고려하거나
# 조건의 결과를 반전시킬 경우 사용한다

# A and B       : A 도 참이고, B 도 참이면 전체가 참이다
# A or B        : A 나 B 둘중 하나라도 참이면 전체가 참이다
# not A         : A 의 결과를 반전 (True -> False, False -> True)
# A in B        : A 가 B 에 포함되어 있으면 True
# A not in B    : A 가 B 에 포함되어 있지 않으면 True

b1 = True
b2 = False
list1 = [1, 3, 5, 7, 9]

# &&, || 는 and, or로 사용한다

print('b1 and b2 : ',b1 and b2)
print('b1 or b2 : ',b1 or b2)
print('not b1 : ',not b1)
print('3 in list1 : ', 3 in list1)
print('3 not in list1 : ', 3 not in list1)
print('=' * 30)

# and : 서로 다른 두 조건을 모두 만족할 경우
# 각 과목이 50점 이상이고, 평균이 60점 이상이면 합격
kor, eng, mat = 60, 60, 60
total = kor + eng + mat
avg = total / 3

cond1 = kor >= 50 and eng >= 50 and mat >= 50
cond2 = avg >= 60
print('과락이 없는가 ? : ',cond1)
print('평균이 합격점 이상인가 : ',cond2)
print('합격여부 : ',cond1 and cond2)
print()

# 서로 다른 조건을 나열하려면, 각각 작성해야한다.
print(50 < kor and eng and mat) # 이렇게 하믄 안ㄷ

# 파이썬에서는 숫자도 조건으로 활용할 수 있다
# 0은 False에 해당하며, 나머지 모든 수는 True에 해당한다
if 0:
    print(0)

if 1:
    print(1)

if -1:
    print(-1)

print()

# 수의 범위를 제한하고자 할 때
n1 = int(input('정수 입력 (0 ~ 100) : '))

# if <= n1 and n1 <= 100:   # 실행 가능
if 0 <= n1 <= 100:          # 실행 가능하지만 권장하지 않음
    print('정상')

if not (0 <= n1 <= 100):
    print('범위 초과')
print()

# or 연산자 : 서로 다른 조건 중 하나라도 만족하면 결과가 참이다

cash = 0
checkCard = 7200
creditCard = 50000
taxiFee = 12000

canRideTaxi = (cash >= taxiFee) or (checkCard >= taxiFee) or (creditCard >= taxiFee)

if canRideTaxi:
    print('택시를 타고 집에 간다')

if not canRideTaxi:
    print('다른 방법을 찾아야 한다')
print()


# and : 양쪽의 모든 조건이 True여야 한다
# 만약, 첫번째 조건이 False라면, 두번째 조건을 확인할 필요가 없다

# or : 양쪽의 조건 중 하나라도 True가 있으면 참이다
# 만약 첫번째 조건이 True라면, 두번째 조건을 확인할 필요가 없다

n1, n2, n3, n4 = 1, 0, -1, 2

b1 = n1 <= n2 and n3 + 1 > n4 -1
print(b1)
print()

print(n1 % 2 == 0 and '짝수' or '홀수')
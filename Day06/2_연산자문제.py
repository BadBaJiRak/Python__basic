# 1) 정수를 입력 받아서 훌짝 판별 후 출력
num1 = int(input('정수를 입력하세요 : '))
if(num1 % 2 == 0):
    print('짝수')
if(num1 % 2 != 0):
    print('홀수')
print('=' * 30)


# 2) 문자열을 입력받아서, 미리 준비한 값과 비교하여 일치 여부 판별(apple)
a = 'apple'
b = input('단어 입력 : ')

if a == b:
    c = '일치'
else:
    c = '불일치'

print(c)
print('=' * 30)

# 3) 나이가 20세 이상이고, 성별이 남성이면 현역, 아니면 면제로 출력하세요
a1 = input('성별을 입력 하세요 : ')
age = int(input('나이를 입력 하세요 : '))
men = '남성'
tf = a1 == men and age >= 20

if (tf == True):
    hd = '현역'
if (tf != True):
    hd = '면제'

print(hd)
print('=' * 30)

# 4) 두개의 문자열을 연속으로 입력 받아서
# 첫번째가 itbank, 두번째가 it이면 성공
# 아니면 실패라고 출력하세요
ip1 = input('첫번째 단어 입력 : ')
ip2 = input('두번째 단어 입력 : ')
save1 = 'itbank'
save2 = 'it'
result = save1 == ip1 and save2 == ip2

if result == True:
    d1 = '성공'
if result != True:
    d1 = '실패'
print(d1)


id, pw = input('id, pw를 연속으로 입력 : ').split()
serverid, serverpw = 'itbank', 'it'

flag = (id == serverid) and (pw == serverpw)

print(flag and '성공' or '실패')
print('=' * 30)

# A.B
# A객체 내부의 B요소에 접근할때 사용
# . 은 한국어 소유격 조사 (~의) 에 해당한다고 생각하면 된다

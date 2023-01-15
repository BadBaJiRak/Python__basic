# 4_문제.py

name = '홍길동'
age = 20
address = '부산 해운대'

print('이름 :', name)
print('나이 :', age)
print('주소 :', address)

print(name, '/', age, '/', address)
# print(name + '/' + age + '/' + address)

print(name + ' / ' + str(age) + ' / ' + address)
# int 형태의 age를 str형태로 변환한 이후 덧셈한다

# 문장 형태로 출력하기
# 중간에 특정 단어만 내용이 바뀐다면
# 전체 내용을 계속 적어줘야해서 불편하다
print(
    '제 이름은 ' + name + '이고, 나이는', 
    age, 
    '살이고, 주소는 ' + address + '입니다'
)
# 파이썬은 print를 위와 같은 형식으로도 사용 가능




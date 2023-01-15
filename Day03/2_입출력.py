# 2_입출력.py

# 1) input() 함수는 키보드로 입력받은 값을 문자열로 만들어낸다
# 2) 입력받은 값은 변수에 저장해서 사용한다
# 3) 필요하다면, 입력받을 때 곧바로 형변환을 적용할 수 있다

name = input('이름 입력 : ')
age = int(input('나이 입력 : '))    # 나이를 입력 받아서 정수로 변환하여 age 변수에 저장한다
isAdult = age >= 20

print('이름 :', name)
print('나이 :', age)
print(isAdult and '성인' or '미성년자')

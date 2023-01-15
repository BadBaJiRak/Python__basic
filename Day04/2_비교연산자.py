# 2_비교연산자

# 값의 크기를 비교하거나, 일치 여부를 판단한다.
# 결과는 bool 형태의 값 (True/False) 로 나타난다.

n1 = '10'
n2 = '3'
# 문자열도 크기 비교가 가능하다 (문자열 정렬이 쉽다)
print('{} > {} : {}'.format(n1, n2, n1 > n2))       # 초과
print('{} >= {} : {}'.format(n1, n2, n1 >= n2))     # 이상
print('{} < {} : {}'.format(n1, n2, n1 < n2))       # 미만
print('{} <= {} : {}'.format(n1, n2, n1 <= n2))     # 이하
print('{} == {} : {}'.format(n1, n2, n1 == n2))     # 일치
print('{} != {} : {}'.format(n1, n2, n1 != n2))     # 불일치
print()

# 제어문 if와 연동하여 주로 사용한다

score = int(input('정수 입력 : '))
if score >= 60:
    result = '합격'
if score < 60:
    result = '불합격'

print(result)

# 비교연산 예시2)
 
movieList = '어벤져스'

newMovie = input('새로운 영화 제목 입력 : ')

if newMovie > movieList:
    movieList = movieList + ', ' + newMovie

if newMovie <= movieList:
    movieList = newMovie + ', ' + movieList

print(movieList)
print()

# 비교연산 예시3)
password = input('비밀번호 입력 : ')    # 입력 받아서 apssword 변수에 저장

if password == 'itbank':    # 일치하면
    print('통과')           # 통과
if password != 'itbank':    # 일치하지 않으면
    print('거부')           # 거부

    
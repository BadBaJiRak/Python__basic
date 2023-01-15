# 5_문자열만들기.py

s1 = '■ ■ ■ ■ ■'
print(s1)
print(s1)
print(s1)
print(s1)
print(s1)

print('=' * 25)

# s2 변수에 5줄 x 5칸으로 하나의 문자열을 만들어서 출력하기
s2 = '''■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■ ■ ■
■ ■ ■ ■ ■'''
print(s2)
print('=' * 25)

# 다른 접근 방법
s3 = f'''{s1}
{s1}
{s1}
{s1}
{s1}
'''
print(s3)
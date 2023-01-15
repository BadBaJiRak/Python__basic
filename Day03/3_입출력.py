# 3_입출력.py
# 파이썬에서 따옴표를 3개붙이면 여러줄 문자열을 만들 수 있다

question = '''
다음 중, 파이썬 기본 자료형이 아닌것은 무엇인가?
    1. str
    2. int
    3. float
    4. double
    5. bool
입력 >>> '''

answer = int(input(question))
print(answer == 4)  # bool 형태 참 or 거짓으로 출력 
                    # 변수 answer의 값과 4가 일치하면 True(참)을 출력한다
# 일치함을 나타낼때는 == 로 표시한다

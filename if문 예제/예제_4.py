'''
아이디를 입력받아 아이디가 'admin'이면 '모든 콘텐츠 이용 가능'을 출력하고 프로그램을 종료한다. 
아이디가 'admin'이 아니면 회원 레벨을 입력받아 회원 레벨이 2~7이면 '일부 콘텐츠 이용 가능'을 출력하고, 
그렇지 않으면 '콘텐츠 이용 불가'를 출력하는 프로그램을 작성하시오.
'''

saveId = 'admin'

inputId = input('아이디를 입력하세요 : ')

if inputId == saveId:
    print('모든 콘텐츠 이용 가능')

else:
    inputLevel = int(input('회원 레벨을 입력하세요 : '))
    if 2 <= inputLevel and inputLevel <= 7:
        print('일부 콘텐츠 이용 가능')
    else:
        print('콘텐츠 이용 불가')


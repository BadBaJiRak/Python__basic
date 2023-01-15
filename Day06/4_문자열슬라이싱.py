
'''
    위 문자열을 4자리의 연도, 2자리의 월
    2자리의 일, 마지막까지의 요일로 구분하여
    각 변수에 저장하세요

    한 문장으로 다음과 같이 출력하세요
    
    '내일은 2023년 1월 12일 Thursday 입니다'
'''

tomorrow = '20230112Thursday'
year = tomorrow[0:4]
mon = tomorrow[4:6]
dat = tomorrow[6:8]
da = tomorrow[8:16] # tommorow[8:len(tomorrow)]

year = tomorrow[:4]
da = tomorrow[8:]

print('내일은 {}년 {}월 {}일 {} 입니다'.format(year, mon, dat, da))


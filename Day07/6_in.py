# 문자열에 특정 글자가 포함되어 있는지 아닌지 판별할 수 있다
metroCity = '부산,울산,광주,인천,대구,대전'

inputCity = input('도시 이름 입력 : ')
# flag1 : 입력한 글자가 metroCity 안에 포함 되어있는지
flag1 = flag = inputCity in metroCity

# flag2 : 입력한 단어가 metroCity 안에 포함 되어있는지
flag2 = inputCity in metroCity.split(',')    # split(',') -> ['부산', '울산', '광주', '인천', '대구', '대전']

if flag2:
    result = '광역시가 맞습니다'

else:
    result = '광역시가 아닙니다'

print(inputCity, ': ' + result)
print()


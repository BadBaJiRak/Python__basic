'''
    물의 섭씨 또는 화씨 온도를 입력받아 섭씨 온도와 물의 상태를 판별하는 프로그램을 작성하시오.
    단, 화씨 온도가 입력될 경우에는 섭씨 온도로 변환한다

    * 힌트 : 섭씨 = (화씨 - 32) * 5 / 9

'''
choice = int(input('단위를 입력 하세요(1. 섭씨 / 2. 화씨) : '))
tmp = int(input('온도를 입력 하세요 : '))

if choice == 2:
    tmp = (tmp - 32) * 5 / 9

print('물의 섭씨 온도 :{:.2f}'.format(tmp))



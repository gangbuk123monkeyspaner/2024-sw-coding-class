try:
    a,b = map(int,input('두 수를 입력하세요:').split())
    try:
        c = a/b
        print(f'{a} / {b} = {c}')
    except ZeroDivisionError:
        print('0으로는 나눌수 없습니다')

except ValueError:
    print('두 수를 입력했는지 확인하세요')

import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

years = float(input('Введіть кількість років вашої собаки: '))

if years > 2:
    print('Тривалість життя у людських роках (1 варіант): ', years * 7)
    humen_y = 2 * 10.5
    years -= 2
    humen_y += years * 4
    print('Тривалість життя у людських роках (2 варіант): ', humen_y)

elif years > 0 and years <= 2:
    print('Тривалість життя у людських роках (1 варіант): ', years * 7)
    humen_y = years * 10.5
    print('Тривалість життя у людських роках (2 варіант): ', humen_y)

else:
    print('Error')

printTimeStamp('Anastasiia Kordonska')

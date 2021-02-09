import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

whater = float(input('Введіть кількість кубометрів: '))
sum = 20
if whater > 30:
    whater -= 30
    sum += 30 * 9.86

    if whater <= 20:
        sum += whater * 11.22
        print('Ваш рахунок: ', '{:0.2f}'.format(sum))

    elif whater > 20 and whater <= 30:
        whater -= 20
        sum += 20 * 11.22 + whater * 13.06
        print('Ваш рахунок: ', '{:0.2f}'.format(sum))

    else:
        whater -= 30
        sum += 20 * 11.22 + 10 * 13.06 + whater * 17.89
        print('Ваш рахунок: ', '{:0.2f}'.format(sum))

else:
    sum += whater * 9.86
    print('Ваш рахунок: ', '{:0.2f}'.format(sum))

printTimeStamp('Anastasiia Kordonska')

import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

minutes = int(input('Введіть кількість витрачених хвилин: '))
mesages = int(input('Введіть кількість витрачених повідомлень: '))
sum = float(45)
if minutes > 200:
    sum += 0.27 * (minutes - 200)
    if mesages > 50:
        sum += 0.5 * (mesages - 50)
    else:
        print('Базова плата за користування (без внесків та податків): ', '{:0.2f}'.format(sum))
        print('Загальний рахунок для користувача: ', '{:0.2f}'.format(sum * 1.05 + 1.44))

else:
    print('Базова плата за користування (без внесків та податків): ', '{:0.2f}'.format(sum))
    print('Загальний рахунок для користувача: ', '{:0.2f}'.format(sum * 1.05 + 1.44))


printTimeStamp('Anastasiia Kordonska')

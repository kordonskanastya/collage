import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

formula = input('Введіть систему (метрична\американська): ')
lenght = float(input('Введіть свій зріст: '))
weight = float(input('Введіть свою вагу: '))
if formula == 'метрична':
    imt = weight / lenght ** 2
    print("Ваш ІМТ: ", "{:0.2f}".format(imt))
elif formula == 'американська':
    imt = 703 * (weight / lenght ** 2)
    print("Ваш ІМТ: ", "{:0.2f}".format(imt))
else:
    print("Error, try again")

printTimeStamp('Anastasiia Kordonska')

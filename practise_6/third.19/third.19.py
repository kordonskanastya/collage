import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

year = int(input('Введіть ваш рік народження: '))
year = year % 100
print(year)

if year == 0:
    print('Рік Дракон')

elif year == 1:
    print('Рік Змія')

elif year == 2:
    print('Рік Кінь')

elif year == 3:
    print('Рік Коза')

elif year == 4:
    print('Рік Мавпа')

elif year == 5:
    print('Рік Півень')

elif year == 6:
    print('Рік Собака')

elif year == 7:
    print('Рік Свиня')

elif year == 8:
    print('Рік Щур')

elif year == 9:
    print('Рік Бик')

elif year == 10:
    print('Рік Тигр')

elif year == 11:
    print('Рік Кролик')

else:
    print('Error')

printTimeStamp('Anastasiia Kordonska')

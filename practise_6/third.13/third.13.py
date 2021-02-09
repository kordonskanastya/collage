import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

mag = float(input('Введіть магнітуду: '))

if mag < 2 and mag >= 0:
    print('Мікро (micro)')

elif mag >= 2 and mag < 3:
    print('Дуже слабкий (very minor)')

elif mag >= 3 and mag < 4:
    print('Слабкий (minor)')

elif mag >= 4 and mag < 5:
    print('Легкий (light)')

elif mag >= 5 and mag < 6:
    print('Помірний (moderate)')

elif mag >= 6 and mag < 7:
    print('Сильний (strong)')
elif mag >= 7 and mag < 8:
    print('Дуже сильний (major))')

elif mag >= 8 and mag < 10:
    print('Великий (great)')

elif mag >= 10:
    print('Рідкісно великий (meteoric)')
else:
    print('Error')

printTimeStamp('Anastasiia Kordonska')

import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

volume = float(input('Введіть кількість децибел: '))
if volume < 40:
    print('Гучність знаходиться до Тихої кімнати')
elif volume == 40:
    print('Гучність дорівнює Тихій кімнаті')
elif volume > 40 and volume < 70:
    print('Гучність знаходиться між Тихою кімнатою та Будильником')
elif volume == 70:
    print('Гучність дорівнює Будильнику')
elif volume > 70 and volume < 106:
    print('Гучність знаходиться між Будильником та Бензиновою газонокосаркою')
elif volume == 106:
    print('Гучність дорівнює Бензиновій газонокосаркі')
elif volume > 106 and volume < 130:
    print('Гучність знаходиться між Бензиновою газонокосаркою та Відбійним молотоком')
elif volume == 130:
    print('Гучність дорівнює Відбійному молотку')
else:
    print('Гучність більша за Відбійний молоток')

printTimeStamp('Anastasiia Kordonska')

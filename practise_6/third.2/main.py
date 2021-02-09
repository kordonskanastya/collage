import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

place = str(input('Введіть місце проживання (Будинок\Квартира\Гуртожиток): '))
time = int(input('Введіть ваш час вдома: '))
if place == 'Будинок':
    if time >= 18:
        print('Рекомендація: В’єтнамське порося')
    if time > 10 & time < 17:
        print('Рекомендація: Собака')
    if time < 10:
        print('Рекомендація: Змія')

if place == 'Квартира':
    if time >= 10:
        print('Рекомендація: Кішка')
    if time < 10:
        print('Рекомендація: Хом’як')

if place == 'Гуртожиток':
    if time >= 6:
        print('Рекомендація: Рибки')
    if time < 6:
        print('Рекомендація: Мурашник')

printTimeStamp('Anastasiia Kordonska')


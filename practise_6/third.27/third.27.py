import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

number = int(input('Введіть десяткове число: '))
result = str('')

while number != 0:
    r = number % 2
    result += str(r)
    number //= 2

result = result[::-1]
print(result)
print('end')

printTimeStamp('Anastasiia Kordonska')

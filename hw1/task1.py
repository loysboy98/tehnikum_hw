print('Введите три числа!')
a = int(input('первое числа: '))
b = int(input('второй число: '))
c = int(input('третье число: '))

if b < a < c or c < a < b:
    print('Среднее:', a)
elif a < b < c or c < b < a:
    print('Среднее:', b)
else:
    print('Среднее:', c)

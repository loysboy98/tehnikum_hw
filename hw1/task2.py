print('Введите три числа!')
a = int(input('первое числа: '))
b = int(input('второй число: '))
c = int(input('третье число: '))

if a > b and a < c:
    m = a
    print(a)
if b > a and b > c:
    m = b
    print(b)
if c > a and c > b:
    m = c
    print(c)
    
print(max(a,b,c) ==m)

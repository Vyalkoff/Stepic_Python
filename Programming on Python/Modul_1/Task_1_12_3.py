x = float(input())
y = float(input())
z = input()
if y == 0.0 and ((z == 'mod') or (z == '/') or (z == 'div')):
    print("Деление на 0!")
elif z == '+':
    print(x + y)
elif z == '*':
    print(x * y)
elif z == '/':
    print(x / y)
elif z == '-':
    print(x - y)
elif z == 'mod':
    print(x % y)
elif z == 'pow':
    print(x ** y)
elif z == 'div':
    print(x // y)

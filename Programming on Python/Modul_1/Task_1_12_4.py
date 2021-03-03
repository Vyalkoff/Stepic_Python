form = str(input())
if form == "треугольник":
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif form == "прямоугольник":
    a = int(input())
    b = int(input())
    print(a * b)
elif form == "круг":
    r = int(input())
    p = 3.14
    print(p * (r ** 2))

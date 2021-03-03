a = int(input())
b = int(input())
h = int(input())
if b >= h >= a:
    print("Это нормально")
elif h > b:
    print("Пересып")
elif h < a:
    print("Недосып")

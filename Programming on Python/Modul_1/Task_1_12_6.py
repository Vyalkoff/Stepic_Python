x = int(input())
edit = 'программист'
if x % 10 == 1 and x % 100 != 11:
    print(x, edit)
elif 2 <= x % 10 <= 4 and (x % 100 < 12 or x % 100 > 14):
    print(x, edit + 'а')

else:
    print(x, edit + 'ов')

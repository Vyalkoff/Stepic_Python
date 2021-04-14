with open('dataset_3363_4.txt', 'r', encoding='utf-8') as dt:
    with open('data1.txt', 'w', encoding='utf-8') as dw:
        list_mat, list_fiz, list_rus, count = 0, 0, 0, 0
        for line in dt:
            line_list = line.strip().split(';')
            list_mat += int(line_list[1])
            list_fiz += int(line_list[2])
            list_rus += int(line_list[3])
            dw.write(f'{(int(line_list[1]) + int(line_list[2]) + int(line_list[3])) / 3}\n')
            count += 1
        dw.write(f'{round(list_mat / count, 9)} {round(list_fiz / count, 9)} {round(list_rus / count, 9)}')

# st = [x.split(';') for x in open('dataset_3363_4.txt').readlines()]
# print(*[sum([int(y) for y in x[1:]]) / 3 for x in st], sep='\n')
# print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]]) / len(st) for z in range(1, 4)])

with open('dataset_3363_3.txt', 'r') as inf:
    content = inf.read().strip().split(' ')
    word = ''
    cont = 0
    print(content)
    for i in content:
        if i != word:
            co = content.count(i)
            if co > cont:
                cont = co
                word = i

    print(word,cont)

import requests
name = '699991.txt'
while True:
    if 'We' in name:
        break
    else:
        r = requests.get(f'https://stepic.org/media/attachments/course67/3.6.3/{name}')
        name = r.text
        print(name)


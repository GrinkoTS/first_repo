import os

sayt = input()

if 'https://' in sayt:
    os.system('start ' + sayt)
    print('if')
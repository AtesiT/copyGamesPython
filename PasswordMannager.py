# master_pwd = input('Что такое "мастер" паролей? ')

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print('Логин: ', user, '| Пароль: ', passw)


def add():
    name = input('Ваш логин: ')
    pwd = input('Пароль: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + pwd + '\n')


while True:
    mode = input('Хотите добавить новый пароль и добавить существующий?\nВведите "посмотреть" или "добавить", а можно и вовсе "выйти" ').lower()
    if mode == 'выйти':
        break

    elif mode == 'посмотреть':
        view()
    
    elif mode == 'добавить':
        add()

    else:
        print('Вы напечатали не то, что нужно было')
        continue
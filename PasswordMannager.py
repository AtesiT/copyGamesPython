from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key) 
'''


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_pwd = input('Какой "мастер" паролей? ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(' | ')
            print('Логин: ', user, '| Пароль: ', fer.decrypt(pwd.encode()).decode())



def add():
    name = input('Ваш логин: ')
    pwd = input('Пароль: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + '\n')


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
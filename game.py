print('Добро пожаловать в викторину.')

playing = input('Сыграете в викторину? (Да / Нет) ')
if playing != 'Да':
    quit()

print('Начинаем игру.')

answer = input('Сокращение ПК. Это? ')
if answer.capitalize() == 'Персональный компьютер' or answer.title() == 'Персональный Компьютер':
    print('Правильно!')
    i=i+1
else:
    print('Неправильно')

answer = input('Что такое GPU на русском? ')
if answer.capitalize() == 'Видеокарта':
    print('Правильно!')
    i=i+1
else:
    print('Неправильно')


answer = input('Что такое CPU на русском? ')
if answer.capitalize() == 'Процессор':
    print('Правильно!')
    i=i+1
else:
    print('Неправильно')

answer = input('Что такое RAM на русском? ')
if answer.capitalize() == 'Оперативная память' or answer.title() == 'Оперативная Память':
    print('Правильно!')
    i=i+1
else:
    print('Неправильно')

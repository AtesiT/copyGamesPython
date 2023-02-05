print('Добро пожаловать в викторину.')

playing = input('Сыграете в викторину? (Да / Нет) ')
if playing.capitalize() != 'Да':
    quit()

print('Начинаем игру.')
score = 0
asks=0

answer = input('Сокращение ПК. Это? ')
if answer.capitalize() == 'Персональный компьютер' or answer.title() == 'Персональный Компьютер':
    print('Правильно!')
    score = score+1
else:
    print('Неправильно')
asks+=1

answer = input('Что такое GPU на русском? ')
if answer.capitalize() == 'Видеокарта':
    print('Правильно!')
    score = score+1
else:
    print('Неправильно')
asks+=1


answer = input('Что такое CPU на русском? ')
if answer.capitalize() == 'Процессор':
    print('Правильно!')
    score = score+1
else:
    print('Неправильно')
asks+=1

answer = input('Что такое RAM на русском? ')
if answer.capitalize() == 'Оперативная память' or answer.title() == 'Оперативная Память':
    print('Правильно!')
    score = score+1
else:
    print('Неправильно')
asks+=1

print(f'У тебя {score} баллов')
print(f'Ты ответил правильно на {int((score/asks) * 100)}% вопросов')
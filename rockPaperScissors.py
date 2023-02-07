import random

user_wins = 0
computer_wins = 0

options = ['камень', 'ножницы', 'бумага']

print('Добро пожаловать в игру новичок. Если ты выберешь ножницы, компьютер выберет ножницы, ты проиграешь. И аналогично с другими предметами. \nТаковы правила. Если ты выиграешь в игре, можешь покупать лотерею. Победить будет не просто.')

while True:
    user_input = input('Камень/Ножницы/Бумага или Q - чтобы выйти: ').lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #камень - 0, бумага - 1, ножницы - 2
    computer_pick = options[random_number]
    print('"Искуственный интеллект" выбрал', computer_pick + '.')

    if user_input == "камень" and computer_pick == "ножницы":
        print('Вы выиграли!')
        user_wins += 1

    elif user_input == "бумага" and computer_pick == "камень":
        print('Вы выиграли!')
        user_wins += 1

    elif user_input == "ножницы" and computer_pick == "бумага":
        print('Вы выиграли!')
        user_wins += 1

    else:
        print('Ты проиграл.')
        computer_wins += 1

print(f'Ты выиграл {user_wins} раз. Искусственный интеллект выиграл {computer_wins} раз.')

if computer_wins > user_wins:
    print('Искуственный интеллект победил тебя. Ты уволен. На твоё место поставили робота.')
elif computer_wins == user_wins:
    print('В следующий раз будь сильнее, а лучше взломай игру.')
else:
    print('Ты победил. Везунчик. Тебе повезло в текущей игре.')

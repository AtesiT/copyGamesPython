import random

top_of_range = input('Введите число: ')

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('Напишите число больше нуля в следующий раз')
        quit()
else:
    print('Напишите число в следующий раз')
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input('Попробуй угадать число: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Напишите число в следующий раз')
        continue

    if user_guess == random_number:
        print('Ты угадал число')
        break
    else:
        if user_guess > random_number:
            print('Число выше твоего')
        else:
            print('Число ниже твоего')

print(f'У тебя было {guesses} попыток')
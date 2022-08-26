import time

number = int(time.time() * 10) % 10
user_number = int(input('Введите цифру от 0 до 9: '))

attempts_count = 1
attempts = [user_number,]

while number != user_number:
    attempts_count += 1
    if user_number > number:
        print('Ваше число больше!')
    else:
        print('Ваше число меньше!')
    user_number = int(input('Попробуйте ещё раз: '))
    attempts.append(user_number)

print('Вы угадали! Количество попыток', attempts_count, sep=' - ')
print('Ваши числа в порядке введения:')

for attempt_index, attempt in enumerate(attempts):
    print(f'Попытка № {attempt_index} : {attempt}')

year_as_str = input('Введите год: ')
year = int(year_as_str)
print(year)
is_leap_year = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
answer = "Да" if is_leap_year else "Нет"
print('Год високосный? ', answer)
print()

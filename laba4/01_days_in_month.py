#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

# TODO здесь ваш код
number_1 = [1, 3, 5, 7, 8, 10, 12]
number_2 = [4, 6, 9, 11]
if month in number_1:
    print('31 days')
elif month in number_2:
    print('30 days')
elif month == 2:
    print('28 days')
else:
    print('Error')
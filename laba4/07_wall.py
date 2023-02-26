#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.resolution = (1200, 600)
pos_x = -150
pos_y = -50
pos_x_1 = -50
pos_y_1 = 0

for i in range(1, 13):
    temp_1 = pos_x
    temp_2 = pos_x_1
    if i % 2 == 0:
        temp_1 += 50
        temp_2 += 50
    pos_y += 50
    pos_y_1 += 50
    for k in range(1, 13):
        temp_1 += 100
        temp_2 += 100
        sd.rectangle(left_bottom = sd.Point(temp_1, pos_y), right_top = sd.Point(temp_2, pos_y_1), color = sd.COLOR_RED, width = 1)
sd.pause()

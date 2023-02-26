#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код

point = sd.get_point(50, 50)
sd.circle(center_position = point)
rd = 35
for i in range(1, 4):
    sd.circle(center_position = sd.Point(x = 50, y = 50), radius = rd, color = sd.COLOR_YELLOW, width = 1)
    rd += 5

# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
# TODO здесь ваш код

def bubble(point, step):
    radius = 50
    for i in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color = sd.COLOR_BLACK)
point = sd.get_point(90, 510)
bubble(point=point, step=10)

# colors = {
#     sd.COLOR_BLACK: 1,
#     sd.COLOR_BLUE: 2,
#     sd.COLOR_CYAN: 3,
#     sd.COLOR_DARK_BLUE: 4,
#     sd.COLOR_DARK_CYAN: 5,
#     sd.COLOR_DARK_GREEN: 6,
#     sd.COLOR_DARK_ORANGE: 7,
#     sd.COLOR_DARK_PURPLE: 8,
#     sd.COLOR_DARK_RED: 9,
#     sd.COLOR_DARK_YELLOW: 10,
#     sd.COLOR_GREEN: 11,
#     sd.COLOR_WHITE: 12,
#     sd.COLOR_YELLOW: 13,
#     sd.COLOR_ORANGE: 14,
#     sd.COLOR_PURPLE: 15,
#     sd.COLOR_RED: 16
# }

# colors_name = [
#     'Black',
#     'Blue',
#     'Cyan',
#     'Dark blue',
#     'Dark cyan',
#     'Dark green',
#     'Dark orange',
#     'Dark red',
#     'Green',
#     'White',
#     'Yellow'
# ]

# print('All colors:',', '.join(colors_name))
# cur_color = input('Enter the color of your circle (from 1 to 16): ')
# cur_radius = input('Enter the radius: ')
# cur_width = input('Enter the width: ')
# cur_point_1, cur_point_2 = input('Enter position of your circle \n(x):'), input('(y):')
# sd.circle(center_position = sd.Point(int(cur_point_1), int(cur_point_2)), radius = int(cur_radius), color = int(cur_color), width = int(cur_width))
# sd.circle(center_position = sd.Point(int(cur_point_1), int(cur_point_2)), radius = int(cur_radius) - 5, color = int(cur_color), width = int(cur_width))
# sd.circle(center_position = sd.Point(int(cur_point_1), int(cur_point_2)), radius = int(cur_radius) - 10, color = int(cur_color), width = int(cur_width))

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

pos_x = 470
pos_y = 100
for _ in range(1, 11):
     sd.circle(center_position = sd.Point(pos_x, pos_y), radius = 20, color = sd.COLOR_WHITE, width = 1)
     sd.circle(center_position = sd.Point(pos_x, pos_y), radius = 15, color = sd.COLOR_WHITE, width = 1)
     sd.circle(center_position = sd.Point(pos_x, pos_y), radius = 10, color = sd.COLOR_WHITE, width = 1)
     pos_x += 50


# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

pos_x = 370
pos_y = 300
for _ in range(1, 4):
    temp = pos_x
    pos_y += 50
    for _ in range(1, 11):
       sd.circle(center_position = sd.Point(temp, pos_y), radius = 20, color = sd.COLOR_ORANGE, width = 1)
       sd.circle(center_position = sd.Point(temp, pos_y), radius = 15, color = sd.COLOR_ORANGE, width = 1)
       sd.circle(center_position = sd.Point(temp, pos_y), radius = 10, color = sd.COLOR_ORANGE, width = 1)
       temp += 50

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

for _ in range(1, 101):
    s = sd.random_point()
    sd.circle(center_position = s, radius = 20, color = sd.random_color(), width = 2)
    sd.circle(center_position = s, radius = 15, color = sd.random_color(), width = 2)
    sd.circle(center_position = s, radius = 10, color = sd.random_color(), width = 2)

sd.pause()
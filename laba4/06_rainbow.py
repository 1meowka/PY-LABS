#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.

# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.
sd.resolution = (600, 600)
pos_x_1 = 45
pos_y_1 = 45
pos_x_2 = 545
pos_y_2 = 645
for i in range(0, 7):
    pos_x_1 += 5
    pos_x_2 += 5
    sd.line(start_point = sd.Point(pos_x_1, pos_y_1), end_point = sd.Point(pos_x_2, pos_y_2), color = rainbow_colors[i], width = 4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
sd.pause()

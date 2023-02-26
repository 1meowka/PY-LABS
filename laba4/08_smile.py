#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код

sd.resolution = (600, 600)

for i in range(1, 11):
    s = sd.random_point()
    point_list = [sd.Point(s.x - 15, s.y - 5), sd.Point(s.x - 8, s.y - 1), sd.Point(s.x + 8, s.y - 1), sd.Point(s.x + 15, s.y - 5)]
    sd.circle(center_position = s, radius = 50)
    sd.circle(center_position = sd.Point(s.x - 20, s.y + 20), radius = 12)
    sd.circle(center_position = sd.Point(s.x + 20, s.y + 20), radius = 12)
    sd.lines(point_list)
sd.pause()


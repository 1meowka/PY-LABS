#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря
m1, m2 = sites['Moscow']
l1, l2 = sites['London']
p1, p2 = sites['Paris']

distances['Moscow-London'] = ((m1 - l1) ** 2 + (m2 - l2) ** 2) ** 0.5
distances['Moscow-Paris'] = ((m1 - p1) ** 2 + (m2 - p2) ** 2) ** 0.5
distances['London-Paris'] = ((l1 - p1) ** 2 + (l2 - p2) ** 2) ** 0.5

print(distances)

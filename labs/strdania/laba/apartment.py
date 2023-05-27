from laba.room import calculate_area

def calculate_heat_power(outside_temp, inside_temp, heat_loss_coef):
    area = calculate_area(10, 10, 3)  # Пример вызова функции calculate_area из модуля room.py
    heat_power = area * (inside_temp - outside_temp) * heat_loss_coef
    return heat_power

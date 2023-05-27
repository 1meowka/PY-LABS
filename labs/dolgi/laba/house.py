from laba.apartment import calculate_heat_power

def calculate_total_heat_power(outside_temp, inside_temp, heat_loss_coef, num_apartments):
    total_heat_power = calculate_heat_power(outside_temp, inside_temp, heat_loss_coef) * num_apartments
    return total_heat_power

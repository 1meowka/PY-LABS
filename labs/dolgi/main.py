import tkinter as tk
from tkinter import messagebox
from laba.room import calculate_area as room_calculate_area
from laba.apartment import calculate_heat_power as apartment_calculate_heat_power
from laba.house import calculate_total_heat_power as house_calculate_total_heat_power
import docx

def calculate():
    # Расчет общей площади
    length = float(length_entry.get())
    width = float(width_entry.get())
    height = float(height_entry.get())
    num_rooms = int(num_rooms_entry.get())
    area = room_calculate_area(length, width, height)
    total_area_label.config(text="Общая площадь помещений: {} м^2".format(area * num_rooms))

    # Расчет тепловой мощности
    outside_temp = float(outside_temp_entry.get())
    inside_temp = float(inside_temp_entry.get())
    heat_loss_coef = float(heat_loss_coef_entry.get())
    num_apartments = int(num_apartments_entry.get())
    heat_power = apartment_calculate_heat_power(outside_temp, inside_temp, heat_loss_coef)
    total_heat_power_label.config(text="Тепловая мощность для обогрева помещений: {} Вт".format(heat_power * num_apartments))

def save_report():
    doc = docx.Document()
    doc.add_heading('Результаты расчетов', 0)
    doc.add_paragraph(total_area_label.cget("text"))
    doc.add_paragraph(total_heat_power_label.cget("text"))
    doc.save('report.docx')
    messagebox.showinfo("Сохранение отчета", "Отчет успешно сохранен в report.docx")

root = tk.Tk()
root.title("Расчет площади и тепловой мощности")
root.geometry("400x420+500+100")


length_label = tk.Label(root, text="Длина (м):")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

width_label = tk.Label(root, text="Ширина (м):")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Высота (м):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

num_rooms_label = tk.Label(root, text="Количество комнат:")
num_rooms_label.pack()
num_rooms_entry = tk.Entry(root)
num_rooms_entry.pack()

outside_temp_label = tk.Label(root, text="Температура на улице (C):")
outside_temp_label.pack()
outside_temp_entry = tk.Entry(root)
outside_temp_entry.pack()

inside_temp_label = tk.Label(root, text="Температура в помещении (C):")
inside_temp_label.pack()
inside_temp_entry = tk.Entry(root)
inside_temp_entry.pack()

heat_loss_coef_label = tk.Label(root, text="Коэффициент тепловых потерь:")
heat_loss_coef_label.pack()
heat_loss_coef_entry = tk.Entry(root)
heat_loss_coef_entry.pack()

num_apartments_label = tk.Label(root, text="Количество квартир:")
num_apartments_label.pack()
num_apartments_entry = tk.Entry(root)
num_apartments_entry.pack()

calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.pack()

total_area_label = tk.Label(root, text="")
total_area_label.pack()

total_heat_power_label = tk.Label(root, text="")
total_heat_power_label.pack()

save_report_button = tk.Button(root, text="Сохранить отчет", command=save_report)
save_report_button.pack()

root.mainloop()

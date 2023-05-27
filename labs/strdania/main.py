from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from laba.room import calculate_area as room_calculate_area
from laba.apartment import calculate_heat_power as apartment_calculate_heat_power
from laba.house import calculate_total_heat_power as house_calculate_total_heat_power
import docx

class CalculationForm(BoxLayout):
    def __init__(self, **kwargs):
        super(CalculationForm, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.length_label = Label(text="Длина (м):")
        self.add_widget(self.length_label)
        self.length_entry = TextInput()
        self.add_widget(self.length_entry)

        self.width_label = Label(text="Ширина (м):")
        self.add_widget(self.width_label)
        self.width_entry = TextInput()
        self.add_widget(self.width_entry)

        self.height_label = Label(text="Высота (м):")
        self.add_widget(self.height_label)
        self.height_entry = TextInput()
        self.add_widget(self.height_entry)

        self.num_rooms_label = Label(text="Количество комнат:")
        self.add_widget(self.num_rooms_label)
        self.num_rooms_entry = TextInput()
        self.add_widget(self.num_rooms_entry)

        self.outside_temp_label = Label(text="Температура на улице (C):")
        self.add_widget(self.outside_temp_label)
        self.outside_temp_entry = TextInput()
        self.add_widget(self.outside_temp_entry)

        self.inside_temp_label = Label(text="Температура в помещении (C):")
        self.add_widget(self.inside_temp_label)
        self.inside_temp_entry = TextInput()
        self.add_widget(self.inside_temp_entry)

        self.heat_loss_coef_label = Label(text="Коэффициент тепловых потерь:")
        self.add_widget(self.heat_loss_coef_label)
        self.heat_loss_coef_entry = TextInput()
        self.add_widget(self.heat_loss_coef_entry)

        self.num_apartments_label = Label(text="Количество квартир:")
        self.add_widget(self.num_apartments_label)
        self.num_apartments_entry = TextInput()
        self.add_widget(self.num_apartments_entry)

        self.calculate_button = Button(text="Рассчитать")
        self.calculate_button.bind(on_press=self.calculate)
        self.add_widget(self.calculate_button)

        self.total_area_label = Label(text="")
        self.add_widget(self.total_area_label)

        self.total_heat_power_label = Label(text="")
        self.add_widget(self.total_heat_power_label)

        self.save_report_button = Button(text="Сохранить отчет")
        self.save_report_button.bind(on_press=self.save_report)
        self.add_widget(self.save_report_button)

    def calculate(self, instance):
        # Расчет общей площади
        length = float(self.length_entry.text)
        width = float(self.width_entry.text)
        height = float(self.height_entry.text)
        num_rooms = int(self.num_rooms_entry.text)
        area = room_calculate_area(length, width, height)
        self.total_area_label.text = "Общая площадь помещений: {} м^2".format(area * num_rooms)

        # Расчет тепловой мощности
        outside_temp = float(self.outside_temp_entry.text)
        inside_temp = float(self.inside_temp_entry.text)
        heat_loss_coef = float(self.heat_loss_coef_entry.text)
        num_apartments = int(self.num_apartments_entry.text)
        heat_power = apartment_calculate_heat_power(outside_temp, inside_temp, heat_loss_coef)
        self.total_heat_power_label.text = "Тепловая мощность для обогрева помещений: {} Вт".format(heat_power * num_apartments)

    def save_report(self, instance):
        doc = docx.Document()
        doc.add_heading('Результаты расчетов', 0)
        doc.add_paragraph(self.total_area_label.text)
        doc.add_paragraph(self.total_heat_power_label.text)
        doc.save('report.docx')
        popup = Popup(title='Сохранение отчета', content=Label(text='Отчет успешно сохранен в report.docx'), size_hint=(None, None), size=(400, 200))
        popup.open()

class CalculationApp(App):
    def build(self):
        return CalculationForm()

if __name__ == '__main__':
    CalculationApp().run()

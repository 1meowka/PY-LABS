import simple_draw as sd

def draw_house(height, width, start, colorL, color):
    widths = width + start
    sd.rectangle(left_bottom=sd.Point(start-50, 150), right_top= sd.Point(widths+50, height), 
                 color=color)
    for g in range(height, 150, -50):
        if g % 100 == 50:
            for i in range(start, widths, 100):
                sd.rectangle(left_bottom = sd.Point(i, g-50), right_top = sd.Point(i+100, g), 
                             width=1, color=colorL)
        else:
            for i in range(start-50, widths, 100):
                sd.rectangle(left_bottom = sd.Point(i, g-50), right_top = sd.Point(i+100, g), 
                             width=1, color=colorL)
    sd.rectangle(left_bottom=sd.Point(start-50, 150), right_top= sd.Point(widths+50, height), 
                 width=1, color=colorL)
    point_list = [sd.Point(start-80, height), sd.Point(start+width//2, height+200), sd.Point(widths+80, height)]
    sd.polygon(point_list, width = 0, color=sd.COLOR_DARK_RED)

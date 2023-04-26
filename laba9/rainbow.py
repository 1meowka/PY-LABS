import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def draw_rainbow(center, rad, width):
    for g in rainbow_colors:
        sd.circle(center_position = center,radius=rad,color=g, width=width)
        rad -= width

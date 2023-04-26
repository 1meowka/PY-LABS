import simple_draw as sd
import random

def draw_tree(start, colorL, colorT):
    v0 = sd.get_vector(start, angle=90, length=115, width=10)
    v0.draw(colorT)

    def branch(point, angle, length):
        if length < 5:
            return
        elif length < 15:
            vetvi(length, angle, point, colorL, 1)
        elif length < 25:
            vetvi(length, angle, point, colorT, 3)
        elif length < 50:
            vetvi(length, angle, point, colorT, 5)
        else:
            vetvi(length, angle, point, colorT, 8)

    def vetvi(length, angle, point, color, width):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v1.draw(color)
        v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        v2.draw(color)
        next_point1 = v1.end_point
        next_point2 = v2.end_point
        next_length = length * random.uniform(0.60, 0.90)
        branch(point=next_point1, angle=angle-random.uniform(18, 42), length=next_length)
        branch(point=next_point2, angle=angle+random.uniform(18, 42), length=next_length)
    
    branch(point=v0.end_point,angle=90, length=100)

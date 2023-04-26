import simple_draw as sd

def draw_rain():
    def slovarik_snow():
        return {'length': sd.random_number(10, 50),
                'x': sd.random_number(100, 350),
                'y': sd.randint(350, 500)
                }

    snowflakes = []
    for _ in range(20):
        snowflakes.append(slovarik_snow())

    i = 0
    sd.start_drawing()
    while True:
        for snowflake in snowflakes:
            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(center=point, color=sd.background_color, length = snowflake['length'])
            snowflake['x'] -= sd.randint(-10, 10)
            snowflake['y'] -= sd.randint(10, 25)
            point = sd.get_point(snowflake['x'], snowflake['y'])
            sd.snowflake(center=point,color=sd.COLOR_WHITE, length = snowflake['length'])
            if len(snowflakes) > 60:
                snowflakes.remove(snowflake)
            if snowflake['y'] < sd.random_number(220, 270):
                snowflakes.remove(snowflake)
        i += 1
        if i % 2 ==0:
            snowflakes.append(slovarik_snow())
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

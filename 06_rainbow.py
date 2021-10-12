

# (цикл for)

import simple_draw as sd
sd.background_color = (255, 255, 255)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
colors = rainbow_colors[::-1]
# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# i = -1
# end_point = sd.get_point(350, 450)
# for x in range(50, 80, 5):
#     start_point = sd.get_point(x, 50)
#     end_point = sd.get_point(300 + x, 450)
#     i += 1
#     sd.line(start_point, end_point, color=rainbow_colors[i], width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(280, 120)


def bubble(point, step):
    radius = 350

    for i in range(7):
        radius += step
        sd.circle(center_position=point, radius=radius, width=6, color=colors[i])


bubble(point=point, step=7)
sd.pause()

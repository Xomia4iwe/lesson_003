# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.

left_bottom = sd.get_point(0, 0)
right_top = sd.get_point(200, 150)
q = sd.get_point(20, 75)
w = sd.get_point(80, 50)
e = sd.get_point(120, 50)
r = sd.get_point(180, 75)
point1 = sd.get_point(75, 100)
point2 = sd.get_point(125, 100)
radius = 10
sd.circle(center_position=point1, radius=radius, width=2)
sd.circle(center_position=point2, radius=radius, width=2)
line1 = sd.line(start_point=q, end_point=w)
line2 = sd.line(start_point=w, end_point=e)
line3 = sd.line(start_point=e, end_point=r)

sd.ellipse(left_bottom=left_bottom, right_top=right_top, width=2)


def smile(start_x, start_y, line_color):
    start_point = sd.get_point(start_x, start_y)
    sd.circle(center_position=start_point, radius=200, color=line_color, width=3)
    start_point = sd.get_point(start_x - 75, start_y + 75)
    sd.circle(center_position=start_point, radius=20, color=line_color, width=3)
    start_point = sd.get_point(start_x + 75, start_y + 75)
    sd.circle(center_position=start_point, radius=20, color=line_color, width=3)
    start_point = sd.get_point(start_x, start_y + 75)
    end_point = sd.get_point(start_x, start_y - 75)
    sd.line(start_point=start_point, end_point=end_point, color=line_color, width=3)
    point_list = [sd.get_point(start_x - 100, start_y - 100), sd.get_point(start_x - 50, start_y - 125),
                  sd.get_point(start_x + 50, start_y - 125), sd.get_point(start_x + 100, start_y - 100)]
    sd.polygon(point_list=point_list, color=current_color, width=3)


sd.resolution = (501, 501)
sd.background_color = [255, 255, 0]
current_color = [0, 0, 255]
smile(250, 250, current_color)
sd.pause()

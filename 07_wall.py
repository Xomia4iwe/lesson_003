# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# left_bottom = sd.get_point(0, 0)
# right_top = sd.get_point(100, 50)
# sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=1)



step = 0
for y in range(0, 1500, 50):
    y1 = y + 50
    step -=50
    for x in range(step, 1500, 100):
        x1 = x + 100
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x1, y1)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, width=2)







# step = 0
# for y in range(0, 1000, 50):
#     y1 = y + 50
#     step -= 50
#     for x in range(step, 1000, 100):
#         x1 = x + 100
#         point = sd.get_point(x, y)
#         point1 = sd.get_point(x1, y1)
#         sd.rectangle(point, point1, width=1)

sd.pause()

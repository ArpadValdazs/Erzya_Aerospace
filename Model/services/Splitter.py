from CalcLib.methods import sort_loads
from CalcLib import Separator


class Splitter:

    def __init__(self, field, dividers=None):
        if dividers is None:
            dividers = []
        self.field = field
        self.dividers = dividers

    # Сплиттер принимает массив вида [y, [x,x]], а в случае с напряжениями поступает массив [[y,y], [x,x]]
    # Следует модернизировать сплиттер, чтобы он сплитовал всё полноценно по всем разделителям.

    def call_splitter(self):
        splitted_field = []
        if self.dividers != []:
            self.adapter()
            return self.split_load_field(splitted_field)
        else:
            return self.split_load_field(splitted_field)

    def adapter(self):
        print(self.field)
        prev_elem = 0
        for elem in self.dividers:
            self.field.append([0, [prev_elem+elem, prev_elem+elem]])
            prev_elem += elem
        print(sort_loads(self.field))

    # ЭТА ФУНКЦИЯ НЕ ИСПОЛЬЗУЕТСЯ
    def split_tension_field(self, splitted_field):
        divider = Separator.Separator(self.field)
        points, intervals = divider.call_separator()[0], divider.call_separator()[1]
        for i in range(len(intervals)):
            dividers_inside = self.collect_points(points, intervals, i)
            print(dividers_inside)
            if len(dividers_inside) != 0:
                splitted_field.append([[intervals[i][0][0], intervals[i][0][1]], [intervals[i][1][0], dividers_inside[0][1][0]]])
                j = 0
                while j < len(dividers_inside):
                    min_y = intervals[i][0][0]
                    max_y = intervals[i][0][1]
                    x_left = dividers_inside[j][1][0] - intervals[i][1][0]
                    x_right = intervals[i][1][1] - dividers_inside[j][1][0]

                    div_y = min_y + x_left * ((max_y-min_y)/(x_right+x_left))
                    print("div_y", div_y)
                    if j != len(dividers_inside) - 1:
                        splitted_field.append([[intervals[i][0][0], div_y], [dividers_inside[j][1][0], dividers_inside[j - 1][1][0]]])
                    j += 1
                splitted_field.append([[intervals[i][0][0], intervals[i][0][1]], [dividers_inside[len(dividers_inside) - 1][1][0], intervals[i][1][1]]])
            else:
                splitted_field.append(intervals[i])
        splitted_field = sort_loads(points + splitted_field)
        return splitted_field

    def split_load_field(self, splitted_field):
        divider = Separator.Separator(self.field)
        points, intervals = divider.call_separator()[0], divider.call_separator()[1]
        for i in range(len(intervals)):
            dividers_inside = self.collect_points(points, intervals, i)
            if len(dividers_inside) != 0:
                splitted_field.append([intervals[i][0], [intervals[i][1][0], dividers_inside[0][1][0]]])
                j = 0
                while j < len(dividers_inside):
                    if j != len(dividers_inside)-1:
                        splitted_field.append([intervals[i][0], [dividers_inside[j][1][0], dividers_inside[j-1][1][0]]])
                    j += 1
                splitted_field.append([intervals[i][0], [dividers_inside[len(dividers_inside)-1][1][0], intervals[i][1][1]]])
            else:
                splitted_field.append(intervals[i])
        splitted_field = sort_loads(points + splitted_field)
        print("splitted", splitted_field)
        return splitted_field

    def collect_points(self, points, intervals, i):
        loads_inside = []
        for j in range(len(points)):
            # Here we ensure, if a concentrated field were applied inside the interval of a distributed load
            # If so, we split the interval and put the pointed load inside
            if points[j][1][0] > intervals[i][1][0] and points[j][1][0] < intervals[i][1][1]:
                loads_inside.append(points[j])
            else:
                pass
        return loads_inside
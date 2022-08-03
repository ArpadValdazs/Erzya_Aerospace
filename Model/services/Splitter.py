from CalcLib.methods import sort_loads
from CalcLib import Divider


class Splitter:

    def __init__(self, loads):
        self.loads = loads

    def split_loads(self):
        splitted_loads = []
        divider = Divider.Divider(self.loads)
        points, intervals = divider.call_divider()[0], divider.call_divider()[1]
        for i in range(len(intervals)):
            loads_inside = self.collect_points(points, intervals, i)
            if len(loads_inside) != 0:
                splitted_loads.append([intervals[i][0], [intervals[i][1][0], loads_inside[0][1][0]]])
                j = 0
                while j < len(loads_inside):
                    if j != len(loads_inside)-1:
                        splitted_loads.append([intervals[i][0], [loads_inside[j][1][0], loads_inside[j-1][1][0]]])
                    j += 1
                splitted_loads.append([intervals[i][0], [loads_inside[len(loads_inside)-1][1][0], intervals[i][1][1]]])
            else:
                splitted_loads.append(intervals[i])
        splitted_loads = sort_loads(points + splitted_loads)
        return splitted_loads

    def collect_points(self, points, intervals, i):
        loads_inside = []
        for j in range(len(points)):
            # Here we ensure, if a concentrated loads were applied inside the interval of a distributed load
            # If so, we split the interval and put the pointed load inside
            if points[j][1][0] > intervals[i][1][0] and points[j][1][0] < intervals[i][1][1]:
                loads_inside.append(points[j])
            else:
                pass
        return loads_inside
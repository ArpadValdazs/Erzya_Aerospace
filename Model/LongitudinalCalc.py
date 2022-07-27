from CalcLib import methods


class LongitudinalCalc:
    def __init__(self, length, loads, areas, seal, temp):
        self.length = length
        self.loads = loads
        self.areas = areas
        self.seal = seal
        self.temp = temp

    def print(self):
        print(self.length)

    def seal_calc(self):
        lengths = []
        r = 0

        for load in self.loads:
            load_length = load[1][1]-load[1][0]
            if load_length == 0:
                load_length = 1
            lengths.append(load_length)

        for i in range(len(lengths)):
            r += -self.loads[i][0]*lengths[i]
        return r


    def sort_loads(self, loads):
        for i in range(1, len(loads)):
            temp = loads[i]
            j = i - 1
            while j >= 0 and temp[1][0] < loads[j][1][0]:
                loads[j+1] = loads[j]
                j = j - 1
            loads[j+1] = temp
        # print("loads ", loads)
        return loads


    def split_loads(self):

        splitted_loads = []
        points, intervals = methods.divider(self.loads)[0], methods.divider(self.loads)[1]
        for i in range(len(intervals)):
            loads_inside = []
            for j in range(len(points)):
                # Here we ensure, if a concentrated loads were applied inside the interval of a distributed load
                # If so, we split the interval and put the pointed load inside
                if points[j][1][0] > intervals[i][1][0] and points[j][1][0] < intervals[i][1][1]:
                    loads_inside.append(points[j])
                else:
                    print("a")
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
        splitted_loads = self.sort_loads(points + splitted_loads)
        return splitted_loads

    def loads_calc(self):
        # output: [Y,X]. That's uncorrectable mistake
        finish_loads = [[[0, self.seal_calc()], [0, 0]]]
        load = self.split_loads()
        print(load)
        for i in range(len(load)):
            section_length = load[i][1][1] - load[i][1][0]
            if section_length > 0:
                print("before:", finish_loads, "i:", i)
                print(finish_loads[i][0], section_length*load[i][0])
                finish_loads.append([[finish_loads[i][0][1], finish_loads[i][0][1] + section_length*load[i][0]], [load[i][1][0], load[i][1][1]]])
            else:
                finish_loads.append([[finish_loads[i][0][1], finish_loads[i][0][1] + load[i][0]], [load[i][1][0], load[i][1][1]]])
        finish_loads = self.sort_loads(self.fill_empties(finish_loads))
        return finish_loads

    def fill_empties(self, loads):
        for i in range(len(loads)-1):
            print(loads[i+1][1][0] != loads[i][1][1])
            # if (this_load_end != next_load_start) and (this_load_pos !=
            if (loads[i][1][1] != loads[i+1][1][0]) & (loads[i+1][0][0] == loads[i][0][1]):
                loads.append([[loads[i][0][1], loads[i+1][0][0]], [loads[i][1][1], loads[i+1][1][0]]])
            #elif ()
        print("finish.load", loads)
        return loads



#long_calc.split_loads()
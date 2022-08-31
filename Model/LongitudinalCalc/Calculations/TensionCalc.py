from Model.services.Splitter import Splitter
from CalcLib.methods import sort_loads

class TensionCalc:
    def __init__(self, length, loads, areas):
        self.length = length
        self.loads = loads
        self.areas = areas

    def tensions_calc(self, finish_tensions):
        # после изменения сплиттера вытащить его наружу
        splitter = Splitter(self.loads, self.length)
        load = splitter.call_splitter()
        j = 0
        for i in range(len(load)):
            print("areas", self.areas[j])
            if (load[i][0] == 0):
                finish_tensions.append([[finish_tensions[i][0][1], finish_tensions[i][0][1]], [load[i][1][0], load[i][1][1]]])
                j += 1
                continue
            section_length = load[i][1][1] - load[i][1][0]
            print("areas2", self.areas[j], "j", j)
            print("load2", load, "j", finish_tensions, "i", i)
            #print("finish_tensions[i][0][1]", finish_tensions[i][0][1], "load[i][0]", load[i][0], "self.areas[i]", self.areas[i])
            if section_length > 0:
                finish_tensions.append([[finish_tensions[i][0][1], (finish_tensions[i][0][1] + section_length * load[i][0])/self.areas[j]], [load[i][1][0], load[i][1][1]]])
            else:
                finish_tensions.append([[finish_tensions[i][0][1], (finish_tensions[i][0][1] + load[i][0])/self.areas[j]], [load[i][1][0], load[i][1][1]]])
        finish_tensions = sort_loads(self.fill_empties(finish_tensions))
        print("finish", finish_tensions)
        return finish_tensions

    def fill_empties(self, load):
        j = 0
        for i in range(len(load) - 1):
            if (load[i][0] == 0):
                j += 1
                continue
            if (load[i][1][1] != load[i + 1][1][0]) & (load[i + 1][0][0] == load[i][0][1]):
                load.append([[load[i][0][1]//self.areas[j], load[i + 1][0][0]//self.areas[j]], [load[i][1][1], load[i + 1][1][0]]])
        return load

    def tension_steps(self):
        length_map = [[0, self.length[0]]]
        steps = []
        for i in range(len(self.length)-1):
            length_map.append([length_map[i][1], length_map[i][1]+self.length[i+1]])
        for elem in self.load_map:
            for i in range(len(length_map)-1):
                if (length_map[i][1] in range(elem[1][0], elem[1][1])) & (length_map[i][1] != elem[1][0]):
                    steps.append(length_map[i][1])
        print("steps", steps)
        splitter = Splitter(self.load_map, steps)
        result = splitter.call_splitter()
        print("result: ", result)
        #print(length_map)
        #print(steps)


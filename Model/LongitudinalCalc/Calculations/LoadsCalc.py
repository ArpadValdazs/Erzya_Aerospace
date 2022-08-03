from CalcLib.methods import sort_loads
from Model.services.Splitter import Splitter


class LoadsCalc:
    def __init__(self, length, loads, seal, temp):
        self.length = length
        self.loads = loads
        self.seal = seal
        self.temp = temp

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

    def loads_calc(self):
        # output: [Y,X]. That's uncorrectable mistake
        finish_loads = [[[0, self.seal_calc()], [0, 0]]]
        splitter = Splitter(self.loads)
        load = splitter.split_loads()
        for i in range(len(load)):
            section_length = load[i][1][1] - load[i][1][0]
            if section_length > 0:
                finish_loads.append([[finish_loads[i][0][1], finish_loads[i][0][1] + section_length*load[i][0]], [load[i][1][0], load[i][1][1]]])
            else:
                finish_loads.append([[finish_loads[i][0][1], finish_loads[i][0][1] + load[i][0]], [load[i][1][0], load[i][1][1]]])
        finish_loads = sort_loads(self.fill_empties(finish_loads))
        return finish_loads

    def fill_empties(self, loads):
        for i in range(len(loads)-1):
            if (loads[i][1][1] != loads[i+1][1][0]) & (loads[i+1][0][0] == loads[i][0][1]):
                loads.append([[loads[i][0][1], loads[i+1][0][0]], [loads[i][1][1], loads[i+1][1][0]]])
        return loads
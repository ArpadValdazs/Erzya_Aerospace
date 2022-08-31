from CalcLib.methods import sort_loads
from Model.services.Splitter import Splitter


class LoadsCalc:
    def __init__(self, length, loads, temp, areas):
        self.length = length
        self.loads = loads
        self.temp = temp
        self.areas = areas

    def loads_calc(self, finish_loads):
        # output: [Y,X]. That's uncorrectable mistake
        splitter = Splitter(self.loads)
        load = splitter.call_splitter()
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


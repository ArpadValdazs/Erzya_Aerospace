from Model.LongitudinalCalc.Calculations import LoadsCalc, TensionCalc
from View.Plotter import Plotter


class LongitudinalCalc:
    def __init__(self, length, loads, areas, seal, temp, jung):
        self.length = length
        self.loads = loads
        self.areas = areas
        self.seal = seal
        self.temp = temp
        self.jung = jung

    def loads_calc(self):

        loads_calc = LoadsCalc.LoadsCalc(self.length, self.loads, self.temp, self.areas)
        finish_loads = [[[0, self.seal_calc()], [0, 0]]]
        load_map = loads_calc.loads_calc(finish_loads)

        areas = self.organize_areas(self.areas)
        print("self.loadsqa", self.loads)
        tension_calc = TensionCalc.TensionCalc(self.length, self.loads, self.areas)
        # Зарезервировать первое место для заделки
        finish_tensions = [[[0, self.seal_calc()/self.areas[0]], [0, 0]]]
        tension_map = tension_calc.tensions_calc(finish_tensions)
        # plotter = Plotter(load_map, self.length)
        # plotter.loads_graph()

        #tensions = tension_calc.tensions_calc()
        plotter = Plotter(tension_map, self.length)
        plotter.loads_graph()
        res = load_map
        return res

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


    def organize_areas(self, areas):
        for elem in areas:
            if type(elem) == list:
                if len(elem) == 2:
                    print(2)
                elif len(elem) == 3:
                    print(3)
                elif len(elem) == 4:
                    print(4)
            else:
                return areas




#long_calc.split_load_field()
from Model.LongitudinalCalc.Calculations import LoadsCalc, TensionCalc


class LongitudinalCalc:
    def __init__(self, length, loads, areas, seal, temp, jung):
        self.length = length
        self.loads = loads
        self.areas = areas
        self.seal = seal
        self.temp = temp
        self.jung = jung

    def loads_calc(self):
        loads_calc = LoadsCalc.LoadsCalc(self.length, self.loads, self.seal, self.temp)
        load_map = loads_calc.loads_calc()
        Tensions = TensionCalc.TensionCalc(self.length, load_map, self.areas)
        res = Tensions.tensions_calc()
        return res




#long_calc.split_loads()
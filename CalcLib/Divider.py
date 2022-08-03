class Divider:

    def __init__(self, loads, mode="standart"):
        self.loads = loads
        self.mode = mode

    def call_divider(self):
        if self.mode == "no_loads":
            return self.no_loads_divider()
        elif self.mode == "tensions":
            pass
        else:
            return self.standart_divider()

    def standart_divider(self):
        intervals = []
        points = []
        for i in range(len(self.loads)):
            # This cycle divides loads on lists with only concentrated and distributed loads
            if self.loads[i][1][1] - self.loads[i][1][0] == 0:
                points.append(self.loads[i])
            else:
                intervals.append(self.loads[i])
        return [points, intervals]

    def no_loads_divider(self):
        intervals = []
        points = []
        no_loads = []
        for i in range(len(self.loads)):
            if self.loads[i][1][1] - self.loads[i][1][0] == 0:
                points.append(self.loads[i])
            elif self.loads[i][0][1] - self.loads[i][0][0] == 0:
                no_loads.append(self.loads[i])
            else:
                intervals.append(self.loads[i])
        return [points, intervals, no_loads]
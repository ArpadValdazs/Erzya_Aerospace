class Separator:

    def __init__(self, field, mode="standart"):
        self.field = field
        self.mode = mode

    def call_separator(self):
        if self.mode == "vectorless":
            return self.vectorless_separator()
        elif self.mode == "tensions":
            pass
        else:
            return self.standart_separator()

    def standart_separator(self):
        intervals = []
        points = []
        for i in range(len(self.field)):
            # This cycle divides field on lists with only concentrated and distributed field
            if self.field[i][1][1] - self.field[i][1][0] == 0:
                points.append(self.field[i])
            else:
                intervals.append(self.field[i])
        return [points, intervals]

    def vectorless_separator(self):
        intervals = []
        points = []
        no_loads = []
        print("field", self.field)
        for i in range(len(self.field)):
            if self.field[i][1][1] - self.field[i][1][0] == 0:
                points.append(self.field[i])
            elif self.field[i][0][1] - self.field[i][0][0] == 0:
                no_loads.append(self.field[i])
            else:
                intervals.append(self.field[i])
        return [points, intervals, no_loads]
class TensionCalc:
    def __init__(self, length, load_map, areas):
        self.length = length
        self.load_map = load_map
        self.areas = areas

    def tensions_calc(self):
        self.tension_steps()
        return (self.load_map)

    def tension_steps(self):
        print("aa", self.load_map)
        length_map = [[0, self.length[0]]]
        steps = []
        for i in range(len(self.length)-1):
            print("aa", self.length[i], self.length[i-1])
            length_map.append([length_map[i][1], length_map[i][1]+self.length[i+1]])
        for elem in self.load_map:
            for i in range(len(length_map)-1):
                if (length_map[i][1] in range(elem[1][0], elem[1][1])) & (length_map[i][1] != elem[1][0]) :
                    steps.append(length_map[i][1])

        print(length_map)
        print(steps)


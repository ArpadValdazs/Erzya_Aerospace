import matplotlib.pyplot as plt
import numpy as np
from CalcLib import methods


class Plotter:
    def __init__(self, loads, len):
        self.loads = loads
        self.len = len

    def loads_graph(self):
        # Closed interval from length
        # All loads should be divided on concentrated and distributed
        points, intervals, no_loads = methods.divider_sec(self.loads)[0], methods.divider_sec(self.loads)[1], methods.divider_sec(self.loads)[2]
        print("no_loads", no_loads)
        x_mass = []
        y_mass = []
        for elem in intervals:
            x = np.linspace(elem[1][0], elem[1][1], 10)
            x_mass.append(x)
            y = np.linspace(elem[0][0], elem[0][1], 10)
            print("y", y)
            y_mass.append(y)

        fig, ax = plt.subplots()
        plt_color = '#77AAEE'
        for i in range(len(x_mass)):
            ax.plot(x_mass[i], y_mass[i], color='black')
            plt.fill_between(x_mass[i], y_mass[i], np.zeros_like(y_mass[i]), color=plt_color)
        for elem in no_loads:
            ax.hlines(elem[0][0], elem[1][0], elem[1][1], color='black')
            plt.fill_between([elem[1][0], elem[1][1]], elem[0][0], color=plt_color)
        for elem in points:
            print(elem)
            ax.vlines(elem[1][0], elem[0][0], elem[0][1], color='black')
        plt.ylabel("N", fontsize=14, fontweight="bold", rotation=90)
        ax.grid()
        plt.show()
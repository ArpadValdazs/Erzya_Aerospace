from Model.LongitudinalCalc import LongitudinalCalc
from View.Plotter import Plotter


task_len = [1, 4, 1]
task_areas = (3, 1, 1.5)
#task_loads = [[-1, [0, 5]], [2, [1, 1]], [-1, [6, 6]]]
#task_loads = [[2, [1, 1]], [-1, [6, 6]]]
#task_loads = [[2, [2, 2]], [-1, [0, 3]], [-1, [4, 6]], [2, [5, 5]], [-1, [6, 6]]]
#task_loads = [[2, [3, 3]], [1, [0, 2]], [-1, [4, 6]], [2, [5, 5]]]
task_loads = [[-1, [0, 2]], [-1, [4, 5]], [-1, [6, 6]]]
#task_loads = [[-1, [0, 1]], [2, [2, 2]], [-2, [3, 3]], [-1, [5, 6]]]
task_seal = 0
task_temp = 0


long_calc = LongitudinalCalc(task_len, task_loads, task_areas, task_seal, task_temp)
loads = long_calc.loads_calc()

plotter = Plotter(loads, task_len)
plotter.loads_graph()
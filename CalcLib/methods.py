def divider(loads):
    intervals = []
    points = []
    for i in range(len(loads)):
        # This cycle divides loads on lists with only concentrated and distributed loads
        if loads[i][1][1] - loads[i][1][0] == 0:
            points.append(loads[i])
        else:
            intervals.append(loads[i])
    return [points, intervals]

def divider_sec(loads):
    intervals = []
    points = []
    no_loads = []
    for i in range(len(loads)):
        # This cycle divides loads on lists with only concentrated and distributed loads
        if loads[i][1][1] - loads[i][1][0] == 0:
            points.append(loads[i])
        elif loads[i][0][1] - loads[i][0][0] == 0:
                no_loads.append(loads[i])
        else:
            intervals.append(loads[i])
    return [points, intervals, no_loads]


# def closed_interval(num1, num2, step):
#     result = []
#     i = num1
#     print("num1 ", num1, "num2 ", num2, "step", step)
#     if step > 0:
#         while i <= num2:
#             result.append(round(i, 1))
#             i += step
#     else:
#         while i >= num2:
#             result.append(round(i, 1))
#             i += step
#     print("length", result)
#     return result
#
#
# def merge_intervals(interval):
#     result = []
#     for elem in interval:
#         for number in elem:
#             result.append(number)
#     return result

def sort_loads(loads):
    for i in range(1, len(loads)):
        temp = loads[i]
        j = i - 1
        while j >= 0 and temp[1][0] < loads[j][1][0]:
            loads[j+1] = loads[j]
            j = j - 1
        loads[j+1] = temp
    return loads
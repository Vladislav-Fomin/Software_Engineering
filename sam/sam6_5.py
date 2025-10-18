import math
def calc_distance(num1, num2):
    return math.sqrt((num2[0] - num1[0])**2 + (num2[1] - num1[1])**2)
def taksometr(dict):
    res = {}
    for id, coordinates in dict.items():
        total_dist = 0
        max = 0
        for i in range(len(coordinates) -1):
            local_dist = calc_distance(coordinates[i], coordinates[i + 1])
            total_dist += local_dist
            if local_dist > max:
                max = local_dist
        if total_dist > 50:
            res[id] = (total_dist, max)
    return res

test1 = {
    101: [(0, 0), (30, 0), (30, 40)],
    102: [(0, 0), (10, 0), (10, 10)],
    103: [(0, 0), (0, 25), (25, 25), (25, 0)]
}

test2 = {
    201: [(0, 0), (5, 0)],
    202: [(1, 1), (2, 2), (3, 3)]
}
print("Тест 1:", taksometr(test1))
print("Тест 2:", taksometr(test2))
import math
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_a, max_b, max_c = max(one), max(two), max(three)
min_a, min_b, min_c = min(one), min(two), min(three)

max_area = triangle_area(max_a, max_b, max_c)
min_area = triangle_area(min_a, min_b, min_c)
print(f"Площадь треугольника с максимальными стороными: {max_area}\nПлощадь треугольника с минимальными стороными: {min_area}")

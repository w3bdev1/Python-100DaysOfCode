import math

height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = int(input("Area coverage per can: "))

def cans_needed(height, width, coverage):
    area = height * width
    return math.ceil(area / coverage)

print(cans_needed(height, width, coverage))
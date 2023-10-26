# heights = [181, 124, 165, 174]
heights_str = input('Give comma-separated list of heights: ')
heights = [int(h.strip()) for h in heights_str.split(',')]

total_height = 0
number_of_items = 0

for h in heights:
    total_height += h
    number_of_items += 1

avg_height = round(total_height / number_of_items)
print(f"Average height is {avg_height}")
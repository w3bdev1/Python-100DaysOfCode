# 2 + 4 + 6 + ... + 100

sum = 0
for num in range(2, 101, 2):
    sum += num

print(f"Sum of even numbers [2,100] is {sum}")
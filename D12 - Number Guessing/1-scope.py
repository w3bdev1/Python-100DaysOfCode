num = 1

def increase_num():
    num = 2
    print(f"Number inside function: {num}")

increase_num()
print(f"Number outside function before if block: {num}")

if num:
    num = 3
print(f"Number outside function and if block: {num}")
num = 1

def increase_num():
    global num
    num += 1
    print(f"num within function: {num}")

increase_num()
print(f"num outside function: {num}")
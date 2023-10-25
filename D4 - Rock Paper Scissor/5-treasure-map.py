row1 = ["🟧", "🟧", "🟧"]
row2 = ["🟧", "🟧", "🟧"]
row3 = ["🟧", "🟧", "🟧"]

map = [row1, row2, row3]

print('This is the current map:')
print(f"{row1}\n{row2}\n{row3}")

position = input("Pick position (row,column) to hide the treasure? ")
position_list = [x.strip() for x in position.split(',')]
row = int(position_list[0])-1
col = int(position_list[1])-1

map[row][col] = '🟪'

print(f"{row1}\n{row2}\n{row3}")
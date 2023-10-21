# Tip Calculator

print('------------------------')
print('|   PRINT CALCULATOR   |')
print('------------------------')

bill = int(input('What was the total bill? ₹'))
tip = int(input('What percentage of tip would you like to give? 10, 12 or 15? '))
split = int(input('How many people to split the bill? '))

bill_with_tip = bill * (100 + tip) / 100
split_amount = round(bill_with_tip / split)

print(f'Everyone needs to pay ₹{split_amount}')
print('Welcome to Python Pizzas!')

size = input('What size pizza? (S, M, or L)? ')

bill = 0

if size == 'S':
    print('Price of small pizza ₹100')
    bill += 100

    add_pepperoni = input('Do you want pepperoni? (Y or N)? ')
    print('Pepperoni for small pizza ₹10')
    bill +=10
else:
    if size =='M':
        print('Price of medium pizza ₹150')
        bill += 150
    elif size == 'L':
        print('Price of large pizza ₹200')
        bill += 200
    
    add_pepperoni = input('Do you want pepperoni? (Y or N)? ')
    print('Pepperoni for medium or large pizza ₹15')
    bill +=15

extra_cheese = input('Do you want extra cheese? (Y or N)? ')
if extra_cheese == 'Y':
    print('Extra cheese for any size pizza ₹10')
    bill +=10

print(f"Your total bill {bill}")

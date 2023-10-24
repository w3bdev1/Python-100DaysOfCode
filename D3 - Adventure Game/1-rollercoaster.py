print("Welcome to the Roller Coaster!")
height = int(input("What is your height (in cm)? "))

if height >= 120:
    print('You are allowed to ride')

    age = int(input("What is your age (in years)? "))
    if age >= 18:
        print('Pay ₹100')
    else:
        print('Pay ₹50')
else:
    print('You are not allowed')
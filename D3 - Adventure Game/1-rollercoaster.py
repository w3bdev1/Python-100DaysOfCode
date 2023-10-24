print("Welcome to the Roller Coaster!")
height = int(input("What is your height (in cm)? "))

if height >= 120:
    print('You are allowed to ride')
    bill = 0

    age = int(input("What is your age (in years)? "))
    if age >= 18:
        print('Adult ticket price ₹100')
        bill = 100
    elif age >= 12:
        print('Youth ticket price ₹70')
        bill = 70
    else:
        print('Child ticket price ₹50')
        bill = 50
    
    want_photo = input('Do you want your photo taken? (Y or N): ')
    if want_photo == 'Y':
        print('Extra charge for photo: ₹20')
        bill += 20
    
    print(f"Total bill: {bill}")
else:
    print('You are not allowed')
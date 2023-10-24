print("Love Calculator - Find your foolproof destiny :P")
name1 = input('Whats your name? ')
name2 = input('Whats the name of the lucky person? ')

combined_name = name1+name2
combined_name = combined_name.lower()

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
# e = combined_name.eower().count('e')

true = t + r + u + e
love = l + o + v + e

score = int(f"{true}{love}")

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos!")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
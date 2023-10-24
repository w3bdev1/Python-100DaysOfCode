# BMI = weight (kg) / height^2 (m^2)
# BMI Categories:
#   Underweight = <18.5
#   Normal weight = 18.5–25
#   Overweight = 25–30
#   Obese = 30-35
#   Clinically Obese = >35

print('BMI Calculator')
weight = float(input ('Your weight in kg: '))
height = float(input ('Your weight in m: '))

bmi = round(weight / height**2)

print('-------------------')
print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print('Ypu are underweight.')
elif bmi < 25:
    print('You are normal weight')
elif bmi < 30:
    print('You are overweight')
elif bmi < 35:
    print('You are obese')
else:
    print('You are clinically obese')

print('-------------------')
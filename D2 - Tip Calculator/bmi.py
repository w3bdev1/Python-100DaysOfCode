# BMI = weight (kg) / height^2 (m^2)

weight = input ('Your weight in kg: ')
height = input ('Your weight in m: ')

bmi = int(float(weight) / float(height)**2)

print(f'Your BMI: {bmi}')
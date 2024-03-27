name = input("What's your name? ")
height = input(f"How tall are you, {name}? (in cm) ")
weight = input(f"How much do you weigh, {name}? (in kg) ")

height = float(height)/100
weight = float(weight)

bmi = weight / pow(height, 2)
bmi = round(bmi, 2)

print(f"{name}, your {bmi = }")




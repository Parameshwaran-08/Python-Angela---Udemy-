print("Welcome to know your BMI !")

weight = int(input("Enter your bodyweight (in kilogram) : "))
height = float(input("Enter your height (in metre) : "))
bmi = weight / (height**2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f} ! And you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f} ! And you are normal in weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f} ! And you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f} ! And you are obese.")
else:
    print(f"Your BMI is {bmi:.2f} ! And you are clinically overweight.")

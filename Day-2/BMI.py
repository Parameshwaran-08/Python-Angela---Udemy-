print("Welcome to know your BMI !")
 
weight = int(input("Enter your bodyweight (in kilogram) : "))
height = float(input("Enter your height (in metre) : "))
bmi = weight / (height**2)

print(f"Your BMI is {bmi:.2f} !")

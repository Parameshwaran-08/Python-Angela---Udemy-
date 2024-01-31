print("Welcome to the ROLLERCOSTER ride ! ")

height = float(input("Enter your height (in cm) : "))

if height >= 120:
    print(f"You can ride in the rollercoster !")

    age = int(input("Enter your age : "))

    if age < 12:
        print(f"You have to pay 5$")
    elif age <= 18:
        print(f"You have to pay 7$")
    else:
        print(f"You have to pay 12$")

else:
    print(f"Sorry you are a {round(height):.1f} cm midget. You cannot ride.")
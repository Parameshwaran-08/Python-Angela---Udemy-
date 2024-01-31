print("Welcome to the ROLLERCOSTER ride ! ")

height = float(input("Enter your height (in cm) : "))

if height >= 120:
    print(f"You can ride in the rollercoster !")

    age = int(input("Enter your age : "))
    bill = 0
    want_photos = input("Do you want photos (EXTRA 3$ with ticket - yes or no) : ")

    if age < 12:
        bill = 5 

    elif age <= 18:
        bill = 7

    else:
        bill = 12

    if want_photos == "yes":
        print(f"You have to pay {bill+3}$")

    else:
        print(f"You have to pay {bill}$")

else:
    print(f"Sorry you are a {round(height):.1f} cm midget. You cannot ride.")
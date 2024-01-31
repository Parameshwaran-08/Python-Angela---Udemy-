print(f"Thank you for choosing python pizza deliveries.")

size = input("choose the size of the pizza (L, M or S) : ")
add_pepporoni = input("Do you want pepporoni (y or n) : ")
add_cheese = input("Do you want cheese (y or n) : ")
bill = 0

if size == "S":
    bill += 15

elif size == "M":
    bill += 20

else:
    bill += 25

if add_pepporoni == "y":
    if size == "S":
        bill += 2   

    else:
        bill += 3

if add_cheese == "y":
    bill += 1

print(f"Your final bill is ${bill}")
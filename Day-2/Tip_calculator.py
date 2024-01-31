print("Welcome to the tip calculator ! ")

total_bill = float(input("Enter the total bill ($) : "))
tip_percentage = int(input("Enter the tip percentage you likely to give (10, 12 or 15) : "))
total_ppl = int(input("How people are splitting the bill : "))
bill_overall = total_bill + (total_bill*(tip_percentage/100))
bill_per_person = round((bill_overall/total_ppl),2)

print(f"Each person has to pay {bill_per_person:.2f}$")
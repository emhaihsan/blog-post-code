print("Welcome to the restaurant bill calculator!")

# Input the total bill
bill = float(input("What was the total bill? $"))

# Input the tip percentage
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Input the tax percentage
tax = float(input("What is the tax percentage? "))

# Input the fixed service fee
service_fee = float(input("What is the fixed service fee? $"))

# Input the number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent

# Calculate the tax amount
tax_as_percent = tax / 100
total_tax_amount = bill * tax_as_percent

# Calculate the total bill including tax, tip, and service fee
total_bill = bill + total_tip_amount + total_tax_amount + service_fee

# Calculate the bill per person
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Display the amount each person should pay
print(f"Each person should pay: ${final_amount}")
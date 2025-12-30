units = int(input("Enter the number of electricity units consumed: "))

if units <= 100:
    bill_amount = units * 5
elif units <= 200 and units > 100:
    bill_amount = units * 7
elif units <= 300 and units > 200:
    bill_amount = units * 10
else:
    bill_amount = units * 15

print(f"Your electricity bill amount is: {bill_amount} rupees")
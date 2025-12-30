salary = int(input("Enter your salary: "))

if salary <= 250000:
    tax = 0
elif salary <= 500000 and salary > 250000:
    tax = salary * 0.05
elif salary <= 1000000 and salary > 500000:
    tax = salary * 0.20
else:
    tax = salary * 0.30

print(f"Your income tax amount is: {tax} rupees")

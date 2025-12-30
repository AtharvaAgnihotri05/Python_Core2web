age = int(input("Enter your age: "))
weight = int(input("Enter your weight (in kgs): "))
hb = float(input("ENter you hb : "))

if age > 18 and age < 65:
    if weight > 50 and hb > 12.5:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood due to weight or hb criteria.")
else:
    print("You are not eligible to donate blood due to age criteria.")
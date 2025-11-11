num1 = int(input("Enter a number 1 : "))
num2 = int(input("Enter a number 2 : "))
num3 = int(input("Enter a number 3 : "))


if num1 > num2 and num1 > num3:
    print("Num1 is greater than num1 and num2")
elif num2 > num3 and num2 > num1:
    print("Num2 is greater than num1 and num3")
else:
    print("Num3 is greater than num1 and num2")


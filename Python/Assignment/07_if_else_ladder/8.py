num = int(input("Enter number : "))

if num > 0 and num % 2 == 0:
    print("Positive Even")
elif num > 0 and num % 2 != 0:
    print("Positive Odd")
elif num < 0 and num % 2 == 0:
    print("Negative Even")
elif num < 0 and num % 2 != 0:
    print("Negative Odd")
else:
    print("zero")



percentage = int(input("Enter your percentage :"))

if percentage > 90:
    print("Elite Program")
elif percentage < 90 and percentage > 80:
    print("Standard Program")
elif percentage < 80 and percentage > 70:
    print("Basic Program")
else:
    print("Not eligible")


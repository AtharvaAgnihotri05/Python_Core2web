angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("The triangle is a right-angled triangle.")
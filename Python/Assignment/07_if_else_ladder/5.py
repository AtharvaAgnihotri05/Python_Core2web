temp = int(input("Enter the temperature in Celsius: "))

if temp <= 0:
    print("Freezing weather")
elif temp > 0 and temp <= 10:
    print("Very Cold weather")
elif temp > 10 and temp <= 20:
    print("Cold")
elif temp > 20 and temp <= 30:
    print("Warm")
elif temp > 30 and temp <= 40:
    print("Hot")
else:
    print("Extreme Heat")


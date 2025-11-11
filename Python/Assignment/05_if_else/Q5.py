
day = int(input("Enter weekday number : "))

match day:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thurday")
    case 4:
        print("Friday")
        
    case 5:
        print("Saturday")
    case _:
        print("Sunday")

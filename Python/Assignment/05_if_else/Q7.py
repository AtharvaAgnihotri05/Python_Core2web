

month = int(input("Enter month number : "))

month_with_31_days = [1,3,5,7,8,10,12]

month_with_30_days = [4,6,9,11]

if month in month_with_31_days:
    match month:
        case 1:
            print("Jan has 31 days")
        case 3:
            print("March has 31 days")
        case 5:
            print("May has 31 days")
        case 7:
            print("July has 31 days")
        case 8:
            print("Augest has 31 days")
        case 10:
            print("October has 31 days")
        case 12:
            print("Dec has 31 days")
elif month in month_with_30_days:
    match month:
        case 4:
            print("April has 30 days")
        case 6:
            print("June has 30 days")
        case 9:
            print("Sept has 30 days")
        case 11:
            print("Nov has 30 days")
else:
    print("Feb has 29 or 28 days")


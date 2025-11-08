
# match- case 

day = input('Enter day : ')

match day:
    case "Mon":
        print("Start of week")
    case "Fri":
        print("start of weekend")
    case "Sat":
        print("Weekend")
    case _ :
        print("WeekDay")


from enum import Enum

class day(Enum):
        Monday = 1
        Tuesday = 2
        Wednesday = 3
        Thursday = 4
        Friday = 5
        Saturday = 6
        Sunday = 7

class Solution:
        def WeekOfDay():
            Week = int(input("Enter a number: "))
            match Week:
                case 1 :
                    print(day.Monday.name)
                case 2 :
                    print(day.Tuesday.name)
                case 3 :
                    print(day.Wednesday.name)
                case 4 :
                    print(day.Thursday.name)
                case 5 :
                    print(day.Friday.name)
                case 6 :
                    print(day.Saturday.name)
                case 7 :
                    print(day.Sunday.name)
                case _ :
                    print("Invalid")
        WeekOfDay()
    

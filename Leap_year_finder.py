i=0
while i<5:
    year=int(input("Enter the year:"))

    """ if  some years the year divided by 4 and not divided by 100  like 2004.
        or some years divided by 400 like 2000"""
    if((year%4==0)and(year%100!=0)or(year%400==0)):

        print("{} this year is leap year".format(year))
    else:
        print("Its not a leap year")
    i+=1
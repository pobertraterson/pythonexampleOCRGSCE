import time
#this is an example of asking a user how old 
#something is, the usage and see if it can be sold
age=input("How old is you car?: ")
mileage=input("How many miles has your car done?: ")
iage=int(age)
imileage=int(mileage)
if iage<10:
    if imileage<1000:
        print("Your car can be sold")
    else:
        print("Your car cannot be sold")
else:
    print("Your car cannot be sold")
time.sleep(5)
#you don't need the time.sleep, but it's so you
#can see the result of the script
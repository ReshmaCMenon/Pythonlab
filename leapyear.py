cy=int(input("enter the current year:"))
x=int(input("enter the last year:"))
if(x>cy):
    print("Leap years are:")
for i in range(cy,x+1):
    if(i%4==0):
        if(i%100==0):
            if(i%400==0):
                print(i)
        else:
            print(i)
else:
    print("invalid input")

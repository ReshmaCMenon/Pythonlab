n=int(input("enter the limit:"))
print("fibonacci series :")
a=0
b=1
print(a)
print(b)
count=1
while(count<=n-1):
    c=a+b
    a=b
    b=c
    count+=1
    print(c)

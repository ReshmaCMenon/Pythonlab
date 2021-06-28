a=[]
n=input("Enter the  sen:")
str=n.split(" ")
for i in str:
    if i not in a:
        a.append(i)
for i in range(0,len(a)):
    print("The word",a[i],"occurs",str.count(a[i]),"times")

    
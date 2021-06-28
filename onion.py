str=input("Enter the string:")
a=str[0]
for i in range(0,len(str)):
    str=str.replace(a,'$')
    str=a+str[1:]
print("String is:",str)

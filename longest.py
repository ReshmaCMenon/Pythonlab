a=[]
n=int(input("Enter the no of words:"))
for i in range(n):
    m=input("enter the word:")
    a.append(m)
print(a)
max_length=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max_length):
        max_length=len(i)
        temp=i
print("longest word:",temp)
print("maxlength:",max_length)
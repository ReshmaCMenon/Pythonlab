n=int(input("Enter the size:"))
a=[]
sum=0
print("Enter the numbers:")
for i in range(n):
    a.append(int(input()))
print("List is:",a)
print("Sum is:")
for i in range(n):
    sum=sum+a[i]
print(sum)
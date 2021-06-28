n=int(input("enter the size:"))
a=[]
print("Enter the numbers:")
for i in range(0,n):
    a.append(int(input()))
pos=[i for i in a if i>=0]
print(pos)
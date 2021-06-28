a=[]
n=input("Enter the word:")
l=len(n)
for i in range(l):
    a.insert(i,n[i])
print(a)
l3=[ord(a[i]) for i in range(l)]
print("ordinal value:",l3)
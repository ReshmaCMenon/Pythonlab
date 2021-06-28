l1=['a','e','i','o','u']
l2=[]
a=input("enter the word:")
length=len(a)
for i in range(length):
    l2.insert(i,a[i])
l3=[i for i in l2 if i in l1]
print("list of vowels",l3)
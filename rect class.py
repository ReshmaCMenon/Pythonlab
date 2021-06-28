class Rectangle:
    def __init__(self):
        self.length=int(input("Enter the length:"))
        self.breadth=int(input("Enter the breadth:"))
    def area(self):
        self.a=self.length*self.breadth
        print("Area=",self.a)
        return self.a
    def perimeter(self):
        self.p=2*(self.length+self.breadth)
        print("perimeter=",self.p)
        return self.p
x=Rectangle()
print("---Rect 1--")
a1=x.area()
x.perimeter()

y=Rectangle()
print("---Rect 2--")
b1=y.area()
y.perimeter()

if a1>b1:
    print("rect 1is big")
elif a1==b1:
    print("same area")
else :
    print("rect 2 is big")
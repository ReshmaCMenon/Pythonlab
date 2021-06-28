class Rect:
    def __init__(self):
        self.length=int(input("Enter the length:"))
        self.breadth=int(input("Enter the breadth:"))
    def area(self):
        self.a=self.length*self.breadth
        return self.a
    def __lt__(self, other):
        if(self.area() < other.area()):
           return True
        else :
            return False
print("---Rect 1--")
x=Rect()
print("---Rect 2--")
y=Rect()
if(x<y):
    print("rec1 is < rect2")
else:
    print("rec2 is < rect1")
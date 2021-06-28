print("Area of square")
a = int(input("Enter the side of square:"))
x = lambda a: a * a
print("Area of square is:", x(a))

print("\nArea of rectangle")
l = int(input("Enter the length of rectangle:"))
b = int(input("Enter the breadth of rectangle:"))
x = lambda a: l * b
print("Area of rectangle is:", x(a))

print("\nArea of triangle")
l = int(input("Enter the base of triangle:"))
b = int(input("Enter the height of triangle:"))
x = lambda a: 0.5 * l * b
print("Area of triangle is:", x(a))

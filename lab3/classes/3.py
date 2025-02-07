class Shape:
    def area(self):
        return 0
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = float(input("Length: "))
width = float(input("Width: "))
S_ploshad =Rectangle(length,width)
print("Area of the rectangle:",S_ploshad.area())



    
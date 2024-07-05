"""Rectangle"""
class Rectangle:
    """Rectangle"""
    def __init__(self, height, width):
        """_"""
        self.height = height
        self.width = width

    def calculate_area(self):
        """_"""
        return self.height * self.width

    def calculate_perimeter(self):
        """_"""
        return (2 * self.width) + (2 * self.height)
rectangle = Rectangle(float(input()), float(input()))

condition = input()
if condition == "area":
    resultt = rectangle.calculate_area()
else:
    resultt = rectangle.calculate_perimeter()
print("%.2f" % resultt)

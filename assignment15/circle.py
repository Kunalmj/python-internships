import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_circumference(self):
        return self.get_perimeter()

# Example usage:
if __name__ == "__main__":
    # Creating a circle with center at (0, 0) and radius 5
    circle = Circle(0, 0, 5)
    
    # Calculating and printing area, perimeter and circumference
    print("Area of the circle:",round(circle.get_area(),3))         #rounding off to 3 decimal place
    print("Perimeter of the circle:",round(circle.get_perimeter(),3))
    print("Circumference of the circle:",round(circle.get_circumference(),3))

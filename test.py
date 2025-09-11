class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

def check_shape(shape):
    match shape:
      
      	# Match Circle and extract the radius
        case Circle(radius):  
            print(f"circle radius {radius}.")
            
        # Match Rectangle and extract width and height
        case Rectangle(width, height):  
            print(f"Rectangle width {width} and height {height}.")
            
        # Default case for any other object
        case _:  
            print("This is an unknown shape.")

# Create objects of Circle and Rectangle
circle = Circle(10)
rectangle = Rectangle(4, 6)

# Test with different shapes
check_shape(circle)     
check_shape(rectangle)
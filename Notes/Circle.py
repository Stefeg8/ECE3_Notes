import math

# Classes can be used to create objects 
# in this example, we use the circle class to create a circle class
# See below for how to call this class
class Circle:

    # constructor method
    # The constructor method is responsible for initializing the attributes of the class/object
    # Here, we create a circle object with radius set to the user input
    def __init__(self, radius=1):
        # We use the self keyword to define this radius as the radius of the circle object that we just created
        # You wouldn't want to do radius = radius because then the radius of the circle object wouldn't be defined
        self.radius = radius # This is a public variable that can be accessed from outside the class
        self.__radius = radius # This is a private variable that cannot be accessed from outside the class. Private properties are prefixed with "__"
                               # For the self.__radius variable this is denoted by the double underscore right after the "self."
                               # This is useful if you want to create a variable that is used for calculations in the class or other stuff idfk
    # instance method
    def getRadius(self):
        return self.radius  

    # instance method
    # This method gets the perimeter of the circle
    # The self.radius variable is stored in the circle object that you created
    def getPerimeter(self):
        perimeterOfThisCircle = 2 * self.radius * math.pi
        return perimeterOfThisCircle

    # instance method
    def getArea(self):
        return self.radius * self.radius * math.pi

    # instance method
    # you can use this to change the value of the radius
    def setRadius(self, radius):
        # Here you must do self.radius because self.radius is the radius of the circle object
        self.radius = radius
        
import turtle
import random

class Circle:
    circles = []
    colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "white", "cyan", "magenta"]

    def __init__(self, radius = None, diameter = None):
        if radius is not None and diameter is not None:
            raise ValueError("Cannot have both radius and diameter")
    
        if radius is None :
            self.radius = diameter / 2
            self.diameter = diameter
        elif diameter is None :
            self.radius = radius
            self.diameter = radius * 2
        else :
            raise ValueError("Circle must have radius or diameter")  
        Circle.circles.append(self) 

    def area(self) -> int :
        return self.radius ** 2 * 3.14

    def __str__(self) :
        return f"Circle with radius: {self.radius} and diameter: {self.diameter}"  

    def __add__(self, other_circle) :
        return f"Two circles together: radiuses - {self.radius + other_circle.radius}, diameters - {self.diameter + other_circle.diameter}"

    def __gt__(self, other_circle) :
        if self.radius > other_circle.radius:
            return f"Circle with radius {self.radius} is bigger than circle with radius {other_circle.radius}"
        else:
            return f"Circle with radius {other_circle.radius} is bigger than circle with radius {self.radius}"      

    def __eq__(self, other_circle) -> str:
        if self.radius == other_circle.radius:
            return "Circles is equals"

    def draw():
        scr = turtle.getscreen()
        t = turtle.Turtle()
        t.speed(3)
        turtle.bgcolor("black")
        for circle_r in Circle.circles:
            t.goto(random.randrange(-200, 200), random.randrange(-200, 200))
            t.pendown()
            t.pencolor(random.choice(Circle.colors))
            t.pensize(random.randrange(1, 15))
            t.circle(circle_r.radius) 
            t.penup() 

circle1 = Circle(radius = 20)
circle2 = Circle(diameter = 30)
circle3 = Circle(radius = 40)
circle4 = Circle(diameter = 80)
circle1 = Circle(radius = 20)
circle2 = Circle(diameter = 52)
circle3 = Circle(radius = 89)
circle4 = Circle(diameter = 80)
circle1 = Circle(radius = 10)
circle2 = Circle(diameter = 10)
circle3 = Circle(radius = 12)
circle4 = Circle(diameter = 25)
circle1 = Circle(radius = 30)
circle2 = Circle(diameter = 66)
circle3 = Circle(radius = 45)
circle4 = Circle(diameter = 100)

print(circle1.area())
print(circle2.__str__())
print(circle3 + circle4)
print(circle1 > circle3)
print(circle3 == circle4)

Circle.draw()

        
import turtle
import os
from PIL import Image

cwd = os.getcwd()

""" CLASSES """
class Point(object):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        super().__init__(x1, y1, width, height, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()


class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)


class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


""" EXPORT IMAGE """
def export_image(image_name):
    """Creates an image of the current turtle screen and adds them to an Images folder"""
    # Figure out how to save certain frames to a folder of images, so you don't have to ss each one
    if not os.path.exists(cwd + '/images/'):
        os.mkdir(cwd + '/images/')

    if not os.path.exists(cwd + '/eps_files/'):
        os.mkdir(cwd + '/eps_files/')

    filename = 'lab13_img_' + str(image_name)
    screen = turtle.getscreen()
    screen.getcanvas().postscript(file=f'{cwd}/eps_files/{filename}.eps')

    with Image.open(f'{cwd}/eps_files/{filename}.eps') as image:
        image.convert()
        image.save(f'{cwd}/Images/{filename + ".jpg"}')

    os.remove(f'{cwd}/eps_files/{filename + ".eps"}')
    turtle.clear()


""" MAIN PROGRAM """
# Turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
export_image('Turtle')

# Turtle Filled
turtle.fillcolor('red')
turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()
export_image('TurtleFilled')

# Point
p = Point(-100, 100, "blue")
p.draw()
export_image('Point')

# Box
b = Box(-100, 100, 50, 20, 'blue')
b.draw()
export_image('Box')

# BoxFilled
b = BoxFilled(1, 2, 100, 200, 'red', 'blue')
b.draw()
export_image('BoxFilled')

# Circle
c = Circle(-100, 100, 50, 'blue')
c.draw()
export_image('Circle')

# Circle Filled
c = CircleFilled(1, 2, 100, 'red', 'blue')
c.draw()
export_image('CircleFilled')

if os.path.exists(cwd + '/eps_files/'):
    os.rmdir(cwd + '/eps_files/')
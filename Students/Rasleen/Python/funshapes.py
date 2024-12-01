import turtle

t = turtle.Turtle()
t.speed(2)  # Set drawing speed

# Function to draw an equilateral triangle
def draw_triangle(side_length, color):
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(width, height, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a hexagon
def draw_hexagon(side_length, color):
    t.color(color)
    t.begin_fill()
    for _ in range(6):
        t.forward(side_length)
        t.left(60)
    t.end_fill()

# Draw the shapes
t.penup()
t.goto(-100, 0)# Position for triangle
t.pendown()
draw_triangle(100, "red")

t.penup()
t.goto(100, 0)# Position for rectangle
t.pendown()
draw_rectangle(120, 60, "green")

t.penup()
t.goto(0, -150)# Position for hexagon
t.pendown()
draw_hexagon(80, "blue")


t.hideturtle()
turtle.done()
import turtle as trtl

# --- Setup ---
screen = trtl.Screen()
screen.trtl("Custom Duck Project")

# --- Brainstorming/Design ---
# Possible duck colors stored in a list
colors = ["yellow", "green", "blue", "pink"]

# User Input (Interactivity)
print("Choose your duck color from:", colors)
duck_color = input("Enter a color: ")
if duck_color not in colors:
    duck_color = "yellow"   # default if invalid

message = input("What should the duck say? ")

# --- Create custom duck turtle ---
duck = trtl.trtl()
duck.speed(10)
duck.color(duck_color)
duck.pensize(3)

# --- Functions to draw shapes ---
def draw_circle(t, radius):
    """Draws a circle using iteration"""
    for i in range(36):   # iteration example
        t.forward(radius)
        t.left(10)

# --- Draw the duck ---
# Body
duck.penup()
duck.goto(-50, -50)
duck.pendown()
draw_circle(duck, 10)   # big circle for body

# Head
duck.penup()
duck.goto(50, 0)
duck.pendown()
draw_circle(duck, 5)

# Beak
duck.penup()
duck.goto(95, 15)
duck.pendown()
duck.color("orange")
duck.begin_fill()
for i in range(3):       # triangle beak with iteration
    duck.forward(20)
    duck.left(120)
duck.end_fill()

# Return duck color to chosen one
duck.color(duck_color)

# --- Speech Bubble ---
pen = trtl.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-50, 100)
pen.write(message, font=("Arial", 16, "normal"))

# Keep window open until closed
wn = trtl.Screen()
wn.mainloop()

import turtle as trtl
import random as rand

Screen = trtl.Screen()
Screen.bgcolor("darkgreen")

pen = trtl.Turtle()
pen.hideturtle()
pen.speed(10)
pen.color("white")

name = Screen.textinput("Would you like to play?")


for x, label in [(start_x, "START"), (finish_x, "FINISH")]:
    pen.penup()
    pen.goto(x, -120)
    pen.setheading(90)
    pen.pendown()
    pen.forward(240)
    pen.penup()
    pen.goto(x, 130)
    pen.write(label, align="center", font=("Arial", 12, "bold"))

deck = ((2,))

screen.mainloop()
#TODO
#TODO
#Green Felt UI
# Deck of cards
#
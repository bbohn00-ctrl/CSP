import turtle as trtl
import random as rand

#Setup screen
Screen = trtl.Screen()
Screen.bgcolor("darkgreen")

pen = trtl.Turtle()
pen.hideturtle()
pen.speed(0)

# Better way to make the deck without tedious uploads
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]* 4

name = Screen.textinput("Would you like to play?")
Credits = 5000
#Cards slot cordinates
player_start_X = -150
player_start_Y = -150
dealer_start_X = -150
dealer_start_Y = 150

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
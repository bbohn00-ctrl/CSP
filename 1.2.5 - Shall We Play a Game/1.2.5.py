import turtle as trtl
import random as rand

#Setup screen
Screen = trtl.Screen()
Screen.bgcolor("darkgreen")
pen = trtl.Turtle()
pen.hideturtle()
pen.color("white")
pen.speed(0)

#Deck Setup
# Better way to make the deck without tedious uploads using a 52 card deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]* 4

def deal_cards():
    return rand.choice(deck)

def calculate_hand(hand):
    total = sum(hand)
    aces = hand.count(11)

#Table UI/ Card Slots
def draw_slots(x, y, label, cards, total, hide_dealer=False):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.setheading(0)
    for _ in range(2):
        pen.forward(120)
        pen.left(90)
        pen.forward(160)
        pen.left(90)
    pen.penup()



name = Screen.textinput("Would you like to play?")
Credits = 5000


deck = ((2,))

screen.mainloop()
#TODO
#TODO
#Green Felt UI
# Deck of cards
#
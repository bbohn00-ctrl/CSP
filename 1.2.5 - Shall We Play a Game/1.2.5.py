import turtle as trtl
import random as rand

#Setup screen
Screen = trtl.Screen()
Screen.bgcolor("darkgreen")
pen = trtl.Turtle()
pen.hideturtle()
pen.color("white")
pen.speed(0)


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

#Card Score Label 
    pen.goto(x + 60, y + 140)
    pen.write(label, align= "middle", font=("Arial", 14, "bold"))

#Hiding the dealers hole card logic
    if hide_dealer:
        display_cards = [cards[0], "?"]
        total_text = "?"
    else:
        display_cards = cards
        total_text = str(total)

#Showing the hand
    pen.goto(x + 60, y + 60)
    pen.write(f"Cards: {display_cards}", align="center", font=("Arial", 12, "normal"))

    # All cards fliped/drawn
    pen.goto(x + 60, y + 20)
    pen.write(f"Total: {total_text}", align="center", font=("Arial", 20, "bold"))


#Deck Setup
# Better way to make the deck without tedious uploads using a 52 card deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]* 4

def deal_cards():
    return rand.choice(deck)

def calculate_hand(hand):
    total = sum(hand)
    aces = hand.count(11)

name = Screen.textinput("Would you like to play?")
Credits = 5000


deck = ((2,))


#TODO
#TODO
#Green Felt UI
# Deck of cards
#
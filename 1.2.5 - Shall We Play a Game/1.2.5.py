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



# Deck Setup/ Better way to make the deck without tedious uploads using a 52 card deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]* 4


#Calcualting the hands
def calc(hand):
    total = sum(hand)
    aces = hand.count(11)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

#Game Variables
Chips = 5000
playing = True

# Main loop needed for BJ
while playing:
    bet = Screen.numinput("Pick a Bet Amount", f"You have {Chips}. Enter Your Bet:", minval=500, maxval=Chips)
    
    player = [rand.choice(deck), rand.choice(deck)]
    dealer = [rand.choice(deck), rand.choice(deck)]

    pen.clear()
    draw_slots(-150, 0, "Player", player, calc(player))
    draw_slots(-150, 0, "Dealer", dealer, calc(dealer), hide_dealer=True)

#Player Goes
    while calc(player) < 21:
        playersmove = Screen.textinput("Your turn", "Enter 'h' or 's':").lower()
        if playersmove == "hit":
            player.append(rand.choice(deck))
            pen.clear()
            draw_slots(-150, 0, "Player", player, calc(player))
            draw_slots(-150, 0, "Dealer", player, calc(player), hide_dealer=True)
        else:
            break

    playerscore_total = calc(player)
    dealerscore_total = calc(dealer)

#Dealer Goes
    while dealerscore_total < 17:
        dealer.append(rand.choice(deck))
        dealerscore_total = calc(dealer)

#Show Results of the Hand
    pen.clear()
    draw_slots(-150, 0, "Player", player, playerscore_total)
    draw_slots(-150, 0, "Dealer", dealer, dealerscore_total)

    if playerscore_total > 21:
        result = "Bust! Dealer Wins"
        Chips -= bet
    elif dealerscore_total > 21 or playerscore_total > dealerscore_total:
        result = "You Win!"
        Chips += bet
    elif playerscore_total < dealerscore_total:
        result = "Dealer Wins"
        Chips -= bet
    else:
        result = "Tie"

    pen.goto(0. -180)
    pen.write(f"{result}\nChips: {Chips}", align="center", font=("Arial", 16, "bold"))
        







#TODO
#TODO
#Green Felt UI
# Deck of cards
#
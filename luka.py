# Luka Jeremic Python Project 91896
import random

u = 0
sumTotal = 0
winnings = 0
balance = 1000
gameRunning = True
bet = 0
e = 0


# Print Card Layout onto Terminal
def card(x, y):
    # If the card number is 10, the spacing is changed to what is shown below.
    if x == '10':
        print("_______________")
        print(f"|{x}           |")
        print("|             |")
        print("|             |")
        print(f"|      {y}      |")
        print("|             |")
        print("|             |")
        print(f"|          {x} |")
        print("---------------")
    else:
        # All other numbers are 1 space large, therefore the spacing is changed
        # to what is shown below.
        print("_______________")
        print(f"| {x}           |")
        print("|             |")
        print("|             |")
        print(f"|      {y}      |")
        print("|             |")
        print("|             |")
        print(f"|           {x} |")
        print("---------------")


# Ask Player to Play Again / Re-deal
def replay():
    global gameRunning, balance, z, bet, sumTotal, b
    q = 0
    balance = balance + winnings
    print('\n')
    print("Now your balance is: $", balance)
    # Resets all Game loops for a possible new deal.
    b += 2
    sumTotal = 0
    z += 2
    bet = 0
    # Enters a loop so that the user is repeatedly asked, until a valid input
    # is entered.
    while q < 1:
        p = input('Would you like a ReDeal? Yes/No').lower()
        if p == 'no':
            gameRunning = False
            q += 2
        elif p == 'yes':
            q += 2
        else:
            print('\n')
            print("Please answer Yes or No Only (Yes / No)")


# Convert Ace to a 1 instead of 11 (Removes 10 from Card Total)
# (ONLY FOR PLAYER)
def ace():
    global sumTotal
    sumTotal -= 10
    print('\n')
    print("As you have busted, one of your Ace(s) has been converted to 1")
    print("Now Current Card Total:", sumTotal)
    print('\n')
    deck.remove('A')


# Convert Ace to a 1 instead of 11 (Removes 10 from Card total)
# (ONLY FOR DEALER)
def ace2():
    global sumTotal2
    sumTotal2 -= 10
    print('\n')
    print("As dealer has busted, one of their Ace(s) has been converted to 1")
    print("Now Current Card Total:", sumTotal2)
    print('\n')
    deck2.remove('A')


# Collect Random Card Values and Set Numerical Values - (ONLY FOR PLAYER)
def player():
    global sumTotal, deck
    x = random.choice(value)
    y = random.choice(suit)
    card(x, y)
    deck.append(x)
    number = value.index(x) + 1
    if number > 10:
        number = 10
    if sumTotal <= 21 and x == 'A':
        number = 11
    if sumTotal > 21 and x == 'A':
        number = 1
    sumTotal += number


# Collect Random Card Values and Set Numerical Values - (ONLY FOR DEALER)
def dealer():
    global sumTotal2, deck2
    x = random.choice(value)
    y = random.choice(suit)
    card(x, y)
    deck2.append(x)
    number = value.index(x) + 1
    if number > 10:
        number = 10
    if sumTotal2 <= 21 and x == 'A':
        number = 11
    if sumTotal2 > 21 and x == 'A':
        number = 1
    sumTotal2 += number


# Ensures the bet made by user is a Number. This prevents breaking the code
# through entering 'hundred' instead of '100'
def numb():
    global bet, e
    while True:
        try:
            bet = int(input("How much would you like to bet (Minimum of 100)\
" + name + "?"))
            break
        except ValueError as e:
            print("Please Enter Numbers Only.")
            print('\n')
            print("Current Balance: $", balance)


# Initial Instructions/Help
print('''BLACKJACK TERMS:
Hit-Pick up a Card
Stand-Do not pick up a card
BLACKJACK-21 Total

If you get BLACKJACK, You instantly win!
''')
# Determine User's Name and Use it Throughout Their Playtime.

name = input("What is Your Name?")
# Ensures Users True Name Through Not Being Numbers, Repeatedly asks until
# Numbers are not Present Due to the loop.
while u < 1:
    if name.isdigit():
        print("Please enter name (Characters Only)")
        print('\n')
        name = input("What is Your Name?")
    else:
        print("Hello", name)
        print('\n')
        u += 2
# Sets Game Variables to Starting values Declaring Game Start.

while gameRunning:
    # Resets Loops Back to Initial so They Can Be Looped Once Again.
    b = 0
    j = 0
    z = 0
    k = 0
    # Balance Check. If any of these are true, the player is not allowed to
    # continue playing and the Game loop breaks.
    if balance < 100:
        print("You can no longer bet.")
        break
    elif balance > 9999:
        print("Congratulations, You have reached the maximum winnings!")
        break
    else:
        pass
    # Displays User their present balance and explains bet for full clarity.
    print('\n')
    print("Current Balance: $", balance)
    print("If you win, you get 2x your bet. If you lose, you lose your bet.")
    # Ask user for a bet. Enters a while loop and continues to ask until a
    # number bet is presented.
    numb()
    # Bet Check. If the bet is deemed not legal(These possible outcomes), the
    # user is re-asked for a bet. If the bet is legal, the loop breaks and the
    # game loop continues.
    while k < 1:
        if bet < 100:
            print("You must bet over $100")
            print('\n')
            print("Current Balance: $", balance)
            numb()
        elif bet > balance:
            print('\n')
            print("You can not afford that bet")
            numb()
        else:
            k += 2
    # Declaring Bet has been Accepted and Been Taken from the Users Balance
    print('\n')
    print("Current bet: $", bet)
    print("$", bet, "Has been taken from your balance")
    balance = balance - bet
    print("Balance is now: $", balance)
    # Sets Card Values to Initial Starts.
    sumTotal2 = 0
    deck = []
    deck2 = []
    value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suit = ["♥", "♦", "♣", "♠"]
    # Provides User With Their 2 Initial Cards
    for i in range(2):
        player()
    print("Your Current Card Total:", sumTotal)
    # Checks the Users two Initial Cards Numerical values. If Either are
    # substantial, action takes place. If not, the game loop continues.
    if sumTotal == 21:
        print("YOU HAVE GOT BLACKJACK, You automatically win")
        winnings = bet * 2
        print("You won", winnings)
        replay()
    elif sumTotal > 21:
        ace()
    # Sends user into a loop of choice. Ensures the user only enters 'H' or
    # 'S' and continuously gives the choice, when correct
    # (e.g Card Total is still in play)
    while z < 1:
        choice = input("Will you H (for Hit) or S (for Stand)").lower()
        if choice == 'h':
            # Provides New Card and Added to Card Total using player define
            player()
            print("New Card Total:", sumTotal)
            # Checks for Ace when player busts, Adjusts accordingly
            while sumTotal > 21:
                if 'A' in deck:
                    ace()
                else:
                    print("You busted as your total is above 21. You lose.")
                    print("You lost your:", bet)
                    winnings = 0
                    replay()
            # Checks if the player has obtained Blackjack after gaining another
            # card. If so, acts accordingly. If not, pass
            if sumTotal == 21:
                print("BLACKJACK BLACKJACK BLACKJACK, You automatically win!")
                winnings = bet * 2
                print("You won", winnings)
                replay()
        elif choice == 's':
            # Begins Dealers (Computer) Card Total / Deck Through providing its
            # initial two cards.
            for i in range(2):
                dealer()
            print("Dealers current card total:", sumTotal2)
            # Checks if Dealer has got Blackjack. If so, acts accordingly,
            # if not pass.
            if sumTotal2 == 21:
                print("Dealer has got BLACKJACK, you automatically lose.")
                print("You lost your:", bet)
                winnings = 0
                replay()
            # Checks if Dealer has busted. In this case, the only possible way
            # to bust is 22 with two cards (2 Aces) meaning in this scenario,
            # Ace will always be present. No need to adjust for a possible
            # no-ace bust. This occurs earlier for the player as well.
            elif sumTotal2 > 21:
                ace2()
            # Sends dealer in a loop of Conditions. This forces card pick-ups
            # until their card total is > 17.
            while b < 1:
                # Checks if dealers card total is below 17. If so, dealer is
                # forced a card onto their card total.
                if sumTotal2 < 17:
                    dealer()
                    print("Dealer hits for a new total of:", sumTotal2)
                # Checks if dealer contains an Ace after busting.
                # Acts accordingly.
                elif sumTotal2 > 21:
                    if 'A' in deck2:
                        ace2()
                    else:
                        print("Dealer busted as their total is > 21, you win!")
                        winnings = bet * 2
                        print("You won", winnings)
                        replay()
                # Checks if dealer has obtained Blackjack. If not, simply
                # passes as function is not satisfied.
                elif sumTotal2 == 21:
                    print("Dealer has got BLACKJACK, you lose automatically.")
                    print("You lost your:", bet)
                    replay()
                    winnings = 0
                else:
                    # Checks if players card total is zero. If it is zero,
                    # there has either been an error or the players deck has
                    # been reset. Either case, the loop breaks and restarts as
                    # it is not a legitimate game.
                    if sumTotal == 0:
                        break
                    # If no previous conditions are satisfied, the card totals
                    # are compared for a final winner. The card totals are
                    # compared until a satisfied function and act accordingly.
                    elif sumTotal2 > sumTotal:
                        print("DEALER WINS WITH", sumTotal2, "TO", sumTotal)
                        print("You lost your:", bet)
                        winnings = 0
                        replay()
                    elif sumTotal > sumTotal2:
                        print("PLAYER WINS WITH", sumTotal, "TO", sumTotal2)
                        winnings = bet * 2
                        print("You won", winnings)
                        replay()
                    else:
                        print("IT'S A TIE OF", sumTotal, "FOR DEALER & PLAYER")
                        print("YOUR", bet, "HAS BEEN RETURNED.")
                        winnings = bet
                        replay()
        else:
            # If the player does not enter a correct choice, this will be
            # presented and looped back to the question.
            print('\n')
            print("Please enter either H (for Hit) or S (for Stand)")
# Final statements of game overview. This only occurs when the game loop has
# been broken meaning a stoppage in Blackjack
print('\n')
print("You're Ending Balance After Starting with $1000, = $", balance)
print("THANKS FOR PLAYING!")

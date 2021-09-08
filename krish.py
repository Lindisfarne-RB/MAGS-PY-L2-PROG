#!/usr/bin/python
# -*- coding: utf-8 -*-
# Krish Patel 12GRG
# Functions
# List of list of strings AND List of ints, and its manipulation
# String manipulation
# File management
# External libaries, GUI
# Advanced clean code
import random # random
import tkinter as tk  # gui
from functools import partial # to use cards as buttons seperately
# This is a list of all possible cards so the program can randomly choose one when it needs to.
deckOfCards = ['0.r', '1.r', '1.r', '2.r', '2.r', '3.r', '3.r', '4.r', '4.r', '5.r', '5.r', '6.r', '6.r', '7.r', '7.r', '8.r', '8.r', '9.r', '9.r', 'S.r', 'S.r', 'R.r', 'R.r', '+2.r', '+2.r', '+4.w', 'C.w', '0.y', '1.y', '1.y', '2.y', '2.y', '3.y', '3.y', '4.y', '4.y', '5.y', '5.y', '6.y', '6.y', '7.y', '7.y', '8.y', '8.y', '9.y', '9.y', 'S.y', 'S.y', 'R.y', 'R.y', '+2.y', '+2.y', '+4.w',
               'C.w', '0.g', '1.g', '1.g', '2.g', '2.g', '3.g', '3.g', '4.g', '4.g', '5.g', '5.g', '6.g', '6.g', '7.g', '7.g', '8.g', '8.g', '9.g', '9.g', 'S.g', 'S.g', 'R.g', 'R.g', '+2.g', '+2.g', '+4.w', 'C.w', '0.b', '1.b', '1.b', '2.b', '2.b', '3.b', '3.b', '4.b', '4.b', '5.b', '5.b', '6.b', '6.b', '7.b', '7.b', '8.b', '8.b', '9.b', '9.b', 'S.b', 'S.b', 'R.b', 'R.b', '+2.b', '+2.b', '+4.w', 'C.w']

while True:  # Loop while answer is a int then continue
    try:
        noOfPlayers = int(input('How many players?\n'))
        if noOfPlayers > 1:
            break
    except ValueError:
        print('Please type a number')

# init
playerDeck = []
change = 0
direction = 1
turns = []
lastCard = random.choice(deckOfCards)  # selecting the starting card at random

for a in range(noOfPlayers):  # Loop for how many players there are
    playerDeck.append(['P.w'])  # start with the pickup
    for b in range(7):

        # give them 7 random cards

        playerDeck[a].append(random.choice(deckOfCards))

root = tk.Tk()  # Root of window def
root.title('Uno - Krish Patel')  # Adding a title
root.geometry('500x640')

playerTurnLblStr = tk.StringVar()
playerTurnLbl = tk.Label(root, textvariable=playerTurnLblStr,
                         width=10).grid(row=0, column=1, columnspan=5)  # creating label for whos turn it is


def waitForTurn(playerReady):

    # Changing string to different players turns

    playerTurnLblStr.set('Player ' + str(curntPlayerTurn + 1)
                         + "'s turn")
    isReady = tk.IntVar()

    # Button before showing cards so device can to pass to the correct player irl

    readybtn = tk.Button(root, text='Ready?', command=lambda:
                         isReady.set(1))
    readybtn.grid(row=1, column=3, columnspan=10)

    # pausing code at this point and waiting till button is pressed

    readybtn.wait_variable(isReady)
    readybtn.destroy()  # remove ready button

    # player turn starts

    Turn(playerReady)


colorPicked = tk.IntVar()


def colorChange():
    global colorPicked, change
    change = tk.Toplevel()  # Root of window def
    change.title('Color change window')  # Adding a title

    def colorWasPicked(x):  # Function accesbile by button
        # sets global var of color chosen so it can be used after window closes.
        colorPicked.set(x)
        print(x, 'was selected')
        change.quit()  # quits out of loop

    redImg = tk.PhotoImage(file='img/C.r.png')  # img of red color sqaure
    red = tk.Button(change, image=redImg, command=lambda z=0:
                    colorWasPicked(z))  # change to red
    red.grid(row=0, column=0)

    blueImg = tk.PhotoImage(file='img/C.b.png')  # img of blue color sqaure
    blue = tk.Button(change, image=blueImg, command=lambda z=1:
                     colorWasPicked(z))  # change to blue
    blue.grid(row=0, column=1)

    greenImg = tk.PhotoImage(file='img/C.g.png')  # img of green color sqaure
    green = tk.Button(change, image=greenImg, command=lambda z=2:
                      colorWasPicked(z))  # change to green
    green.grid(row=1, column=0)

    yellowImg = tk.PhotoImage(file='img/C.y.png')  # img of yellow color sqaure
    yellow = tk.Button(change, image=yellowImg, command=lambda z=3:
                       colorWasPicked(z))  # change to yellow
    yellow.grid(row=1, column=1)

    change.mainloop()  # loops the screen till button is presseed


def pickUpCards(player, numOfCards):
    global playerDeck
    for j in range(numOfCards):

        # gets a number to index which player and makes them pick up x times

        playerDeck[player].append(random.choice(deckOfCards))


def reverseTurn():
    global direction
    direction = direction * -1
    turns.reverse()
    print(turns, "is the turn order")


def skipTurn(curntTurn):
    try:
        del turns[curntTurn + 1 * direction]
    except IndexError:
        print('skip last player so first')
        if direction == 1:
            del turns[0]
        else:
            del turns[-1]


def Actions(CardInfo):  # After selected card is put down, this function determines what to do next
    global lastCard  # to make last card put down to changeable
    print('player', CardInfo[0])
    print('card', CardInfo[1])
    cardSplit = CardInfo[1].split('.')
    if CardInfo[1] == 'C.w':  # color change card
        colorChange()  # Open color Changing screen
        change.destroy()  # exit it after color chosen
        if colorPicked.get() == 0:  # Red color set last card as red
            print('red last card')
            lastCard = 'C.r'
        elif colorPicked.get() == 1:  # blue color set last card as blue
            print('blue last card')
            lastCard = 'C.b'
        elif colorPicked.get() == 2:  # green color set last card as green
            print('green last card')
            lastCard = 'C.g'
        elif colorPicked.get() == 3:  # yellow color set last card as yellow
            print('yellow last card')
            lastCard = 'C.y'
        del playerDeck[CardInfo[0]][playerDeck[CardInfo[0]].index(
            CardInfo[1])]  # delete the card placed from player hand
        root.quit()  # move to next players turn
    elif CardInfo[1] == '+4.w':
        print('player ', CardInfo[0] + 1, 'pick up 4')
        try:
            # try giving 4 to next player, if next player doesnt exist loop to first
            pickUpCards(CardInfo[0] + 1 * direction, 4)
        except IndexError:  # error handling
            print('last player so first')
            if direction == 1:
                pickUpCards(0, 4)  # normal direction
            else:
                pickUpCards(-1, 4)  # reversed direction
        colorChange()  # color change card
        change.destroy()  # Open color Changing screen
        if colorPicked.get() == 0:  # Red color set last card as red
            print('red last card')
            lastCard = 'C.r'
        elif colorPicked.get() == 1:  # blue color set last card as blue
            print('blue last card')
            lastCard = 'C.b'
        elif colorPicked.get() == 2:  # green color set last card as green
            print('green last card')
            lastCard = 'C.g'
        elif colorPicked.get() == 3:  # yellow color set last card as yellow
            print('yellow last card')
            lastCard = 'C.y'
        del playerDeck[CardInfo[0]][playerDeck[CardInfo[0]].index(
            CardInfo[1])]  # delete teh card from teh player hand
        root.quit()  # move to next players turn
    elif CardInfo[1] == 'P.w':
        # if the pick up card was click, make the player pickup 1 card
        pickUpCards(CardInfo[0], 1)
        root.quit()  # move to next players turn
    # If the color of placed and last card down is same,
    elif cardSplit[1] == lastCard.split('.')[1]:
        if cardSplit[0] == 'R':
            reverseTurn()  # reverse if reverse
        elif cardSplit[0] == '+2':  # pickup 2
            try:
                # try picking 2 cards up to next player
                pickUpCards(CardInfo[0] + 1 * direction, 2)
                print('pick up 2 cards')
            except IndexError:  # error handling
                print('last player so first')
                if direction == 1:
                    pickUpCards(0, 2)  # normal
                else:
                    pickUpCards(-1, 2)  # reversed
        elif cardSplit[0] == 'S':
            skipTurn(CardInfo[0])  # skip turn of next player
        print('matched color')
        root.quit()  # move to next players turn
        lastCard = CardInfo[1]  # set last card as one put down
        del playerDeck[CardInfo[0]][playerDeck[CardInfo[0]].index(
            CardInfo[1])]  # delete the card placed from player hand
        root.quit()  # move to next players turn
    elif cardSplit[0] == lastCard.split('.')[0]:
        print('number match')
        lastCard = CardInfo[1]

        del playerDeck[CardInfo[0]][playerDeck[CardInfo[0]].index(
            CardInfo[1])]  # delete the card placed from player hand
        root.quit()  # move to next players turn


def Turn(player):
    print(player)
    lastCardImg = tk.PhotoImage(
        file='img/' + str(lastCard) + '.png')  # img of last card
    pickupBtn = tk.Button(root, image=lastCardImg)  # button for last card
    pickupBtn.grid(row=0, column=0)

    cardImgs = list(tk.PhotoImage(file='img/' + str(thisCard) + '.png')
                    for thisCard in player)  # list of images for all cards the player has

    imgNum = 0  # def value to use in loop
    yCord = 2

    for thisCard in player:  # loop through each card
        thisBtn = tk.Button(root, image=cardImgs[imgNum],
                            command=lambda CardInfo=[playerDeck.index(player),
                            str(thisCard)]: Actions(CardInfo))  # create a button for each card
        # when pressed it will send a list of the player turn and what card

        # show 4 cards side my side then go under

        thisBtn.grid(row=yCord, column=imgNum % 4)

        if imgNum % 4 >= 3:  # Once it reachs 4 cards sideways
            yCord += 1  # move underneath

        imgNum += 1  # goto next pic
    root.mainloop()  # loop through till broken (valid card placed)


for h in range(noOfPlayers):  # starting order
    turns.append(h)
gameRunning = True
while gameRunning:  # while game not won
    for curntPlayerTurn in turns:
        try:
            waitForTurn(playerDeck[curntPlayerTurn])  # start players turn
            if len(playerDeck[curntPlayerTurn]) <= 1:

                print('\n\n\n\n\n__________________________________________')
                print('player', curntPlayerTurn + 1, 'won!')  # say who won
                gameRunning = False
                root.destroy()  # close game
        except IndexError:  # error handling
            print('Skipping turn')
    turns = []
    if direction == 1:
        for h in range(noOfPlayers):  # make order
            turns.append(h)
    else:
        for h in range(noOfPlayers-1, -1, -1):  # make order backwards if reversed
            turns.append(h)
    print(turns, "is the turn order")
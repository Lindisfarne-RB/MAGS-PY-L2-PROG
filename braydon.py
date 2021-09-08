# Braydon Faauuga

# I used dictionaires to store the date that made it easier

# I then used Def for storing the part where I print the questions and choices

# I used the While True and Not Is to ensure
# that the user uses the correct keys to play my quiz

# I wrapped the whole code in another While True
# to create a loop that acts as a 'play again' feature

# I created a score counter that tracks the amount of right answers

# I used features like .lower() and .capitalize()
# that helped ensure that the keys are right

# I had to keep the part of the code where it tells you
# if you got it correct or not out of
# the dictionary cause if it is kept in
# the score counter doesn't read it for some reason

# Question one dictionary
anime1 = {
    "id": 0,
    "question": "what best fits the description? :"
    "a girl transform into a cat for "
    "a boy's attention ",
    "a": "Whisker Away",
    "b": "Cat Love",
    "c": "Catnip",
    "d": "Love is like milk",
    "answer": "a",
}

# Def for printing the question 1
def question1():
    print(anime1["question"])
    print(" ")
    print(
        "A:",
        anime1["a"],
    )
    print(
        "B:",
        anime1["b"],
    )
    print(
        "C:",
        anime1["c"],
    )
    print("D:", anime1["d"])


# Question 2 dictionary
classic1 = {
    "id": 0,
    "question": "What is the name of the man who plays the Terminator?",
    "a": "Ronald Cerrone",
    "b": "Mark Wahlberg",
    "c": "Harvey Keitel",
    "d": "Arnold Schwarzenegger",
    "answer": "d",
}

# Def for question 2
def question2():

    print(classic1["question"])
    print(" ")
    print(
        "A:",
        classic1["a"],
    )
    print(
        "B:",
        classic1["b"],
    )
    print(
        "C:",
        classic1["c"],
    )
    print("D:", classic1["d"])


# Question 3 dictionary
normal1 = {
    "id": 0,
    "question": "What is the name of the the voice actor who plays Ted?",
    "a": "Giovanni Ribsi",
    "b": "Patrick Walberg",
    "c": "Joel McHale",
    "d": "Seth Macfarlane",
    "answer": "d",
}

# Def for question 3
def question3():

    print(normal1["question"])
    print(" ")
    print(
        "A:",
        normal1["a"],
    )
    print(
        "B:",
        normal1["b"],
    )
    print(
        "C:",
        normal1["c"],
    )
    print("D:", normal1["d"])


# Question 4 dictionary
classic2 = {
    "id": 0,
    "question": "When did Rambo first released ",
    "a": "1980",
    "b": "1981",
    "c": "1982",
    "d": "1983",
    "answer": "c",
}

# Def for Question 4
def question4():

    print(classic2["question"])
    print(" ")
    print(
        "A:",
        classic2["a"],
    )
    print(
        "B:",
        classic2["b"],
    )
    print(
        "C:",
        classic2["c"],
    )
    print("D:", classic2["d"])


# Question 5 Dictionary
classic3 = {
    "id": 0,
    "question": "What fits this description ' A boy turns into a robot'",
    "a": "The Mechanic",
    "b": "Tinkering",
    "c": "Nuts and Bolts",
    "d": "Astro Boy",
    "answer": "d",
}

# Def for Question 5
def question5():  # Question function

    print(classic3["question"])
    print(" ")
    print(
        "A:",
        classic3["a"],
    )
    print(
        "B:",
        classic3["b"],
    )
    print(
        "C:",
        classic3["c"],
    )
    print("D:", classic3["d"])


# Question 6 Dictionary
classic4 = {
    "id": 0,
    "question": " finish this : The fast and the _____",
    "a": "Furious",
    "b": "flamboyant",
    "c": "Furrious",
    "d": "Fat",
    "answer": "a",
}

# Def for Question 6
def question6():

    print(classic4["question"])
    print(" ")
    print(
        "A:",
        classic4["a"],
    )
    print(
        "B:",
        classic4["b"],
    )
    print(
        "C:",
        classic4["c"],
    )
    print("D:", classic4["d"])


# Question 7 Dictionary
classic5 = {
    "id": 0,
    "question": "Finish this 'Beauty and the _____",
    "a": "Bomb",
    "b": "Beast",
    "c": "Bee",
    "d": "Bread",
    "answer": "b",
}

# Def for Question 7
def question7():

    print(classic5["question"])
    print(" ")
    print(
        "A:",
        classic5["a"],
    )
    print(
        "B:",
        classic5["b"],
    )
    print(
        "C:",
        classic5["c"],
    )
    print("D:", classic5["d"])


# Question 8 Dictionary
normal2 = {
    "id": 0,
    "question": "In the movie 'Coco' can you finish this : El Poco ____",
    "a": "Loco",
    "b": "Doko",
    "c": "Senor",
    "d": "Senorita",
    "answer": "a",
}

# The Def for Question 8
def question8():

    print(normal2["question"])
    print(" ")
    print(
        "A:",
        normal2["a"],
    )
    print(
        "B:",
        normal2["b"],
    )
    print(
        "C:",
        normal2["c"],
    )
    print("D:", normal2["d"])


# Question 9 Dictionary
normal3 = {
    "id": 0,
    "question": "Finis this : ____ and Monsters",
    "a": "Guns",
    "b": "Werewovles",
    "c": "Ghouls",
    "d": "Love",
    "answer": "d",
}

# Def for Question 9
def question9():

    print(normal3["question"])
    print(" ")
    print(
        "A:",
        normal3["a"],
    )
    print(
        "B:",
        normal3["b"],
    )
    print(
        "C:",
        normal3["c"],
    )
    print("D:", normal3["d"])


# Question 10 dictionary
normal4 = {
    "id": 0,
    "question": "finish this : The _____ squad",
    "a": "loser",
    "b": "sucide",
    "c": "Ghouls",
    "d": "Love",
    "answer": "b",
}

# Def for question 10
def question10():

    print(normal4["question"])
    print(" ")
    print(
        "A:",
        normal4["a"],
    )
    print(
        "B:",
        normal4["b"],
    )
    print(
        "C:",
        normal4["c"],
    )
    print("D:", normal4["d"])


# Restart Code

restart = {"a": "yes", "b": "no"}


# The Quiz

score = 0
run = True
while run is True:
    print("")
    print("Welcome to the quiz!")
    name = input("what is your name?\n")
    name = name.capitalize()
    print("Please try your best", name)
    print(" ")
    while True:
        question1()

        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("sorry that is an invalid answer, please try again")
            print("")
            continue
        else:
            break
    if guess == anime1["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question2()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("sorry that is an invalid answer, please try again")
            print("")
            continue
        else:
            break
    if guess == classic1["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print(" ")
        print("your score is", score)
        print("")
    while True:
        question3()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == normal1["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print(" ")
        print("your score is", score)
    while True:
        question4()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == classic2["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question5()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == classic3["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question6()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == classic4["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question7()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == classic5["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question8()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == normal2["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question9()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == normal3["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    while True:
        question10()
        guess = input("Your guess: ")
        guess = guess.lower()
        if guess not in ("a", "b", "c", "d"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if guess == normal4["answer"]:
        print(" ")
        print("Correct!!!")
        print("")
        score = score + 1
        print("your score is", score)
        print("")
    else:
        print(" ")
        print("Sorry, that was just plain wrong!")
        print("")
        print("your score is", score)
        print("")
    # Finish

    if score == 10:
        print("well done", name, "you got a perfect score")
        print("")
    elif score >= 5:
        print("not bad, you got a score of", score, "which is not bad")
        print("")
    else:
        print("I didn't think you can get", score, "you should try again")
        print("")
    # Play Again

    while True:
        Try_again = input("do you want to play again, its 'yes' or 'no'\n")
        Try_again = Try_again.lower()
        if Try_again not in ("yes", "no"):
            print(" ")
            print("that wrong, please try again")
            print("")
            continue
        else:
            break
    if Try_again == restart["a"]:
        score = score - score
        run = True
    if Try_again == restart["b"]:
        print("thank you")
        run = False

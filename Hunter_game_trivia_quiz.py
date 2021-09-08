
from playsound import playsound

import time


def welcome():
    name = input("Enter your last name")
    gender = input("What would you like to be called - e.g Mr/Mrs/Miss")
    greeting = "Welcome to my quiz " + gender + " " + name + ", ready to play? "
    print(greeting)


welcome()


def new_game():

    guesses = []   # list of guesses
    correct_guesses = 0
    question_num = 1

    for qnum in questions:
        print(" ")  # blank line between
        print(qnum)
        for i in answers[question_num-1]:   # start at 0
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()   # string uppercase
        guesses.append(guess)   # append guess onto list of guesses

        correct_guesses += check_answer(questions.get(qnum), guess)  # add value from check answer to use in scoreboard
        question_num += 1
        if guess not in valid:
            print("invalid answer, no points given")
        else:
            continue
    scoreboard(correct_guesses, guesses)

# ---


def scoreboard(correct_guesses, guesses):
    print("---------------")
    print("RESULTS")
    print("---------------")

    print("Answers:", end="")   #
    for i in questions:
        print(questions.get(i), end="")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end="")
    print()

    score = int((correct_guesses/len(questions))*100)   # score % calculation
    print("Your score is: "+str(score)+"%")  # tells user their score

# ---


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        playsound("correct.mp3")  # correct sound
        return 1    # one point
    else:
        print("WRONG!")
        playsound("incorrect.swf.mp3")  # fail sound
        return 0    # no point


# ---
def countdown(t):  # Counts down to start
    while t > 0:
        print(t)
        t -= 1
        time.sleep(1)
        print(" ")


seconds = 3
seconds = int(seconds)
countdown(seconds)
print("GO!")
# ---


def replay():

    response = input("Do you want to play again?: (YES or NO): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# ---

# dictionary of questions


questions = {
    "What is the name of the first video game ever created?": "A",
    "What is the best selling game console of all time? ": "B",
    "What year was Halo Combat Evolved released? ": "C",
    "What is the name of the main character in The Legend of Zelda? ": "A",
    "What was game of the year in 2019?": "C",
    "What food was the character Pac Man modeled after?": "D",
    "Who is Mario's brother?": "B",
    "What year was Nintendo founded?": "B",
    "What is the best selling video game of all time?": "A",
    "What year was Street Fighter 2 Released?": "C",

}

# list of possible answers in list         #storing multidimensional data
answers = [["A. Pong", "B. Space Invaders", "C. Asteroid", "D. Pac-Man"],
           ["A. Nintendo 64", "B. PlayStation 2", "C. Xbox", "D. PlayStation 3"],
           ["A. 1995", "B. 2000", "C. 2001", "D. 2004"],
           ["A. Link", "B. Zelda", "C. Impa", "D. Navi"],
           ["A. The Outer Worlds", "B. Death Stranding", "C. Sekiro", "D. Resident Evil 2"],
           ["A. Lemon", "B. Pie", "C. Banana", "D. Pizza"],
           ["A. Lorenzo", "B. Luigi", "C. Leonardo", "D. Enzo"],
           ["A. 1952", "B. 1889", "C. 1986", "D. 2000"],
           ["A. Minecraft", "B. Grand Theft Auto V", "C. Tetris(EA)", "D. Wii sports"],
           ["A. 1985", "B. 1991", "C. 1992", "D. 2011"]]

valid = ["A", "B", "C", "D"]

new_game()
# while loop to replay quiz
while replay():
    new_game()

print("Thank you for playing my quiz")

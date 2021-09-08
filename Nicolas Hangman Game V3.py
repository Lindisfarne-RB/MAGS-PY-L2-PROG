from random_word import RandomWords  # External Libraries


def welcome():  # defines the welcome function (Methods)
    name = input("WELCOME hangman player, could you please enter your name:")  # Asks the user their name
    n = 0
    while n < 1:
        if name.isdigit():  # Checks to see if the name starts with a number
            print("\nSorry but my creator designed me to only allow humans to play"
                  "\nSo if your not a robot please enter a name (Characters only)")
            name = input("\nWhat is your name:")
        else:
            print("\nThat is a very cool name!\n")
            n += 2

    b = 0
    while b < 1:  # runs a while loop
        subtitle = input(  # Asks the user if they have a title with their name
            "Another quick question before we begin, do you go by a title? e.g:Mrs, Mr, Ms(Yes/No):").lower()
        if subtitle == "yes":
            title = input("What do you go by then? (Mrs, Mr, Ms etc):") + "."
            b += 2
        elif subtitle == "no":  # Sequence doesnt give user a title
            print("Very well")
            title = ""
            b += 2
        else:
            print("Im sorry but you gotta type either yes or no")
    greeting = "\nHELLO " + title + name + "! I see you have decided to play some hangman " \
                                                 "so lets just jump straight into it!"  # String manipulation
    print(greeting)


# defines the incorrect function when the user guesses wrong
def incorrect():
    print("✘ oops sorry you got that wrong")  # prints wrong message
    print("\nWatch out there is", (10 - wrong), "more incorrect guesses left before you lose")  # shows total guesses left


# defines the correct function when the user guesses right
def correct():
    print("✔ YAY you got that one right")  # prints correct message
    print("\nWatch out there is", (10 - wrong), " more incorrect guesses left before you lose")


# hangman list:
error = ["", "\n\n\n\n\n\n\n\n------------------",
         "\n|\n|\n|\n|\n|\n|\n|\n|\n------------------",
         "\n____________\n|\n|\n|\n|\n|\n|\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/\n|\n|\n|\n|\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/    (｡UwU｡)\n|\n|\n|\n|\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/    (｡OwO｡)\n|          |\n|          "
         "|\n|\n|\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/    (｡>w<｡)\n|      ----|\n|          "
         "|\n|\n|\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/    (｡>﹏<｡)\n|      ----|----\n|          "
         "|\n|\n|\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/    (｡._.｡)\n|      ----|----\n|          "
         "|\n|         /\n|        /\n|\n|\n------------------",
         "\n____________\n|   --/    |\n|--/    (｡X=X｡)\n|      ----|----\n|          "
         "|\n|         / \ \n|        /   \ \n|\n|    You Lose :(\n------------------"]

welcome()

# This sequence below runs the entire game and allows the player to retry and start the game
gameOver = False  # This code means that the game is not over unless the user loses and chooses to stop playing
while not gameOver:
    # this sequence below tracks the different variables used in the code
    r = RandomWords()
    wrong = 0  # sets the amount of wrong guesses to '0'
    guesses = ''  # Stores the amount of total guesses
    correctGuess = ''  # Stores the amount of correct guesses
    z = 0  # This code is used to maintain the while loop for "how many letters do you want in your word"
    w = 0
    l = 0
    punctuation = ["!", "@", "#", "$", "%", "^", "&", "~", "`", "*", "(", ")", "_", "+", "=", "{", "[", "}", "]", "|",
                   ":", ";", "'", "<", ",", ">", ".", "?", "/"]

    print("\n", "-" * 50)
    while z < 1:
        while True:  # Sequence determines the amount of letters in a word from user
            try:
                value = int(input("\nFirst how many letters do you want in your word? (2 - 15):"))
                break
            except ValueError as e:  # Prevents letters from being written
                print("\nSorry write a number and not a letter please")
        if value < 2:  # code prevents from values lower then 2 to be inputted
            print("\nOnly numbers between 2 and 15 are allowed, or else i'll BREAK!!")
        elif value > 15:  # code prevents from values higher then 15 to be inputted
            print("\nOnly numbers between 2 and 15 are allowed, or else i'll BREAK!!")
        else:
            z += 2

    word = r.get_random_word(hasDictionaryDef="True", minCorpusCount=7, minLength=value, maxLength=value).lower()
    for char in word:  # prints out the mystery word
        if char == "-":  # if the word contains a "-" then it will output it
            print(char, end=" ")
            correctGuess += "-"  # adds the '-' to the correctGuess variable if in the word
        else:
            print("_", end=" ")

    gameRunning = True
    while gameRunning:
        # Sequence that codes for the guess input
        q = 0
        while q < 1:
            guess = input("Try guessing a letter:\n").lower()  # allows the user to guess a letter
            if len(guess) > 1:  # Done to prevent the guesses from containing more than one letter
                print("O-Oh you are only allowed to guess 1 letter at a time, \n")
            elif guess.isnumeric():  # Done to prevent the guesses from containing numbers
                print("Oops a number in hangman is cheating! Please enter a letter\n")
            elif guess in guesses:  # Done to prevent the guesses from being repeated
                print("Oops you already guessed this letter before, try again")
            elif guess in punctuation:  # Done to prevent the guesses from having any punctuation symbols
                print("No no, punctuations are not allowed")
            else:
                q += 2  # Makes sure that the guess is alright to input and escapes the while loop
        for char in word:  # Sequence stores letters guessed and correct guesses
            if char in guess:
                l += 1  # checks if the guess was correct and how many times it appears in the word
        correctGuess += guess * l  # if guess is correct then adds to the correctGuess variable
        l = 0
        guesses = guess + guesses  # stores all the guesses from the user

        for char in word:  # sequence of code that prints the mystery word
            if char in guesses:  # if the user has guessed a letter then it prints the letter
                print(char, end=" ")
            elif char == "-":  # if the word has a 'dash' symbol then it prints it out
                print(char, end=" ")
            else:  # for all the letters that haven't been guessed, they are left as '_'
                print("_", end=" ")
        w = 0
        if guess not in word:  # calculates how many times the user has gotten a letter wrong
            wrong += 1
            w += 1
        print(error[wrong])  # prints out the hangman depending on how many letter the user has gotten wrong

        if w == 1:
            incorrect()
        else:
            correct()
        print("\nYou have already guessed the letters:", guesses)  # shows total letters guessed

        # sequence of code for if the user loses
        if wrong >= 10:
            print("\nO-Oh sorry you have run out of guesses, and your hang man has been completed. You lose")
            print("\nthe complete word was:", word)  # prints complete word
            gameRunning = False   # Temporarily stops the game
            valid = True
            while valid:
                retry = input("\nWould you like to play again? [y/n]").lower()
                # if the user types 'y' then the game will restart with a new word
                if retry == 'y':
                    valid = False
                    gameRunning = False
                # if the user types 'n' then the game will end and thank them for playing
                elif retry == 'n':
                    print("\nThank you for playing!")
                    valid = False
                    gameOver = True
                else:
                    print("type y or n")
        # sequence of code for if the user wins
        elif sorted(correctGuess) == sorted(word):
            print("\nHURRAY! You guessed the word correctly and have won the game! ")
            gameRunning = False
            valid = True
            while valid:
                retry = input("\nWould you like to play again? [y/n]").lower()  # asks if the user wants to play again
                if retry == 'y':
                    valid = False
                elif retry == 'n':
                    print("\nThank you for playing and I hope had a great time!")
                    valid = False
                    gameOver = True
                else:
                    print("\nSorry you gotta type either 'y' or 'n'")

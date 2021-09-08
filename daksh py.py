#-------------------------------------------------------------Daksh's Code!-----------------------------------------------------------------
restart = {"a": "yes", "b": "no"}
run = True
while run is True:
    name = input("What is your name:")                                           # This to ask the end users name.
    while name.isdigit() or name== "" or name==" ":                              # This is if anyone uses numbers in there name it ask them to try again.
        print("invalid input,please try again")                                  # string
        name = input("What is your name:")
    else:
        print("You have 2 lives for Each question")                              # Welcoming the users to my quiz with using their names

    gender = input("What would you like us to call You\n Mr \n Ms\n Mrs \n")
    name = name.capitalize()
    gender = gender.capitalize()                                                 #-------------------------Useing String manipulation.
    print("Hii", gender + name, "Welcome to a Multi choice Quiz!")
    print("-----------------------------------------------------------------------------------------------")
    score = 0
    question_number = 1
    def question(questions, options, correct_ans):                               # This is a function Which gives the options , questions & answers            #-------------------- Useing DEF
        global score                                                             # Global allows me to Modify a variable
        global question_number
        counter = 2                                                              # Controlling how many lives i want them to have.
        while counter>0:                                                         # This code is for haveing 2 try's for each questions
            print(int(question_number), ".", questions)
            for i in options:
                print(i)                                                         # This a loop
            answer = input().lower().replace(".", "")                            # String
            if answer in correct_ans:                                                                                                                         #----------Useing Options From Def.
                print("Hooray!!, you got it right")                              # This is when some gets the answer right
                score += 10
                print("You have", score, "points")
                question_number += 1
                break                                                            # This so when the quiz end dose'nt keep on breaking.
            elif answer.isdigit() or answer == "":        #------------------------------------This is a Error check if any writes a Number or press enter it says invalid input try again!
                print("invalid input, please try again")
                answer = input().lower().replace(".", "")


            else:
                print("You got it wrong, You have 1 More life Good Luck! ")       # This is if they get the question wrong then they will have 2 lives left.
                print("You have", score, "points")
                counter -= 1
            while counter == 0:
                print("\n")
                print("The right answer is", correct_ans[0],"\n")                  # This is when they have got the answer wrong after two try's it will reveal the answer.
                question_number += 1
                break
    possible_cricket = ["cricket", "a"]                                            # I have made so they have a option to choose wich quiz they want to do.
    possible_football = ["football", "b"]
    options = input( "\nwhat quiz would you like to attempt\n a. Cricket\n b. Football\n")  # These are the 2 options Cricket & Fotball                    #----------Useing Options From Def.
    print("----------------------------------------------------------------------------------------")
    if options in possible_cricket:                                                         # This are the question if they pick Cricket
        question("Which ground is commonly referred to as the Home of Cricket?", ["a. HPCA stadium", "b. Lords", "c. Eden Gardens", "d. Galle International Stadium"], ["Lords", "b"])
        print("-----------------------------------------------------------------------------------------------")
        question("What is the term used when a player is bowled out by the first ball they face?", ["a. Wide", "b. Yorker", "c. Fish", "d. Goldenduck"], ["goldenduck", "d"])
        print("-----------------------------------------------------------------------------------------------")
        question("What does LBW stand for?", ["a. Leg between wicket", "b. Leg before wicket", "c. Leg After wicket", "d. Leg ball wicket"], ["Leg before wicket", "b"])
        print("-----------------------------------------------------------------------------------------------")
        question("Who is the captain of the 2020 England cricket team?", ["a. Ben Stokes ", "b. Moeen Alin", "c. Eoin Morgan", "d. Joe Root"], ["Ben Stokes", "a"])
        print("-----------------------------------------------------------------------------------------------")
        question("Which legendary bowler had the nickname 'Whispering Death'?", ["a. Michael Holding", "b. Lance Klusener", "c. Virat Kholi", "d. Jasprit Bumrah"], ["Michael Holding", "a"])
        print("-----------------------------------------------------------------------------------------------")
        question("As of 2016, who is the only player to have scored one hundred international centuries?", ["a. Virat Kholi", "b. Williamson", "c. Sachin Tendulkar", "d. MS Dhoni"], [" Sachin Tendulkar", "c"])
        print("-----------------------------------------------------------------------------------------------")
        question("Who has the most record partnerships in the history of ICC Cricket World cup?", ["a. Sourav Ganguly & Rahul Dravid", "b. Kl Rhaul & Virat Kholi" , "c. Sachin Tendulkar & MS Dhoni", "d. Marlon Samuels & Chris Gayle"], ["Marlon Samuels & Chris Gayle", "d"])
        print("-----------------------------------------------------------------------------------------------")
        question("When cricket umpires raise both their arms straight above the head, it means", ["a. It's 6 ", "b. It's a 4", "c. It's a wicket", "d. It's a Wide"], [" It's 6", "a"])
        print("-----------------------------------------------------------------------------------------------")
        question("Who is a famous bowler who is known for his deadly Yorkers and slingy action.", ["a. Malinga", "b. Jasprit Bumrah", "c. Trent Boult", "d. Chris Woakes"], ["Malinga", "a"])
        print("-----------------------------------------------------------------------------------------------")
        question("The Big Bash League is based in which country?", ["a. African", "b. Indian", "c. Australian", "d. Canadian"], ["Australian", "c"])
        print("-----------------------------------------------------------------------------------------------")
    if options in possible_football:                                                         # This are the question if they pick fotball
        question("What team dose Lionel Messi play for?", ["(a) Real Madrid", "(b) barcelona", "(c) Manchester United"], ["barcelona", "b", "B", "Barcelona"])
        print("-----------------------------------------------------------------------------------------------")
        question("What team dose Critiano Ronaldo play for?", ["(a) Barcelona", "(b) Real Madrid", "(c) Juventus"], ["c", "C", "Real Madrid", "real madrid"])
        print("-----------------------------------------------------------------------------------------------")
        question("What team dose Nemyar play for?", ["(a) Paris Saint-Germain F.C.", "(b) Arsenal FC", "(c) Everton FC"], ["a", "A", "Paris Saint-Germain", "paris saint-germain"])
        print("-----------------------------------------------------------------------------------------------")
        question("What team dose Xavi play for?", ["(a) Liverpool FC", "(b) Al Sadd SC", "(c) Southampton FC"], ["b", "B", "Al Sadd SC", "al sadd sc"])
        print("-----------------------------------------------------------------------------------------------")
        question("What team dose Andres Iniesta play for", ["(a) Manchester United", "(b) Vissel Kobe", "(c) Chelsea FC"], ["Manchester", "a", "A", 'manchester'])
        print("-----------------------------------------------------------------------------------------------")
        question("What positions dose Lionel Messi play for?", ["(a) Forward", "(b) back", "(c) Midfielder"], ["a", "A", "forward", "Forward"])
        print("-----------------------------------------------------------------------------------------------")
        question("What positions dose Critiano Ronaldo play for?", ["(a) Forward", "(b) back", "(c) Midfielder"], ["a", "A", "forward", "Forward"])
        print("-----------------------------------------------------------------------------------------------")
        question("What positions dose Nemyar play for?", ["(a) Forward", "(b) back", "(c) Midfielder"], ["a", "A", "forward", "Forward"])
        print("-----------------------------------------------------------------------------------------------")
        question("What positions dose Andres Iniesta play for?", ["(a) Forward", "(b) back", "(c) Midfielder"], ["c", "C", "Midfielder", "midfielder"])
        print("-----------------------------------------------------------------------------------------------")
    print("\n")

    #-----------------------------------------------------------------------------Play Again
    if score == 100:
            print("well done", name, "you got a perfect score")
            print("\n")
    elif score >= 50:
            print("Well done u Got", score ,"Which is not bad")
            print("\n")
    else:
            print("Hmmmmm u got", score ,"Point maybe u should try again or prehaps Play a different quiz?")
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
        print("thank's for playing Dutch's Quiz \n\n" "👍 (❛ ͜ʖ ͡❛)👍 \n\n")
        run = False



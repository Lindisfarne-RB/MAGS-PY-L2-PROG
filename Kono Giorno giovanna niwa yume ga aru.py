import time
from playsound import playsound

#Questions and Answers
q1 = """Which is the correct order that each Jojo appears?
a.Joseph, Jonathan, Jotaro, Jolyne, Josuke, Giorno, Johnny
b.Jonathan, Joseph, Jotaro, Josuke, Giorno, Jolyne, Johnny
c.Jonathan Jotaro, Joseph, Josuke, Giorno, Johnny, Jolyne
d.Joseph, Jonathan, Josuke, Jotaro, Giorno, Jolyne, Johnny 
"""

q2 = """Name the user of Gold Experience
a.Shigekiyo Yangu
b.Prosciutto
c.Ermes Costello
d.Giorno Giovanna
"""

q3 = """Which of these characters has no stand
a.Otoishi Akira
b.Lisa Lisa
c.Vanilla Ice
d.Sorbet
"""

q4 = """Who is the Stand user of Highway Star
a.Fungami Yuya 
b.Yoshikage Kira 
c.Koichi Hirose 
d.Oyanagi Ken 
"""

q5 = """Which of these is not a Jojo reference
a.How many breads have you eaten in your life
b.Jesus
c.Slapping a person with some cheese
d.A pet shop
"""

q6 = """Which of these is NOT a stand
a.Earth, wind and fire
b.ACDC
c.Cream
d.Green Day
"""

q7 = """Who is the stand user of Diver Down?
a. Narciso Anasui
b. Squallo
c. Boingo
d. Otoishi Akira
"""

q8 = """Who survives part 5?
a. Narancia Ghirga
b. Pannacotta Fugo
c. Bruno Bucciarati
d. Leone Abbacchio
"""

q9 = """What part does Jotaro NOT feature in?
a. Part 4
b. Part 5
c. Part 2
d. Part 6
"""

q10 = """What is Anjuro Katagiri's stand?
a. Clash
b. Dark Blue Moon
c. Aqua Necklace
d. Geb
"""


#dictionary of questions
questions = {q1:"b",
             q2:"d",
             q3:"b",
             q4:"a",
             q5:"c",
             q6:"b",
             q7:"a",
             q8:"b",
             q9:"c",
             q10:"c"}

#score
#score=0

def welcome_introduction():
#Initial name and welcome message
    print("hello stand user")
    name=input("Enter your name:")
    greeting=("Hello "+name+", welcome to passione\n" )

    if (name=="Jotaro Kujo"):
        print("ORA ORA ORA ORA ORA ORA ORA\n")
        playsound("oraora.mp3")

    elif (name=="Dio Brando"):
        print("ZA WARUDO\n")
        playsound("zawarudo.mp3")

    elif (name=="Giorno Giovanna"):
        print("MUDA MUDA MUDA MUDA MUDA MUDA MUDA\n")
        playsound("susmanz.mp3")

    elif (name=="joe"):
        print("Forni")
        playsound("Fart.mp3")

    else:
        print(greeting)
welcome_introduction()

def scenario():
#scenario
    print ("\n*Disclaimer* This quiz contains spoilers for the anime, play at your own risk\n")
    time.sleep(3)

    print("\nD'Arby Snr has challenged you to a bet, if you\n"
      "can get 6 or more questions right in a quiz then he\n"
      "will reveal the location of Dio's hideout, otherwise you will DIE!\n")
    time.sleep(8)

scenario()

def newgame():
    global score
    score=0
#this i is to print the questions and optons, grabbing these keys from dictionary
    for i in questions:
        print(i)
        notValid = True
        while(notValid):
            ans = input("enter the answer (a/b/c/d):")
            if(ans.lower() in ['a','b','c','d']):
                notValid = False
        #this i is for the correct answer
        if ans==questions[i]:
            print("\nYES YES YES YES YES!\n")
            playsound("yesyesyes.mp3")
            score = score+1
        else:
            print("\nyare yare daze\n")
            playsound("yareyaredaze.mp3")

    print("Final score is:",score)
newgame()

def result():
#final result of challenge
    if score>=6:
        print("D'Arby has been defeated! He however is frozen in fear, unable to tell you the hideouts location, sadge")
    else:
        print("Challenge Failed, D'Arby has stolen you're soul!")


result()


def try_again():
    playagain = input("Would you like to try again? (Y for yes, N for no)\n")
    if playagain == "y":
        newgame()
        result()
        try_again()
    elif playagain == "Y":
        newgame()
        result()
        try_again()
    elif playagain == "yes":
        newgame()
        result()
        try_again()
    elif playagain == "Yes":
        newgame()
        result()
        try_again()
    else:
        if score<=3:
            print("MUDA MUDA MUDA, useless useless useless, you cannot defeat DIO!")
            quit
        else:
            print ("""
            Leave immediatly and find Dio Stardust Crusader, bring him to justice!
            """)
            quit
try_again()
def play_again():
   print("\nDo you want to play again? (y or n)")

   # convert the player's input to lower_case
   answer = input(">").lower()

   if "y" in answer:
       # if player typed "yes" or "y" start the game from the beginning
       start()
   else:
       # if user types anything besides "yes" or "y", exit() the program
       quit()


def game_over(reason):
   # print the "reason" in a new line (\n)
   print("\n" + reason)
   print("You lived a short valuable life.")
   # ask player to play again or not by activating play_again() function
   play_again()


def End1():
   # some prompts
   print("\nSirens blow all around you as you open your eyes to see someone dragging you by the leg away from the "
         "flicking blue and red lights")
   print("you feel to tired to move but you seem to be normally sized again")
   print("now in the middle of a forget you get shoved in a wooden box in the ground as the person proceeds to lock"
         "you in")
   print("sounds of dirt being shovelled can be heard up top of the box")
   print("\nToo numb to move you just lay there as you drip blood from the glass the window left for you")
   print("\n congratulations, you've beaten the game. Obtained Bad Ending 1")
   play_again()


def End2():
    print("\n you're in a familiar house back at home, in bed, gasping. You stand up and trip over a bottle of ketchup"
          "that your little sibling dropper at the stairs. Getting up to go downstairs you see your cat in her usual"
          "corner but notice that the match box you left on your table last night from lighting fireworks with your"
          "friends is...missing.")
    play_again()


def living_room():
   # some prompts
   # '\n' is to print the line in a new line
   print("\nNow looking around you see a giant hairball and a table with what looks to be valuables")
   print("Which action do you take (1 or 2)")
   print("1). Climb up the hairball to get a better look for your surroundings")
   print("2). stack up some books, onto the couch, to the table")

   # take input()
   answer = input(">")

   if answer == "1":
       # the player dies()
       game_over("the giant hairball started to move, It was a cat which mistook you for dinner")
   elif answer == "2":
       # the player found a light source"
       print("You found a match box and carried it back to the stairs")
       lit_room2()
   else:
       # game_over() with "reason"
       game_over("I didn't get that.")


def lit_room():
   # give some prompts
   # '\n' is to print the line in a new line
   print("\nThe room lightens up as you look around you seeing nothing but giant furniture, or as if you've shrunken")
   print("You inspect the area to see a giant living room to your left and a staircase leading upwards straight in")
   print("front of you.")
   print("What will you do? (1 or 2)")
   print("1). Head up the staircase into the darkness")
   print("2). Walk into the living room unknowing of the dangers ahead")

   # take input()
   answer = input(">")

   if answer == "1":
       # the player is dead!
       print("\nYou climb up just to slip up on some sticky substance and fall back down, "
             "maybe getting some light would be better.")
       lit_room()
   elif answer == "2":
       # leads the player to the living room
       print("\nYou step into the living room.")
       living_room()
   else:
       # else call game_over() function with the "reason" argument
       game_over("Don't you know how to type a number?")


def lit_room2():
   print("\n1). Head up the staircase into the darkness")
   print("2). Walk into the living room.")

   # take input()
   answer = input(">")

   if answer == "1":
       # the player is dead!
       print("\nYou climb up the stairs and light the match to notice the red goo dripping downwards")
       print("you continue to walk through the red liquid leaving footprints behind as terrible chills go down your "
             "spine.")
       upstairs()
   elif answer == "2":
       # leads the player to the living room
       print("\nI don't need to go there right now.")
       lit_room2()
   else:
       # else call game_over() function with the "reason" argument
       game_over("Don't you know how to type a number?")


def upstairs():
   print("You're being watched.")
   print("\n1). you see a window directly in front of you, you have no time to look down,jump.")
   print("2). Walk towards they ominous presence to show you have no fear.")
   print("3). Build up your courage and run.")

   answer = input(">")

   if answer == "1":

       print("\nYou lift your feet off the ground as you close your eyes again only to hear a smash and everything"
             "turns dark")
       End1()

   elif answer == "2":

       print("\nas you walk closer towards the uneasing aura, laughter frantically starts conjuring around you as"
             "you feel someone wrap their hand around you with a soft crunch to follow it up.")
       play_again()

   elif answer == "3":

       print("\nthump thump thump thump is all you can hear as you run into things desperately trying to get out"
             "of this cursed place you were put in")
       print("\n a familiar soft voice rings in your head as it mutters 'You're mine now'")

   Familiar()


def Familiar():
   print("\n as you frantically turn left and right hoping to find the source of this voice that sounds so familiar"
         "you notice a gleam of light in the corner of your eye but as you continue to turn it follows the exact spot"
         "\n obtained a spec of light in the corner of your eye.")
   print("\nNow with voices of a familiar person going around your head your vision is enlightened even further.")
   print("1). Walk towards the door closer to you")
   print("2). Walk to the door further away from you")

   answer = input(">")

   if answer == "1":
       print("\nthe light doesn't seem to appreciate you going towards the room as it lightens even more permanently"
             "blinding you")
       game_over()

   elif answer == "2":
       print("\n finally after a full blown sprint to the door you realise it's locked but this however is no issue to"
             "you being able to crawl under the crack of the door.")
       locked_room()
   else:
       print("I didn't get that")
   Familiar()


def locked_room():
   print("\nalthough the room door felt ginormous, the room felt like your normal height. everything was perfectly sized"
         "to your height where you find a mirror, finally the first mirror. when you look at it you see...")
   print("\n 1). A normal sized girl covering her face from her forehead to her chin")
   print("\n2). A normal sized boy with a mask covering his face.")

   answer = input(">")

   if answer == "1":
       print("\n The room begins to shrink as your head hits the roof and you slowly start growing the room explodes"
             "to reveal..")
       End2()
   elif answer =="2":
       print("\n The room begins to shrink as your head hits the roof and you slowly start growing the room explodes"
             "to reveal..")
       End2()
   else:
       game_over("not an option")


def spider():
    print(
        "\nYou slowly begin to walk around it feeling 1,2,3,onward till 8, it's a spider.")
    print("\n 1). Run")
    print("\n 2). Run")

    answer = input(">")

    if answer == "1":
        print("\n you run frantically managing to escape the beast as your vision slowly adjusts to the darkness your"
              "vision grows in contrast")

    elif answer == "2":
        print("\n you run frantically managing to escape the beast as your vision slowly adjusts to the darkness your"
              "vision grows in contrast")
        print("you begin to see an opening and climb your way out of the hole you're in and walk into a house"
              "directly in front of you")
        lit_room2()

    else:
        game_over("not an option")


def underground():
    print("your surroundings are unclear, you walk around bumping into dirty material everywhere"
          "your vision is still unclear")
    print("1). run straight into the wall really hard in an attempt to break through")
    print("2). feel around for an opening to escape from")

    answer = input(">")

    if answer == "1":
        print("\nyou run straight directly into a sharp object that pierces you clean")
        game_over("that was unfortunate")
    elif answer == "2":
        print("\nyou find a different type of hairy material as it begins to move")
        spider()

    else:
        game_over("not an option")


def dark_room():
   print("You step away from the object wrapped around your arms and stumble backwards onto hard concrete pavement")
   print("\n1).your vision feels too blurry but to your right you feel the grass beneath your feet")
   print("2).under your hand that you prop yourself up with you feel cold concrete")

   answer = input (">")

   if answer == "1":
       print("\n the grassy texture slowly begins to swallow you whole as you try to get your legs unstuck your legs"
             "become consumed while frantically panicking you slowly sink under without escape")
       underground()

   elif answer =="2":
       print("\n you follow the concrete path as it progressively gets colder and colder till you see a light"
             "traveling at an extreme speed, as soon as it reaches you your vision goes blan-")
       game_over("goodbye.")

   elif answer =="3":
       print("you ignore any form of situation and just start to sprint towards a light in the distance to see a light"
             "post that stands 9 feet tall to your miniature 2 cm")
       print("the light post lets down a hand, as you grab on and the post begins walking you think to yourself")

       print("\n I lived")
       play_again()
   else:
       print("I didn't get that")
       game_over()


def start():
   name = input("what do you wish to be called?\n")
   print("\nWelcome to," + name + " and farewell")
   print("\nYou wake up gasping just to stare into empty darkness. Without a cellphone or any other object within")
   print("your grasp the only thing you can feel are the floorboards beneath your feet")
   print("You walk around aimlessly till you finally come across something that seems to be a handle")
   print("Do you want to pull it? (y or n)")

   answer = input(">").lower()

   if "y" in answer:
       # if player typed "left" or "l" lead him to bear_room()
       lit_room()
   elif "n" in answer:
       # else if player typed "right" or "r" lead him to monster_room()
       dark_room()
   else:
       # else call game_over() function with the "reason" argument
       game_over("That wasn't an option.")


# start the game
start()


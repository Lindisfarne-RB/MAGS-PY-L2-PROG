import pygame
import turtle
from playsound import playsound
import re


# External libraries used - 6

# Responding to events (GUI) - 4
def run_game():
    # Image for the field pattern
    wn = turtle.Screen()
    wn.bgpic("Field5.gif")

    # Pong Game Screen Setup
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    def main_functions():
        # First Name Input
        Player_A = wn.textinput("Player A", "Name (Only accepts letters A-Z) of the player A: ")
        Player_B = wn.textinput("Player B", "Name (Only accepts letters A-Z) of the player B: ")
        for i in Player_B:
            if i.isalpha() == False:
                main_functions()

        for y in Player_A:
            if y.isalpha() == False:
                main_functions()

        # Score
        score_a = 0
        score_b = 0

        # Paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.color("red")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # Paddle B
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.color("blue")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.changex = 0.2
        ball.changey = -0.2

        # Pen (Scoreboard)
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write(str(Player_A) + " : {}    ".format(score_a) + str(Player_B) + " : {}    ".format(score_b),
                  align="center", font=("Courier", 14, "normal"))

        # Function for paddles
        def paddle_a_up():
            y = paddle_a.ycor()
            y += 20
            paddle_a.sety(y)

        def paddle_a_down():
            y = paddle_a.ycor()
            y -= 20
            paddle_a.sety(y)

        def paddle_b_up():
            y = paddle_b.ycor()
            y += 20
            paddle_b.sety(y)

        def paddle_b_down():
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

        # Keyboard binding
        wn.listen()
        wn.onkeypress(paddle_a_up, "w")
        wn.onkeypress(paddle_a_down, "s")
        wn.onkeypress(paddle_b_up, "Up")
        wn.onkeypress(paddle_b_down, "Down")

        # Main game loop
        while True:
            wn.update()

            # Move the ball
            ball.setx(ball.xcor() + ball.changex)
            ball.sety(ball.ycor() + ball.changey)

            # Border checking
            if ball.ycor() > 290:
                ball.sety(290)
                ball.changey *= -1

            if ball.ycor() < -290:
                ball.sety(-290)
                ball.changey *= -1

            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball.changex *= -1
                score_a += 1
                pen.clear()
                pen.write(str(Player_A) + " : {}    ".format(score_a) + str(Player_B) + " : {}    ".format(score_b),
                          align="center", font=("Courier", 14, "normal"))

            if ball.xcor() < -390:
                ball.goto(0, 0)
                ball.changex *= -1
                score_b += 1
                pen.clear()
                pen.write(str(Player_A) + " : {}    ".format(score_a) + str(Player_B) + " : {}    ".format(score_b),
                          align="center", font=("Courier", 14, "normal"))

            # Paddle and ball collisions
            if (ball.xcor() > 340 and ball.xcor() < 350) and (
                    ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
                ball.setx(340)
                ball.changex *= -1
                playsound("SlapSound2.wav")

            if (ball.xcor() < -340 and ball.xcor() > -350) and (
                    ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
                ball.setx(-340)
                ball.changex *= -1
                playsound("SlapSound2.wav")

            # Restart Screen and functions
            if score_a >= 13:
                restart = wn.textinput("Game result",
                                       "Well done " + Player_A +
                                       ", you won ! \nDo you want to restart ? \nType y or yes to restart \nPress ESC to exit or type anything to exit")
                if restart == "yes":
                    wn.clearscreen()
                    run_game()
                if restart == "y":
                    wn.clearscreen()
                    run_game()

                else:
                    if wn.onkeypress(paddle_b_down, "ESC"):
                        break
            if score_b >= 13:
                restart = wn.textinput("Game result",
                                       "Well done " + Player_B +
                                       ", you won ! \nDo you want to restart ? \nType y or yes to restart \nPress ESC to exit or type anything to exit")

                if restart == "yes":
                    wn.clearscreen()
                    run_game()
                if restart == "y":
                    wn.clearscreen()
                    run_game()


                else:
                    if wn.onkeypress(paddle_b_down, "ESC"):
                        break

    main_functions()


def loading_screen():
    # general setup for loading screen
    pygame.init()
    clock = pygame.time.Clock()
    # colors
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)

    # setting up the loading screen
    screen_width = 1366
    screen_height = 768
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong")
    screen.fill(WHITE)

    # images setup for loading screen
    display_surface = pygame.display.set_mode((screen_width, screen_height))
    image = pygame.image.load("StartingScreen.png")
    display_surface.blit(image, (0, 0))
    pygame.display.flip()

    # Game Running setup for loading screen
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Keys input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    run = False
                    run_game()


loading_screen()

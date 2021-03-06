import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A maze game")
wn.setup(700, 700)


# create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


# Creates player
class Player(turtle.Turtle):
    # Creates the player
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 0

    # Code for movement of player
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    # Checks whether the player is colliding with the treasure
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        # Advanced technique 3 - return value
        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    # creates the treasure
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    # destroys the treasure when player collides
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


# create levels list
levels = [""]

# define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XPX     X    X X     X  X",
    "X   XXX X XX X X  X  X  X",
    "XXXXXXX X XX      X  X  X",
    "X         XXXXX XXX  X  X",
    "X XXXXXXXXXX X       X  X",
    "X  XX         X  XX     X",
    "XX XX  XX    XX  XXXXX  X",
    "X  XXXXXXXX  X    XXX   X",
    "X         X    XXXXXXXX X",
    "X XXXXXXX XXXX     X    X",
    "X  XT XX     X XX  X    X",
    "X  X  XXXXXX    X  XXX  X",
    "X   X  X XXXXXXXX  X    X",
    "XXX   X  XX     X  XTXXXX",
    "X   XX      X   X   XX  X",
    "XXXXXXXXXX  X   XXX  X XX",
    "X  X   X    XXXXX       X",
    "X    X   X         XXXX X",
    "X   XXXXXXXXXXXXXXXXX   X",
    "X     X  X            XXX",
    "X  X  X  X  XXXXXXXXX   X",
    "X  X  X  X TX       X   X",
    "X  X X   XXXX  XXX  XXXXX",
    "X  X   X       X X     TX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
]

# Adds a treasure list
treasures = []

levels.append(level_1)


# The setup of the maze, where the characters, walls and treasures are
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 228 - (y * 24)
            # Checks if it is a wall
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            # Checks for where the player is
            if character == "P":
                player.goto(screen_x, screen_y)
            # Checks for where the treasure is
            if character == "T":
                # Advance Technique 1 - Modifying data stored in collection
                treasures.append(Treasure(screen_x, screen_y))


# Create class instances
pen = Pen()
player = Player()

# Creates wall coordinate list
walls = []

# Set up the level
setup_maze(levels[1])

# Keyboard binds
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

# Turn off screen updates
wn.tracer(0)

# Main game loop
while True:
    # Check if player is colliding with treasure
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)

    # updates screen
    wn.update()

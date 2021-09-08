# coding=utf8
import sys  # Allow python to use this sys
import os  # Allow python to use this os
import random  # Allow python to use this random
import itertools  # Allow python to use this itertools


def trim(seqs, direction=0):  # Return the average of the array after trimming the distribution from the two tails
    return ([0, 0, 0, 0] + [n for n in seqs if n])[-4:] if direction else ([n for n in seqs if n]+[0, 0, 0, 0])[:4]


def sum_seqs(seqs, direction=0):  # The sum of the terms of an arithmetic sequence
    if seqs[1] and seqs[2] and seqs[1] == seqs[2]:  # One and two are added together, the grid in front of 1 and 2 is 0
        return trim([seqs[0], seqs[1]*2, 0, seqs[3]], direction=direction)
    if seqs[0] and seqs[1] and seqs[0] == seqs[1]:
        seqs[0], seqs[1] = seqs[0]*2, 0
    if seqs[2] and seqs[3] and seqs[2] == seqs[3]:
        seqs[2], seqs[3] = seqs[2]*2, 0
    return trim(seqs, direction=direction)


def up(grid):  # move up
    for col in [0, 1, 2, 3]:
        for _idx, n in enumerate(sum_seqs(trim([row[col] for row in grid]))):  # Generate a new grid
            grid[_idx][col] = n
    return grid


def down(grid):   # move down. Down is the opposite of up
    for col in [0, 1, 2, 3]:
        for _idx, n in enumerate(sum_seqs(trim([row[col] for row in grid], direction=1), direction=1)):
            grid[_idx][col] = n
    return grid


def left(grid):   # move left
    return [sum_seqs(trim(row)) for row in grid]


def right(grid):   # move right
    return [sum_seqs(trim(row, direction=1), direction=1) for row in grid]


class Game:  # It can be accessed and used by creating an instance of the class
    grid = []
    controls = ["w", "a", "s", "d"]

    def rnd_field(self):  # This is a random two or four to fill in
        number = random.choice([4, 2, 4, 2, 4, 2, 4, 2, 4, 2, 4, 2])
        x, y = random.choice([(x, y) for x, y in itertools.product([0, 1, 2, 3], [0, 1, 2, 3]) if self.grid[x][y] == 0])
        self.grid[x][y] = number

    def print_screen(self):   # Output interface like Graphics engine
        os.system('cls')   # Clear the screen
        print("\b")
        print('-' * 21)
        for row in self.grid:
            print('|{}|'.format("|".join([str(col or ' ').center(4) for col in row])))
            print('-' * 21)

    def logic(self, control):   #   The system logic of the entire game
        grid = {'w': up, 'a': left, 's': down, 'd': right}[control]([[c for c in r] for r in self.grid])
        if grid != self.grid:  # Use letters instead of directions to enter into the board
            del self.grid[:] # If it is not lower than the previous board, print a new board
            self.grid.extend(grid)
            if [n for n in itertools.chain(*grid) if n >= 2048]:   # Judge to win
                return 1, "You Win!"
            self.rnd_field()
        else:
            if not [1 for g in [f(grid) for f in [up, down, left, right]] if g != self.grid]:  # Judge to lose
                return -1, "You Lost"
        return 0, ''

    def main_loop(self):  # This is the main loop that controls the entire game
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]   # Initialize the entire board
        self.rnd_field()
        self.rnd_field()
        while True:
            self.print_screen()
            control = input('input w/a/s/d:')   # Controlled information
            if control in self.controls:
                status, info = self.logic(control)
                if status:
                    print(info)   # print result
                    if input('Start another game?[Y/n]').lower() == "y":   # Re-game
                        break
                    else:
                        sys.exit(0)    # exit the game
        self.main_loop()    # Recycle


if __name__ == "__main__":   # This is the code to start the game
    Game().main_loop()
import pygame
from pygame.locals import *


# function to draw a block
def draw_block():
    screen.fill((110, 110, 5))
    screen.blit(pygame.transform.scale(block, (40, 40)), (block_x, block_y))
    pygame.display.flip()


# initializing pygame
if __name__ == "__main__":
    pygame.init()

    # making the screen
    screen = pygame.display.set_mode((800, 600))

    # Title and Icon
    pygame.display.set_caption("Snake Game")
    icon = pygame.image.load("snake.jpg")
    pygame.display.set_icon(icon)

    # RGB - Red, Green, Blue
    screen.fill((110, 110, 5))

    # Working on the block
    block = pygame.image.load(r'snake.jpg').convert()
    block_x = 100
    block_y = 100
    screen.blit(pygame.transform.scale(block, (40, 40)), (block_x, block_y))
    pygame.display.flip()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                while event.key == K_UP and block_y > 0:
                    block_y -= 0.2
                    draw_block()


                while event.key == K_DOWN and block_y < 556:
                    block_y += 0.2
                    draw_block()
                while event.key == K_LEFT and block_x > 0:
                    block_x -= 0.2
                    draw_block()
                while event.key == K_RIGHT and block_x < 757:
                    block_x += 0.2
                    draw_block()

            elif event.type == QUIT:
                running = False

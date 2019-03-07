import pygame as pyg
from Bird import Bird
from Pipes import Pipes
import sys


def main():
    pyg.init()
    screen = pyg.display.set_mode((250, 500))
    pyg.display.set_caption('basic pygame program')

    # background
    background = pyg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 250, 250))

    surface = pyg.image.load("rescources/flappy-bird-background-2.jpg").convert()

    surface1 = pyg.transform.scale(surface, (250, 500))
    screen.blit(surface1, (0, 0))
    pyg.display.flip()
    birdPositionY = 100
    birdPositionx = 100
    bird = Bird()
    gravity = 4
    pipes = Pipes()
    pipesXPos = 250

    # Event loop
    while 1:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:

                return

        if pyg.key.get_pressed()[pyg.K_SPACE]:
            bird.updateY(-3)
        else:
            bird.updateY(gravity)

        pyg.display.flip()
        screen.blit(surface1, (0, 0))
        pyg.draw.circle(screen, pyg.Color("red"), (50, bird.y), 20)
        pyg.draw.rect(surface1, pyg.Color("yellow"), pyg.Rect(pipesXPos,0,50,pipes.topLength))
        pyg.draw.rect(surface1, pyg.Color("yellow"), pyg.Rect(pipesXPos, pipes.bot, 50, 1000))
        pipesXPos -= 5
        #lose condition
        if bird.y >= 500 or bird.y <= 0:
            print("you lost!")
            sys.exit(0)

        #hit detection for pipe





if __name__ == '__main__': main()

# test1_pyganim.py - A very very very basic pyganim test program.
#
# This program just runs a single animation. It shows you what you need to do to use Pyganim. Basically:
#   1) Import the pyganim module
#   2) Create a pyganim.PygAnimation object, passing the constructor a list of image filenames and durations.
#   3) Call the play() method.
#   4) Call the blit() method.
#
# The animation images come from http://www.kenney.nl, and are available under an Attribution-only license.

import sys
import os
sys.path.append(os.path.abspath('..'))
import pygame
from pygame.locals import *
import time
import pyganim

pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((320, 240), 0, 32)
pygame.display.set_caption('Pyganim Basic Demo')

# create the animation objects   ('filename of image',    duration_in_seconds)
boltAnim = pyganim.PygAnimation([('testimages/female_stand.png', 200),
                                 ('testimages/female_walk1.png', 200),
                                 ('testimages/female_walk2.png', 200),
                                 ('testimages/female_walk1.png', 200),
                                 ('testimages/female_walk2.png', 200),
                                 ('testimages/female_walk1.png', 200),
                                 ('testimages/female_jump.png', 200),
                                 ('testimages/female_walk2.png', 200),
                                 ('testimages/female_walk1.png', 200),
                                 ('testimages/female_walk2.png', 200)])
boltAnim.play() # there is also a pause() and stop() method

mainClock = pygame.time.Clock()
BGCOLOR = (100, 50, 50)
while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_l:
            # press "L" key to stop looping
            boltAnim.loop = False

    boltAnim.blit(windowSurface, (100, 50))

    pygame.display.update()
    mainClock.tick(30) # Feel free to experiment with any FPS setting.
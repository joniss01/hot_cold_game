#!/usr/bin/env python3

"""
The Hot/Cold Game!

The game will begin with a circle that will always be in the middle of the screen. The user will have to move around
the screen using the 'wsad' keys to find the hidden circle placed randomly on the screen. Once the hidden circle is
found the user will see how many moves it took to find the hidden circle.

The game difficulty can be modified with a GUI that allows the user to set the size of the circle and/ or the length
of each move.

The circle will indicate if the user moved closer or further from the hidden circle. If the circle turns red, the user
has moved one step closer to the circle. If the circle turns blue, the user is moving away from the hidden circle and
should try moving a different direction.

Controls:
W = UP
S = DOWN
A = LEFT
D = RIGHT
R = RESET

Good luck and have fun playing the Hot/Cold Game!
"""

__author__ = 'Jonathan Nissen'
__version__ = '1.0'
__copyright__ = '2024.02.29'
__github__ = 'https://github.com/joniss01/hot_cold_game'

import random
import pygame
import turtle
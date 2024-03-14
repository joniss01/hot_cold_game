#!/usr/bin/env python3

"""
The Hot/Cold Game!

The game will begin with a circle that will always be in the middle of the screen. The user will have to move around
the screen using the 'wasd' keys to find the hidden circle placed randomly on the screen. Once the hidden circle is
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
LSHIFT = DEBUG

Good luck and have fun playing the Hot/Cold Game!
"""

__author__ = 'Jonathan Nissen'
__version__ = '1.0'
__copyright__ = '2024.02.29'
__github__ = 'https://github.com/joniss01/hot_cold_game'

import pygame
import random

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 233, 0)

SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

game = {
    'circle_size': 50,
    'move_size': 50,
    'prev_x': 0,
    'prev_y': 0,
    'user_x': SCREEN_SIZE / 2,
    'user_y': SCREEN_SIZE / 2,
    'hidden_x': 0,
    'hidden_y': 0,
    'user_color': WHITE,
    'hidden_color': BLACK,
    'num_moves': 0
}

# users_circle
color_circle = WHITE
circle = pygame.draw.circle(SCREEN, color_circle, (game['user_x'], game['user_y']), 50)

# hidden_circle
hidden_circle = WHITE
h_circle = pygame.draw.circle(SCREEN, hidden_circle, (game['hidden_x'], game['hidden_y']), 50)


def play_game():
    """

    :return:
    """
    clock = pygame.time.Clock()

    run_me = True

    while run_me:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    game['user_x'] -= game['move_size']

                if event.key == pygame.K_d:
                    game['user_x'] += game['move_size']

                if event.key == pygame.K_w:
                    game['user_y'] -= game['move_size']

                if event.key == pygame.K_s:
                    game['user_y'] += game['move_size']

                if event.key == pygame.K_LSHIFT:
                    if game['hidden_color'] == BLACK:
                        game['hidden_color'] == WHITE
                    else:
                        game['hidden_color'] == BLACK

                # if event.key == pygame.K_r:
                #

        SCREEN.fill(BLACK)
        pygame.draw.circle(SCREEN, color_circle, (game['user_x'], game['user_y']), 50)
        pygame.draw.circle(SCREEN, hidden_circle, (game['hidden_x'], game['hidden_y']), 50)
        pygame.display.flip()

    # font = pygame.font.SysFont(None, 24)
    #
    # line = font.render('# ' + str(game['num_moves']) + " moves", True, YELLOW)
    # SCREEN.blit(line, (20, 20))
    #
    # debug = font.render('LSHIFT = DEBUG', True, YELLOW)
    # SCREEN.blit(debug, (20, 15))
    #
    # reset = font.render('R = RESET', True, YELLOW)
    # SCREEN.blit(reset, (20, 10))


def hidden_pos():
    """

    :return:
    """
    user_pos = SCREEN_SIZE / 2

    inside_dist = game['circle_size']
    outside_dist = SCREEN_SIZE - game['circle_size']

    right_user_dist = user_pos - game['circle_size']
    left_user_dist = user_pos + game['circle_size']

    while True:
        x = random.randint(inside_dist, outside_dist)
        y = random.randint(inside_dist, outside_dist)

        if (x < right_user_dist or x > left_user_dist) and (y < right_user_dist or y > left_user_dist):
            game['hidden_x'] = x
            game['hidden_y'] = y
            return


def main():
    """

    :return:
    """

    pygame.init()
    pygame.display.set_caption('Hot/Cold Game')

    play_game()

    pygame.quit()


if __name__ == '__main__':
    play_game()

#!/usr/bin/env python3

"""
The Hot/Cold Game!

The game will begin with a circle that will always be in the middle of the screen. The user will have to move around
the screen using the 'wasd' keys to find the hidden circle placed randomly on the screen. Once the hidden circle is
found the user will see how many moves it took to find the hidden circle.

The game difficulty can be modified with a menu that allows the user to set the size of the circle and/ or the length
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
import pygame_menu
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


def play_game():
    """

    :return:
    """
    clock = pygame.time.Clock()
    run_me = True

    font = pygame.font.SysFont(None, 24)

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
                        game['hidden_color'] = WHITE
                    else:
                        game['hidden_color'] = BLACK

                if event.key == pygame.K_r:
                    hidden_pos()
                    game['user_x'] = SCREEN_SIZE / 2
                    game['user_y'] = SCREEN_SIZE / 2
                    game['num_moves'] = -1
                    game['user_color'] = WHITE
                    game['hidden_color'] = BLACK

                game['num_moves'] += 1

        update_colors()

        SCREEN.fill(BLACK)
        pygame.draw.circle(SCREEN, game['user_color'], (game['user_x'], game['user_y']), 50)
        pygame.draw.circle(SCREEN, game['hidden_color'], (game['hidden_x'], game['hidden_y']), 50)

        render_menu(SCREEN, font)

        pygame.display.flip()


def render_menu(screen, font):
    moves_text = font.render('Moves: ' + str(game['num_moves']), True, YELLOW)
    debug_text = font.render('LSHIFT = DEBUG', True, YELLOW)
    reset_text = font.render('R = RESET', True, YELLOW)

    screen.blit(moves_text, (20, 20))
    screen.blit(debug_text, (20, 40))
    screen.blit(reset_text, (20, 60))


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


def update_colors():
    # Get current and previous positions
    curr_x, curr_y = game['user_x'], game['user_y']
    prev_x, prev_y = game['prev_x'], game['prev_y']

    # Get hidden circle position
    hidden_x, hidden_y = game['hidden_x'], game['hidden_y']

    # Check movement along x-axis
    if curr_x != prev_x:
        if abs(curr_x - hidden_x) < abs(prev_x - hidden_x):
            game['user_color'] = RED  # Closer along x-axis
        else:
            game['user_color'] = BLUE  # Moving away along x-axis

    # Check movement along y-axis
    if curr_y != prev_y:
        if abs(curr_y - hidden_y) < abs(prev_y - hidden_y):
            game['user_color'] = RED  # Closer along y-axis
        else:
            game['user_color'] = BLUE  # Moving away along y-axis

    # Update previous position for next iteration
    game['prev_x'], game['prev_y'] = curr_x, curr_y

    # Check if circles touch and turn them green
    distance = ((curr_x - hidden_x) ** 2 + (curr_y - hidden_y) ** 2) ** 0.5
    if distance <= game['circle_size'] * 2:  # Adjusted condition
        game['user_color'] = GREEN
        game['hidden_color'] = GREEN


def set_difficulty(level, difficulty):
    """

    :param level:
    :param difficulty:
    :return:
    """
    if difficulty == 3:
        game['circle_size'], game['move_size'] = (10, 10)
    elif difficulty == 2:
        game['circle_size'], game['move_size'] = (25, 25)
    else:
        game['circle_size'], game['move_size'] = (50, 50)


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('sneaky-snitch.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)


def main():
    """

    :return:
    """
    play_music()
    pygame.init()
    pygame.display.set_caption('Hot/Cold Game')

    menu = pygame_menu.Menu('Hot/Cold Game', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty :', [('Level 1', 1), ('Level 2', 2), ('Level 3', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)

    pygame.quit()


if __name__ == '__main__':
    main()

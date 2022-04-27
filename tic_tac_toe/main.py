import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = WIDTH
SQUARE_SIZE = WIDTH//3
BACKGROUND_COLOR = (28, 170, 156)
LINE_COLOR = (3, 115, 101)
X_COLOR = (66, 66, 66)
X_WIDTH = 25
SPACE = SQUARE_SIZE//4
O_COLOR = (178, 255, 238)
O_RADIUS = SQUARE_SIZE//3
O_WIDTH = 15


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BACKGROUND_COLOR)

board = np.zeros((3, 3))


def draw_board_lines():
    horitonzal_1 = pygame.draw.line(
        screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), 10)
    horizontal_2 = pygame.draw.line(
        screen, LINE_COLOR, (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), 10)
    vertical_1 = pygame.draw.line(
        screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), 10)
    vertical_2 = pygame.draw.line(
        screen, LINE_COLOR, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), 10)


def draw_figures():
    for row in range(3):
        for column in range(3):
            if board[row][column] == 1:
                pygame.draw.circle(screen, O_COLOR, (int(
                    column * SQUARE_SIZE + SQUARE_SIZE//2), int(row * SQUARE_SIZE + SQUARE_SIZE//2)), O_RADIUS, O_WIDTH)
            elif board[row][column] == 2:
                pygame.draw.line(screen, X_COLOR, (column * SQUARE_SIZE + SPACE, row * SQUARE_SIZE +
                                 SQUARE_SIZE - SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (column * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), X_WIDTH)


def mark_square(row, column, player):
    board[row][column] = player


def available_squares(row, column):
    return board[row][column] == 0


def is_board_full():
    for row in range(3):
        for column in range(3):
            if board[row][column] == 0:
                return False
    return True


def check_win(player):
    # vertical win check
    for column in range(3):
        if board[0][column] == player and board[1][column] == player and board[2][column] == player:
            draw_vertical_win_line(column, player)
            return True

    # horizontal win check
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    # diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal_ltr_win_line(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal_rtl_win_line(player)
        return True

    return False


def draw_vertical_win_line(column, player):
    pos_x = column * SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (pos_x, 15),
                     (pos_x, HEIGHT - 15), width=15,)


def draw_horizontal_win_line(row, player):
    pos_y = int(row * SQUARE_SIZE + SQUARE_SIZE//2)

    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), width=15)


def draw_diagonal_ltr_win_line(player):

    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH - 15, 15), 15)


def draw_diagonal_rtl_win_line(player):
    if player == 1:
        color = O_COLOR
    elif player == 2:
        color = X_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15)


def restart_game():
    screen.fill(BACKGROUND_COLOR)
    draw_board_lines()
    player = 1
    for row in range(3):
        for column in range(3):
            board[row][column] = 0


draw_board_lines()


player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            clicked_row = int(mouse_y // SQUARE_SIZE)
            clicked_column = int(mouse_x // SQUARE_SIZE)

            if available_squares(clicked_row, clicked_column):
                mark_square(clicked_row, clicked_column, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
                game_over = False

    pygame.display.update()

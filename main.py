import pygame
import random
import time
from pygame.locals import *

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SPEED = 1
GRID_SIZE = 40
N = 10
M = 10

# Function to add a new fruit to the game board
def addFruit(matrix):
    # Find all the indices of cells with a value of 0
    zero_indices = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 0]

    # Pick a random 0 from the list of indices
    if zero_indices:
        random_zero = random.choice(zero_indices)
        matrix[random_zero[0]][random_zero[1]] = 2
    else:
        print("There are no 0s in the matrix")

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

# Create the game board
matrix = [[0 for j in range(M)] for i in range(N)]

# Choose a random starting position for the snake
start_pos = [random.randint(0, 9), random.randint(0, 9)]
matrix[start_pos[0]][start_pos[1]] = 1

# Set up the game clock
clock = pygame.time.Clock()

# Set the initial direction for the snake
direction = 1

# Initialize the snake
snake = [start_pos]

# Initialize the score
score = 1

# Add the first fruit to the game board
addFruit(matrix)

# Main game loop
while True:
    # Set the game speed
    clock.tick(3)

    # Check for user input events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_DOWN and direction != 3:
                direction = 1
            if event.key == K_UP and direction != 1:
                direction = 3
            if event.key == K_RIGHT and direction != 4:
                direction = 2
            if event.key == K_LEFT and direction != 2:
                direction = 4

    # Move the snake
    head = snake[-1]
    if direction == 1:
        next_cell = [(head[0] + 1) % 10, head[1]]
    if direction == 3:
        next_cell = [(head[0] - 1) % 10, head[1]]
    if direction == 2:
        next_cell = [head[0], (head[1] + 1) % 10]
    if direction == 4:
        next_cell = [head[0], (head[1] - 1) % 10]

    # Check for collision with snake's body
    if matrix[next_cell[0]][next_cell[1]] == 1:
        # Game over
        screen.fill((255, 255, 255))
        font = pygame.font.Font(None, 36)
        text1 = font.render("Your Score:" + str(score), True, (0, 0, 0))
        text1_rect = text1.get_rect(center=(200, 200))
        screen.blit(text1, text1_rect)
        pygame.display.update()
        time.sleep(5)
        break
    if matrix[next_cell[0]][next_cell[1]] == 0:
            snake.append(next_cell)
            matrix[next_cell[0]][next_cell[1]]=1
            tail=snake.pop(0)
            matrix[tail[0]][tail[1]] = 0
    if matrix[next_cell[0]][next_cell[1]] == 2:
            snake.append(next_cell)
            matrix[next_cell[0]][next_cell[1]]=1
            score= score+1
            addFruit(matrix)

    for i in range(10):
        for j in range(10):
            if matrix[i][j]==1:
                    rect_color = (255, 0, 0)
                    rect_pos = (j*GRID_SIZE, i*GRID_SIZE)
                    rect_size = (GRID_SIZE, GRID_SIZE)
                    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_pos, rect_size))
            if matrix[i][j]==0:
                    rect_color = (255, 255,255)
                    rect_pos = (j*GRID_SIZE, i*GRID_SIZE)
                    rect_size = (GRID_SIZE, GRID_SIZE)
                    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_pos, rect_size))
            if matrix[i][j] == 2:
                    rect_color = (255, 255, 0)
                    rect_pos = (j * GRID_SIZE, i * GRID_SIZE)
                    rect_size = (GRID_SIZE, GRID_SIZE)
                    pygame.draw.rect(screen, rect_color, pygame.Rect(rect_pos, rect_size))
    for i in range(1, SCREEN_WIDTH // GRID_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (i * GRID_SIZE, 0), (i * GRID_SIZE, SCREEN_HEIGHT))
    for i in range(1, SCREEN_HEIGHT // GRID_SIZE):
        pygame.draw.line(screen, (0, 0, 0), (0, i * GRID_SIZE), (SCREEN_WIDTH, i * GRID_SIZE))
    pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

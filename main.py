import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

player_pos = [1, 1]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Labirent Oyunu")

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            color = WHITE if maze[row][col] == 0 else BLACK
            if maze[row][col] == 2:
                color = GREEN
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_player():
    pygame.draw.rect(screen, BLUE, (player_pos[1] * CELL_SIZE + 5, player_pos[0] * CELL_SIZE + 5, CELL_SIZE - 10, CELL_SIZE - 10))

def move_player(key):
    row, col = player_pos
    if key == pygame.K_UP and maze[row - 1][col] != 1:
        player_pos[0] -= 1
    if key == pygame.K_DOWN and maze[row + 1][col] != 1:
        player_pos[0] += 1
    if key == pygame.K_LEFT and maze[row][col - 1] != 1:
        player_pos[1] -= 1
    if key == pygame.K_RIGHT and maze[row][col + 1] != 1:
        player_pos[1] += 1

clock = pygame.time.Clock()
while True:
    screen.fill(BLACK)
    draw_maze()
    draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            move_player(event.key)

    if maze[player_pos[0]][player_pos[1]] == 2:
        print("Tebrikler! Çıkışı buldunuz!")
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(30)
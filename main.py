import pygame
from settings import*
from logic import*

pygame.init()
pygame.display.set_caption("snakee")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



def restart_game():
    snake = [[300, 200]]
    derectoin = "up"
    score = 0
    apple = create_apple()
    return snake, derectoin, apple, score

snake, direction, apple, score = restart_game()
game_state = "PLAY"



running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    draw_game(screen, snake, apple, score)

    pygame.display.update()
    clock.tick(FPS)




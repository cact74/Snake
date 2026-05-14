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



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            
            if event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left" 

            if event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

    if game_state =="PLAY":
        new_head =list(snake[0])
        if direction == "up":
            new_head[1] -= SIZE
        if direction == "down":
            new_head[1] += SIZE
        if direction == "left":
            new_head[0] -= SIZE
        if direction == "right":
            new_head[0] += SIZE
        snake.insert(0, new_head)


        if snake[0] == apple:
            score += 1
            apple = create_apple()
        else:
            snake.pop()



            
    draw_game(screen, snake, apple, score)

    pygame.display.update()
    clock.tick(FPS)



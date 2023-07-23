import pygame
import random

pygame.init()

# Set up the screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake variables
snake_block = 10
snake_speed = 10

# Snake function to draw the snake
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, snake_block, snake_block])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Initial position of the snake
    snake_list = []
    length_of_snake = 1
    snake_x = SCREEN_WIDTH // 2
    snake_y = SCREEN_HEIGHT // 2
    snake_list.append((snake_x, snake_y))

    # Food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    # Snake direction
    snake_direction_x = 0
    snake_direction_y = 0

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            # Game over screen
            screen.fill(WHITE)
            font = pygame.font.Font(None, 36)
            message = font.render("You Lost! Press Q-Quit or C-Play Again", True, RED)
            screen.blit(message, [SCREEN_WIDTH // 6, SCREEN_HEIGHT // 3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction_x = -snake_block
                    snake_direction_y = 0
                elif event.key == pygame.K_RIGHT:
                    snake_direction_x = snake_block
                    snake_direction_y = 0
                elif event.key == pygame.K_UP:
                    snake_direction_y = -snake_block
                    snake_direction_x = 0
                elif event.key == pygame.K_DOWN:
                    snake_direction_y = snake_block
                    snake_direction_x = 0

        # Move the snake
        snake_x += snake_direction_x
        snake_y += snake_direction_y

        # Check for collisions with the screen boundaries
        if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_list)

        pygame.display.update()

        # Check for collisions with the food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()

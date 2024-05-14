"""
The code is a snake game implemented using Pygame.
The game consists of a snake that moves around the screen and eats blue circles and green rectangle to increase its score.
the color of the snake is black, the blue circles are blue, the red square is red, and the green rectangle is green.
The blue circles are randomly placed on the screen and the snake can eat them to increase it's score by 1.
The green rectangle is randomly placed on the screen and the snake can eat it to increase it's score by 3.
The red square is randomly placed on the screen and the snake dies if it collides with it because it is a BOMB.
The game ends and restarts if the snake collides with the walls of the screen, and the score is displayed on the screen.
The snake dies if it collides with a red square.
The snake can also eat a green square to increase it's score by 3 and reset the positions of the red and green squares.

Author: Amir Sarrafzadeh Arasi
Date: 05/14/2024
"""

import pygame
import random
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

snake_x, snake_y = width // 2, height // 2
snake_size = 10
snake_speed = 10
snake_dx, snake_dy = 0, 0

blue_circles = []
red_square = [random.randint(0, width - 10), random.randint(0, height - 10)]
green_square = [random.randint(0, width - 10), random.randint(0, height - 10)]
score = 0

clock = pygame.time.Clock()

def create_blue_circle():
    x = random.randint(0, width - 10)
    y = random.randint(0, height - 10)
    return [x, y]

def draw_objects():
    screen.fill(white)
    pygame.draw.rect(screen, red, red_square + [10, 10])
    pygame.draw.rect(screen, green, green_square + [10, 10])
    for circle in blue_circles:
        pygame.draw.ellipse(screen, blue, circle + [10, 10])
    pygame.draw.ellipse(screen, black, [snake_x - snake_size // 2, snake_y - snake_size // 2, snake_size, snake_size])
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, black)
    screen.blit(text, (10, 10))
    pygame.display.update()

def check_collision():
    global score, red_square, green_square
    for circle in blue_circles:
        if snake_x < circle[0] + 10 and snake_x + snake_size > circle[0] and snake_y < circle[1] + 10 and snake_y + snake_size > circle[1]:
            score += 1
            blue_circles.remove(circle)
            blue_circles.append(create_blue_circle())
    if snake_x < red_square[0] + 10 and snake_x + snake_size > red_square[0] and snake_y < red_square[1] + 10 and snake_y + snake_size > red_square[1]:
        announce_defeat('BOMB!')
        pygame.quit()
        sys.exit()
    if snake_x < green_square[0] + 10 and snake_x + snake_size > green_square[0] and snake_y < green_square[1] + 10 and snake_y + snake_size > green_square[1]:
        score += 3
        green_square[0] = random.randint(0, width - 10)
        green_square[1] = random.randint(0, height - 10)
        red_square[0] = random.randint(0, width - 10)
        red_square[1] = random.randint(0, height - 10)

def announce_defeat(message):
    font = pygame.font.Font(None, 60)
    text = font.render(message, True, red)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

def game_loop():
    global snake_x, snake_y, snake_dx, snake_dy, score, blue_circles
    blue_circles = [create_blue_circle() for _ in range(5)]
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_dx, snake_dy = 0, -snake_speed
                elif event.key == pygame.K_DOWN:
                    snake_dx, snake_dy = 0, snake_speed
                elif event.key == pygame.K_LEFT:
                    snake_dx, snake_dy = -snake_speed, 0
                elif event.key == pygame.K_RIGHT:
                    snake_dx, snake_dy = snake_speed, 0
        snake_x += snake_dx
        snake_y += snake_dy
        if snake_x < 0 or snake_x > width or snake_y < 0 or snake_y > height:
            announce_defeat('Game Over!')
            snake_x, snake_y = width // 2, height // 2
            snake_dx, snake_dy = 0, 0
            score = 0
            blue_circles = [create_blue_circle() for _ in range(5)]
            continue
        check_collision()
        draw_objects()
        clock.tick(30)

game_loop()
pygame.quit()

"""Simple pong game"""
# Author: Liam Kelly
# Date: 2020

import pygame
from ball import Ball
from paddle import Paddle

def main():
    # init pygame, set screen size to 700x500
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 500
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")
    display_w, display_h = pygame.display.get_surface().get_size()

    # Game environment variables
    done = False

    # Simple Color constants
    COLOR_BLACK = (0, 0, 0)
    COLOR_WHITE = (255, 255, 255)

    # Paddle constants
    paddle_width = 10
    paddle_height = 100
    paddle_a_x = 20
    # Make sure paddle b is same distance from side of screen
    paddle_b_x = display_w - paddle_width - paddle_a_x

    # Instantiate the paddles
    paddle_a = Paddle(COLOR_WHITE, paddle_width, paddle_height, display_h)
    paddle_a.rect.x = paddle_a_x
    paddle_a.rect.y = display_h / 2

    paddle_b = Paddle(COLOR_WHITE, paddle_width, paddle_height, display_h)
    paddle_b.rect.x = paddle_b_x
    paddle_b.rect.y = display_h / 2

    # Ball constants
    ball_width = 10
    ball_height = 10
    ball_x = display_w / 2 - ball_width / 2
    ball_y = display_h / 2 - ball_height / 2

    # Instantiate the ball
    ball = Ball(COLOR_WHITE, ball_width, ball_height)
    ball.rect.x = ball_x
    ball.rect.y = ball_y

    # Create a list to contain all the sprites
    sprite_list = pygame.sprite.Group()
    sprite_list.add(paddle_a)
    sprite_list.add(paddle_b)
    sprite_list.add(ball)

    # Velocity of paddles
    paddle_velocity = 5

    # Controls
    paddle_a_up_key = pygame.K_w
    paddle_a_down_key = pygame.K_s
    paddle_b_up_key = pygame.K_UP
    paddle_b_down_key = pygame.K_DOWN

    # Clock for screen update speed
    clock = pygame.time.Clock()

    # Player scores
    score_a = 0
    score_b = 0

    ### Main game loop
    while not done:
        ### Event loop for changing game state
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: # Can quite by pressing ESCAPE
                    done = True
        
        ### Input detection
        keys = pygame.key.get_pressed()
        if keys[paddle_a_up_key]:
            paddle_a.move_up(paddle_velocity)
        if keys[paddle_a_down_key]:
            paddle_a.move_down(paddle_velocity)
        if keys[paddle_b_up_key]:
            paddle_b.move_up(paddle_velocity)
        if keys[paddle_b_down_key]:
            paddle_b.move_down(paddle_velocity)
        
        ### Game logic updates
        # Update the sprites
        sprite_list.update()

        # Check for score
        if ball.rect.x >= display_w - ball_width:
            score_a += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            score_b += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y >= display_h - ball_height:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y <= 0:
            ball.velocity[1] = -ball.velocity[1]

        # Check for collisions between ball and paddles
        if pygame.sprite.collide_mask(ball, paddle_a) or pygame.sprite.collide_mask(ball, paddle_b):
            ball.bounce()

        ### Screen drawing updates
        # Clear the screen
        screen.fill(COLOR_BLACK)

        # Draw the net
        pygame.draw.line(screen, COLOR_WHITE, [display_w / 2, 0], [display_w / 2, display_h], 5)

        # Draw the sprites
        sprite_list.draw(screen)

        # Display the scores
        font = pygame.font.Font(None, 50)
        text = font.render(str(score_a), 1, COLOR_WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(score_b), 1, COLOR_WHITE)
        screen.blit(text, (420, 10))

        # Update the screen
        pygame.display.flip()

        # Limit display to 60 frames/sec
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()

import pygame, sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Game screen settings
screen=pygame.display.set_mode((1280,800))

# Paddle settings
paddle = pygame.Rect(400,680,150,10)

#set the ball
# ball = pygame.Rect(400,400,10,10)
ball = pygame.Rect(paddle.centerx - 5, paddle.top - 10, 10, 10)
ball_dx = 3
ball_dy = 3

#brick settings
bricks = [pygame.Rect(50+100*i, 50+20*j, 80, 10) for i in range(12) for j in range(4)]

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)
    
def game_over():
    draw_text("GAME OVER", 48, screen.get_width()/2, screen.get_height()/2)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()
    
def victory():
    draw_text("VICTORY!", 48, screen.get_width()/2, screen.get_height()/2)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()
    
# game loop
while True:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -=8
    if keys[pygame.K_RIGHT] and paddle.right < 1280:
        paddle.right +=8
        
    #move the ball
    ball.left += ball_dx
    ball.top += ball_dy
    
    #Border and ball collide
    if ball.left <= 0 or ball.right >= 1280:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
        
    #If the ball is below the paddle, game over
    if ball.top >= paddle.bottom:
        game_over()
        
    #Collision with paddle and ball
    if ball.colliderect(paddle):
        ball_dy *= -1
        
    #Collision wuth bricks and balls
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_dy *= -1
        
    #Check for victory
    if len(bricks) == 0:
        victory()
        
    #Draw the screen
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), paddle)
    pygame.draw.rect(screen, (255,255,255),ball)
    for brick in bricks:
        pygame.draw.rect(screen, (255, 0, 0), brick)
        
    #screen update
    pygame.display.flip()
    
    #set frame rate
    pygame.time.delay(10) 
    
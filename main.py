import pygame
from sys import exit
from pygame.locals import *
from pygame import mixer


pygame.init()
GRAVITY = 0.5
JUMP_VELOCITY = -10

player_vel_y = 0
jump_sound = pygame.mixer.Sound('sounds/jump.mp3')



screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()



player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,300))

snail_rectangle = snail_surface.get_rect(bottomright = (600,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
            elif event.key == pygame.K_LEFT:
                player_rectangle.x -= 30
            elif event.key == pygame.K_RIGHT:
                player_rectangle.x += 30
        if event.type == pygame.KEYUP:
            print('key up')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_sound.play()
                player_vel_y = JUMP_VELOCITY
        if event.type == pygame.KEYUP:
            pass

    player_rectangle.y += player_vel_y
    player_vel_y += GRAVITY

    # Don't let the player fall through the ground
    if player_rectangle.bottom > 300:
        player_rectangle.bottom = 300
        player_vel_y = 0

    screen.blit(sky_surface,(0,0)) 
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rectangle.x -= 4
    if snail_rectangle.right <= 0: snail_rectangle.left = 800
    screen.blit(snail_surface,snail_rectangle)
    screen.blit(player_surface,player_rectangle)
   
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
       #print('jumped')

    


    #if player_rectangle.colliderect(snail_rectangle):
    #     print('collison')

    
    pygame.display.update()
    clock.tick(60)
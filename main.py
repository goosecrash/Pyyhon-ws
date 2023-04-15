import pygame
from sys import exit
from pygame.locals import *
from pygame import mixer
import time

pygame.init()
font = pygame.font.SysFont("font/", 60)

game_over_text = font.render("Game Over", True, (255, 0, 0))
game_over_rect = game_over_text.get_rect(center=(800/2, 400/2))

def player_animation():
    global player_surface, player_index

    if player_rectangle.bottom < 300:
        player_surface = player_jump
    else:
        player_index = (player_index + 0.1) % len(player_walk)
        player_surface = player_walk[int(player_index)]

pygame.mixer.music.load("audio/background_music.mp3")

# Play the music file in an infinite loop
pygame.mixer.music.play(loops=-1)

# Define constants  for the screen width and height
GRAVITY = 0.5
JUMP_VELOCITY = -10

# Set up variables
player_vel_y = 0
jump_sound = pygame.mixer.Sound('sounds/jump.mp3')

game_paused = False
menu_state = "main"
font = pygame.font.SysFont("arialblack", 40)
# Set up the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Runner')

# Set up the game clock and font
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)

# Load the game graphics
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surface = player_walk[player_index]
mystery_block_surface = pygame.image.load('graphics/mystery_block.png').convert_alpha()
mystery_block_rectangle = mystery_block_surface.get_rect(midbottom=(80, 300))
screen.blit(mystery_block_surface, mystery_block_rectangle)

# Load game sounds

coin_sound = pygame.mixer.Sound('sounds/coin.mp3')
coin_surface = pygame.image.load('graphics/coin.png').convert_alpha()


# Set up the player rectangle
player_rectangle = player_surface.get_rect(midbottom = (80,300))

# Set up the snail rectangle
snail_rectangle = snail_surface.get_rect(bottomright = (600,300))



game_active = True
# Game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            exit()
            print('quit')
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

    # Update player position based on velocity
    player_rectangle.y += player_vel_y
    player_vel_y += GRAVITY

    # Don't let the player fall through the ground
    if player_rectangle.bottom > 300:
        player_rectangle.bottom = 300
        player_animation()
        player_vel_y = 0
    
    # Render game graphics
    if game_active == True:
       screen.blit(sky_surface,(0,0)) 
       screen.blit(ground_surface,(0,300))
       screen.blit(text_surface,(300,50))
       screen.blit(snail_surface,snail_rectangle)
       screen.blit(player_surface,player_rectangle)
   # if player_rectangle.colliderect(mystery_block_rectangle):
      # coin_sound.play()
      # coin_rectangle = coin_surface.get_rect(center=mystery_block_rectangle.center)
      # screen.blit(coin_surface, coin_rectangle)

    # Update snail position
    snail_rectangle.x -= 4
    if snail_rectangle.right <= 0: 
        snail_rectangle.left = 800  
    # Render snail and player rectangles

   
    # Check for collisions
    if snail_rectangle.colliderect(player_rectangle):
       screen.fill((0, 0, 0))
       game_active = False
       screen.blit(game_over_text, game_over_rect)
    elif event.type == pygame.MOUSEBUTTONDOWN:
         game_active = True
         pygame.display.update()
    # Update the game display
    pygame.display.update()
    
    # Set the game clock to 60 FPS
    clock.tick(60)
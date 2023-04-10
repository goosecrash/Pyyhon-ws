import pygame

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Detect Mouse and Keyboard Inputs")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse button pressed at", event.pos)
        elif event.type == pygame.KEYDOWN:
            print("Key pressed:", pygame.key.name(event.key))

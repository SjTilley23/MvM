import pygame
from Character import Character
from Sprites import Sprite

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
character = Sprite(RED,20,20)

pygame.init()
RUN = True
window = pygame.display.set_mode([800,800])
clock = pygame.time.Clock()

while RUN:

    #exiting the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    #Background
    window.fill((120,120,120))
    
    #adding a controllable character with sprites
    character.draw_player(window)
    character.move_player()







    clock.tick(30)
    pygame.display.flip()
pygame.quit()
import pygame
from Character import Character
from Sprites import Sprite

player = Sprite((255,0,0),20,20)
character = Character("placeholder", 1)

pygame.init()
RUN = True
window = pygame.display.set_mode([800,800])
clock = pygame.time.Clock()
character_chosen = False

while RUN:

    #exiting the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    #Background
    window.fill((120,120,120))

    if character_chosen == False:
        selection = input("Choose your character: ")
        Character.character_selection(character, selection)
        character_chosen = True


    if character_chosen:
        #adding a controllable character with sprites
        player.draw_player(window)
        player.move_player(character.speed)







    clock.tick(30)
    pygame.display.flip()
pygame.quit()
import pygame
from Character import Character
from Sprites import Sprite
from Drawing import Drawing

player = Sprite((255,0,0),20,20)
character = Character("placeholder", 1)


pygame.init()
RUN = True
window = pygame.display.set_mode([800,800])
clock = pygame.time.Clock()
character_chosen = False
character_selection_screen = 1
fontFace = pygame.font.SysFont("Tahoma", 30)
play_button_clicked = False

while RUN:

    Click = pygame.mouse.get_pressed()

    #exiting the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    #Background
    window.fill((120,120,120))

    if character_chosen == False:

        #Menu Screen on startup
        Drawing.draw_rect_border(window,325,520,150,50,(150,150,150),(40,40,40),2)
        Drawing.draw_text(window,"Play Game", 329,522,True,(0,0,0),fontFace)
        Drawing.repeating_rect(window, 200,100, 100, 100, (255,255,255), (0,0,0), 3, 150,150,3,9)

        
        #if Drawing.click_border(325,475,500,550) and previous_click == False and Click[0]:
            #play_button_clicked = True



        # Character selection screen
        #if character_selection_screen == 0:




    if character_chosen and play_button_clicked:
        #adding a controllable character with sprites
        player.draw_player(window)
        player.move_player(character.speed)







    previous_click = Click[0]
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
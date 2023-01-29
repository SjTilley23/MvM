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
fontFace2 = pygame.font.SysFont("Tahoma", 15)
play_button_clicked = False

while RUN:

    Click = pygame.mouse.get_pressed()

    #exiting the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    #Background
    window.fill((120,120,120))

    if character_chosen == False or play_button_clicked == False:

        #Character select screen on startup
        Drawing.draw_rect_border(window,325,520,150,50,(150,150,150),(40,40,40),2)
        Drawing.draw_text(window,"Play Game", 329,522,True,(0,0,0),fontFace)
        Drawing.repeating_rect(window, 200,100, 100, 100, (255,255,255), (0,0,0), 3, 150,150,3,9)
        Drawing.repeating_text(window,["John","Sinestra","Carlos","Aaron","Paul","Emily","Sinestro","Alucard","Redfleet"], 
                                        205,200,True,(0,0,0),fontFace2,3,150,150)
        
        #Determines if the player has clicked a character box and what box they clicked
        character_select_box = Drawing.repeating_click_box(200,300,100,200,3,150,150,9)
        if character_select_box and previous_click == False and Click[0]:
            Character.character_selection(character, int(character_select_box[1]))
            character_chosen = True
        
        #Determines if player has clciked the play game button
        if Drawing.click_border(325,475,520,570) and previous_click == False and Click[0]:
            play_button_clicked = True


    #if player has chosen a character this draws it and lets them move it
    if character_chosen and play_button_clicked:
        player.draw_player(window)
        player.move_player(character.speed)

    





    previous_click = Click[0]
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
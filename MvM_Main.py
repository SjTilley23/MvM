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

    # Exiting the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    
    # Background
    window.fill((120,120,120))

        
    if play_button_clicked == False:
        # Menu Screen on startup
        Drawing.draw_rect_border(window,325,520,150,50,(150,150,150),(40,40,40),2)
        Drawing.draw_text(window,"Play Game", 329,522,True,(0,0,0),fontFace)
        Drawing.repeating_rect(window, 200,100, 100, 100, (255,255,255), (0,0,0), 3, 150,150,3,9)
        Drawing.repeating_text(window,["the classic","the single","the fart","the butt",
            "the placeholder","the placeholder 2"], 205,200,True,(0,0,0),fontFace2,3,150,150)
        
        #characters on the selection screen
        pygame.draw.rect(window,(255,0,0),(237,137,26,26))
        pygame.draw.rect(window, (150,0,150), (387,137,26,26))

    if character_chosen == False:
        # Determining if a character has been clicked
        if Drawing.click_border(200,300,100,200) and previous_click is False and Click[0]:
            Character.character_selection(character,"John")
            character_chosen = True
        if Drawing.click_border(350,450,100,200) and previous_click is False and Click[0]:
            Character.character_selection(character, "Sinestra")
            character_chosen = True

    #Determining if the play button has been clicked    
    if Drawing.click_border(325,475,500,550) and previous_click is False and Click[0]:
        play_button_clicked = True



    if character_chosen and play_button_clicked:
        # Adding a controllable character with sprites
        
        test_wall = pygame.draw.rect(window,(0,0,0),(300,300,100,400))
        player_collision_rect = pygame.draw.rect(window, (0,0,0), (player.rect.x, player.rect.y,20,20))
        is_colliding = pygame.Rect.colliderect(player_collision_rect, test_wall)
        if is_colliding:
            



        player.draw_player(window)
        player.move_player(character.speed)

    





    previous_click = Click[0]
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
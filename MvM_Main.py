import pygame


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
    










    clock.tick(30)
    pygame.display.flip()
pygame.quit()
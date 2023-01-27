import pygame
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def draw_player(self, window):
        window.blit(self.image, (self.rect.x,self.rect.y))

    def move_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y = self.rect.y - 1
        if key[pygame.K_DOWN]:
            self.rect.y = self.rect.y + 1
        if key[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + 1
        if key[pygame.K_LEFT]:
            self.rect.x = self.rect.x - 1
        
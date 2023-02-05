import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    #draws the character onto the screen
    def draw_player(self, window):
        window.blit(self.image, (self.rect.x,self.rect.y))

    #Moves the player with the arrow keys
    def move_player(self, speed):
        y_coord = 0
        x_coord = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y = self.rect.y - speed
            y_coord = 1
        if key[pygame.K_DOWN]:
            self.rect.y = self.rect.y + speed
            y_coord = -1
        if key[pygame.K_RIGHT]:
            self.rect.x = self.rect.x + speed
            x_coord = 1
        if key[pygame.K_LEFT]:
            self.rect.x = self.rect.x - speed
            x_coord = -1
        return (x_coord, y_coord)
    
    def character_collision_detect(self, window, width, height, rect_list):

        character_box = pygame.draw.rect(window, (0,0,0), (self.rect.x, self.rect.y, width, height))
        colliding_rectangle = pygame.Rect.collidelist(character_box, rect_list)
        if colliding_rectangle == -1:
            return colliding_rectangle
        else:
            return colliding_rectangle

    def collide_correct(self, direction_this_frame, player_speed):
        x_direction = direction_this_frame[0]
        y_direction = direction_this_frame[1]
        
        match x_direction:
            case -1:
                self.rect.x += player_speed
            case 0:
                pass
            case 1:
                self.rect.x -= player_speed
        match y_direction:
            case -1:
                self.rect.y -= player_speed
            case 0:
                pass
            case 1:
                self.rect.y += player_speed
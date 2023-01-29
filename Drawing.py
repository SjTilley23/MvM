import pygame
pygame.init()

class Drawing:
    def __init__(self) -> None:
        pass

    def draw_text(window, text, coordinate_x, coordinate_y, anti_alias, color, fontFace):
        Surface = fontFace.render(text,anti_alias,color)
        window.blit(Surface,(coordinate_x,coordinate_y))
    
    def draw_rect_border(window, coordinate_x, coordinate_y, width, height, fill_color, border_color, border_width):
        pygame.draw.rect(window, fill_color, (coordinate_x, coordinate_y, width, height))
        pygame.draw.rect(window, border_color, (coordinate_x, coordinate_y, width, height), border_width)

    def click_border(small_x, big_x, small_y, big_y):
        if (pygame.mouse.get_pos()[0] >= small_x and pygame.mouse.get_pos()[0] <= big_x
            and pygame.mouse.get_pos()[1] >= small_y and pygame.mouse.get_pos()[1] <= big_y):
            return True
        else:
            return False

    def repeating_rect(window, coordinate_x, coordinate_y, width, height, fill_color, border_color, border_width, x_offset, y_offset, max_in_x, total):
        
        pygame.draw.rect(window, fill_color, (coordinate_x, coordinate_y, width, height))
        pygame.draw.rect(window, border_color, (coordinate_x, coordinate_y, width, height), border_width)

        list_total = total
        while list_total > 0:
            
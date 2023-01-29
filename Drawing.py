import pygame
pygame.init()

class Drawing:
    def __init__(self) -> None:
        pass

    #draws text onto the screen
    def draw_text(window, text, coordinate_x, coordinate_y, anti_alias, color, fontFace):
        Surface = fontFace.render(text,anti_alias,color)
        window.blit(Surface,(coordinate_x,coordinate_y))
    
    #draws a single rectangle with a border
    def draw_rect_border(window, coordinate_x, coordinate_y, width, height, fill_color, border_color, border_width):
        pygame.draw.rect(window, fill_color, (coordinate_x, coordinate_y, width, height))
        pygame.draw.rect(window, border_color, (coordinate_x, coordinate_y, width, height), border_width)

    #Detects whether the mouse is in a specific rectangular space
    def click_border(small_x, big_x, small_y, big_y):
        if (pygame.mouse.get_pos()[0] >= small_x and pygame.mouse.get_pos()[0] <= big_x
            and pygame.mouse.get_pos()[1] >= small_y and pygame.mouse.get_pos()[1] <= big_y):
            return True
        else:
            return False

    # allows pygame to draw repeating rectangles with borders, in both lines and grids
    def repeating_rect(window, coordinate_x, coordinate_y, width, height, fill_color, border_color, border_width, x_offset, y_offset, max_in_x, total):
    
        #sets temporary variables to compare to function variables every frame
        coordinate_y_temp = coordinate_y
        coordinate_x_temp = coordinate_x
        max_in_x_check = 0
        list_total = total
        
        #checks if total # of rectangles has been reached
        while list_total > 0:
            
            #Draws the rectangles with the modified coordinates
            pygame.draw.rect(window,fill_color,(coordinate_x_temp, coordinate_y_temp, width, height))
            pygame.draw.rect(window, border_color, (coordinate_x_temp, coordinate_y_temp, width, height), border_width)
            
            #Shifts the x coord by the offset
            coordinate_x_temp += x_offset

            #Checks if max number of rectangles in a row has been reached, if it has it resets the x coord and shift the y by the offset
            max_in_x_check += 1
            if max_in_x_check == max_in_x:
                coordinate_x_temp = coordinate_x
                coordinate_y_temp += y_offset
                max_in_x_check = 0

            list_total -= 1
    
    def repeating_text(window, text_as_list, coordinate_x, coordinate_y, anti_alias, color, fontFace, max_in_x, x_offset, y_offset):

        coordinate_x_temp = coordinate_x
        coordinate_y_temp = coordinate_y
        max_in_x_temp = 0
        
        
        for index, amount in enumerate(text_as_list):
            surface = fontFace.render(str(amount), anti_alias, color)
            window.blit(surface, (coordinate_x_temp,coordinate_y_temp))
            coordinate_x_temp += x_offset            
            
            max_in_x_temp += 1
            if max_in_x_temp == max_in_x:
                coordinate_x_temp = coordinate_x
                coordinate_y_temp += y_offset
                max_in_x_temp = 0


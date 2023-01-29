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
    

    #Draws text on the screen in a repeating, grid like pattern.
    def repeating_text(window, text_as_list, coordinate_x, coordinate_y, anti_alias, color, fontFace, max_in_x, x_offset, y_offset):

        #Sets a few temporary variables to use for loops and tracking, reset every frame
        coordinate_x_temp = coordinate_x
        coordinate_y_temp = coordinate_y
        max_in_x_temp = 0
        
        #Enumerates the list of text given as an argument and draws each amount
        #at the specific coordinates, also shifts the x coordinate value by the shift in x
        for index, amount in enumerate(text_as_list):
            Surface = fontFace.render(str(amount), anti_alias, color)
            window.blit(Surface, (coordinate_x_temp,coordinate_y_temp))
            coordinate_x_temp += x_offset            
            
            #Tracks the number written in a row and if it reaches the maximum
            #it resets the x coordinate value and changes the y coordinate
            #value by the shift in y
            max_in_x_temp += 1
            if max_in_x_temp == max_in_x:
                coordinate_x_temp = coordinate_x
                coordinate_y_temp += y_offset
                max_in_x_temp = 0
    

    #Draws "Click boxes" on the screen in a repeating grid like pattern
    #Click boxes are areas on the screen that are invisible but the user
    #can click their mouse and get a response. Basically an invisible button.
    def repeating_click_box(small_x, big_x, small_y, big_y, max_in_x, shift_in_x, shift_in_y, total):

        #Sets a bunch of temp variable to be reset every frame
        current_box_number = 1
        small_x_temp = small_x
        small_y_temp = small_y
        big_x_temp = big_x
        big_y_temp = big_y
        max_in_x_temp = 0
        temp_total = total

        #keeps track of total number of boxes made
        while temp_total > 0:
            
            #Draws the click boxes and returns True if hovered over and returns what box hovered over
            if (pygame.mouse.get_pos()[0] >= small_x_temp and pygame.mouse.get_pos()[0] <= big_x_temp
                    and pygame.mouse.get_pos()[1] >= small_y_temp and pygame.mouse.get_pos()[1] <= big_y_temp):
                    return True, int(current_box_number)
            
            #shofting the box by the x_shift value and keeping track of what box is going to be drawn next
            small_x_temp += shift_in_x
            big_x_temp += shift_in_x
            max_in_x_temp += 1
            current_box_number += 1

            #Checks if the max # of boxes in a row has been reached and resets the x value and shifts
            #the y value by the shift in y
            if max_in_x_temp == max_in_x:
                small_x_temp = small_x
                big_x_temp = big_x
                small_y_temp += shift_in_y
                big_y_temp += shift_in_y
                max_in_x_temp = 0
                
            temp_total -= 1
        
        #If none of the above conditions have been met the funciton returns false
        return False
    

class Character:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    #Characters with different stats, kind of like a list but way more readable
    def character_selection(self,name):
        selection = name
        if selection == 1:
            self.name = "John"
            self.speed = 1
        if selection == 2:
            self.name = "Sinestra"
            self.speed = 10
        if selection == 3:
            self.name = "Carlos"
            self.speed = 5
        if selection == 4:
            self.name = "Aaron"
            self.speed = 1
        if selection == 5:
            self.name = "Paul"
            self.speed = 10
        if selection == 6:
            self.name = "Emily"
            self.speed = 5
        if selection == 7:
            self.name = "Sinestro"
            self.speed = 1
        if selection == 8:
            self.name = "Alucard"
            self.speed = 10
        if selection == 9:
            self.name = "Redfleet"
            self.speed = 5

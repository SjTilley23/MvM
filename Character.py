class Character:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    #Characters with different stats, kind of like a list but way more readable
    def character_selection(self,name):
        selection = name
        if selection == "John":
            self.name = "John"
            self.speed = 1
        if selection == "Sinestra":
            self.name = "Sinestra"
            self.speed = 10
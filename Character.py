class Character:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    def character_selection(self,name):
        selection = name
        if selection == "John":
            self.name = "John"
            self.speed = 1
        if selection == "Sinestra":
            self.name = "Sinestra"
            self.speed = 10
class Character:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    
    #Characters with different stats, kind of like a list but way more readable
    def character_selection(self,number_select):
        match number_select:
            case 1:
                self.name = "John"
                self.speed = 1
            case 2:
                self.name = "Sinestro"
                self.speed = 10
            case 3:
                self.name = "Meatball"
                self.speed = 5
            case 4:
                self.name = "Aaron"
                self.speed = 1
            case 5:
                self.name = "Paul"
                self.speed = 10
            case 6:
                self.name = "Emily"
                self.speed = 5
            case 7:
                self.name = "Sinestro"
                self.speed = 1
            case 8:
                self.name = "Alucard"
                self.speed = 10
            case 9:
                self.name = "Redfleet"
                self.speed = 5

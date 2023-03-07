class Pet:
    def __init__(self, pet_list):
        self.name = pet_list[0]
        self.type = pet_list[1]
        self.tricks = pet_list[2]
        self.health = pet_list[3]
        self.energy = pet_list[4]


    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 10
        self.energy += 5
        return self

    def play(self):
        self.health += 5
        return self
    
    def noise(self):
        print("I hate baths!")
        return self


class Doggo(Pet):
    def __init__(self, pet_list):
        super().__init__(pet_list)
        self.is_good_boy = True

    def noise(self):
        print("woof woof")
        return self

class Catto(Pet):
    def __init__(self, pet_list):
        super().__init__(pet_list)
        self.claws_out = False

    def noise(self):
        print("mew mew")
        return self
    
    def play(self):
        self.claws_out = True
        self.energy -= 5
        self.claws_out = False
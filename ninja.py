from pet import *

class Ninja:
    def __init__(self, first, last, treats, pet_food):
        self.first = first
        self.last = last
        self.treats = treats
        self.pet_food = pet_food
        # self.pet = Pet(pet) ----  removed | invoke adopt() method to associate a pet now
        self.pet = []

    def adopt(self, species, pet_list):
        if species == 'Doggo':
            self.pet.append(Doggo(pet_list))
            print("You got a good boy!")
            print(f"Added the Doggo {pet_list[0]} at location pet[{len(self.pet) - 1}]!")
        elif species == 'Catto':
            self.pet.append(Catto(pet_list))
            print("Watch out for those claws!")
            print(f"Added the Catto {pet_list[0]} at location pet[{len(self.pet) - 1}]!")
        else: 
            self.pet.append(Pet(pet_list))
            print("Can you walk a fish?")
            print(f"Added the Pet {pet_list[0]} at location pet[{len(self.pet) - 1}]!")
        
        return self
        
    
    def walk(self, target=0):
        self.pet[target].play()
        return self

    def feed(self, target=0):
        self.pet[target].eat()
        return self

    def bathe(self, target=0):
        self.pet[target].noise()
        return self
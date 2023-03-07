# Dojo Pets!

## Class List
Ninja - Ninjas can adopt pets and then walk, feed, and bathe them
Pet - Pets are associated to Ninjas so the Pet methods can be called when Ninjas walk, feed, or bathe their Pet
    Doggo(Pet) - Doggos are a subclass of Pet, adding only the "good boy" attribute, which is always True
    Catto(Pet) - Cattos are a subclass of Pet, adding the dangerous claws_out attribute

## Adopting Pets

Ninja.adopt(species, pet_list)

Ninjas can adopt a Pet by invoking the adopt() method and passing in a species and list. Species is used to determine if the Pet should be generated using a subclass or the parent class Pet. The list is not a list of pets, although it would be awesome to adopt more than one at a time. Instead, the list is the full attribute list for initializing a Pet.

Pets are stored in a list. Invoking a Ninja.pet method() also requires the list index for pet to target the correct pet:
    Ninja.pet[0].sleep() would invoke the sleep() method for the pet at 0 idx for Ninja's self.pet list

## Caring for Pets

Ninjas mothods are invoked to care for their pets.

/**
  For all methods below: 
    * target should be the idx value (int) of the target Pet
    * target is optional and defaults to 0
*/

Ninja.walk(target) -  invokes the Pet.play() method of self.pet[target] Pet
Ninja.feed(target) - invokes the Pet.eat() method of self.pet[target] Pet
Ninja.bathe(target) - invokes the Pet.noise() method of self.pet[target] Pet

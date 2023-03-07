from ninja import Ninja
from pet import Pet, Doggo, Catto

# lily = ["Lily", "Lhasadoodle", ["napping", "chasing flies", "following dad"], 100, 50]
# gray = Ninja("gray", "Boulware", "dog biscuits", "kibbel", lily)

# print(gray)
# print(lily)

# gray.feed().walk().bathe()

#! Update to allow speciating with Pet subclasses

gray = Ninja("gray", "Boulware", {
    'dog treats' : "dog biscuits",
    'cat treats' : "catnip",
    'fish treats' : "do you give treats to fish?"
    }, 
    {
        'dog food' : "kibble",
        'cat food' : 'meow mix',
        'fish food' : 'whatever fish eat'
    })

lily = gray.adopt('Doggo', ["Lily", "Lhasadoodle", ["napping", "chasing flies", "following dad"], 100, 50])

milo = gray.adopt('Catto', ["Milo", "American Shorthair", ["scratching", "knocking sh*t over", "annoying dad"], 999, 50000])

goldee = gray.adopt('goldfish', ["Goldee", "Goldfish", ["booping the glass", "swimming in a circle"], 35, 35])

print(gray.pet[1])
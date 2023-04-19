
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound

class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy level is: {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy level is: {self.energy}")
        print(f"{self.name}'s health level is: {self.health}")
        return self

    def play(self):
        self.health += 5
        self.energy -= 25
        print(f"{self.name}'s energy level is: {self.energy}")
        print(f"{self.name}'s health level is: {self.health}")
        return self

    def pet_noise(self):
        print(self.noise)






# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
Loki = Pet("Loki", "Corgi", "Zoomies", "Awwwwooooooo!!! Werewolves of London!")


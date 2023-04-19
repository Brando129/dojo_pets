from classes.pet import Pet
from classes.ninja import Ninja

# Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.
Loki = Pet("Loki", "Corgi", "Zoomies", "Awwwwooooooo!!! Werewolves of London!")
Brandon = Ninja("Brandon", "Colangelo","Sour patch kids", "Table scraps", Loki)

# Have the Ninja feed, walk and bathe their pet.
Brandon.feed().walk().bathe()

# Use Inheritance to create sub classes of pets.

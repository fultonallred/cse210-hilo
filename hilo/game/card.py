import random

class Card:
    """A card with a number from1 to 13.
    
    Attributes: value (int): an random integer from 1 to 13"""

    def __init__(self):
        """Constructs a new instance of Card with a value attribute.
        
        Args:
            self (Die): an instance of Die."""

        self.value = 0

    def draw(self):
        """Generates a new random value.
        
        Args:
            self (Die): An instance of Die."""

        self.value = random.randint(1, 13)
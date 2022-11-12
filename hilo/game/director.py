from game.card import Card

class Director:
    """A person who directs the game.
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
        card_1 (Card): A Card instance
        card_2 (Card): A Card instance
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
        guess (str): A user guess of either h or l for higher or lower.
        comparison (str): Indicates whether card_2 is h or l than card_1.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card_1 = Card()
        self.card_2 = Card()
        self.is_playing = True
        self.total_score = 300
        self.guess = None
        self.comparison = None

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self( Director): and instance of Director.
        """

        self.card_1.draw()
        self.card_2.draw()

        while self.is_playing:
            
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Asks the user if they want to play then asks for a guess.
        
        Args:
            self (Director): An instance of Director."""
        

        print(f"The card is {self.card_1.value}.")

        keep_playing = input("Want to draw another? (y/n): ")
        self.is_playing = (keep_playing == "y")
        if not self.is_playing:
            return

        self.guess = input("Is the next card higher or lower? (h/l): ")

    def do_updates(self):
        """Updates the player's score.
        
        Args:
            self (director): and instance of Director."""
        if not self.is_playing:
            return

        if self.card_1.value > self.card_2.value:
            self.comparison = "l"

        elif self.card_1.value < self.card_2.value:
            self.comparison = "h"

        elif self.card_1.value == self.card_2.value:
            self.comparison = "tie"


        if self.guess == self.comparison:
            self.total_score += 100
        
        elif self.guess != self.comparison:
            self.total_score -= 75

        self.card_1.value = self.card_2.value
        self.card_2.draw()


        

    def do_outputs(self):
        """"""
        if not self.is_playing:
            return

        print()

        if self.guess == self.comparison:
            print(f"Correct! The next card was {self.card_1.value}. "
            f"Your score is now {self.total_score}.")
        elif self.guess != self.comparison:
            print(f"Wrong! The next card was {self.card_1.value}. "
            f"Your score is now {self.total_score}.")
        elif self.comparison == "tie":
            print("It was the same! No score change.")

        print()

        self.isplaying = (self.total_score > 0)


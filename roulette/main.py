import random
from .bets import *

class roulette:
    def __init__(self):
        # initialize the roulette history with 10 random spins
        self.previous = [random.randint(0, 36) for _ in range(10)]
    
    def spin(self):
        self.previous.pop(0)
        self.previous.append(random.randint(0, 36))

    def bet(self, amount, bet_type, selection):
        self.spin()  # spin the wheel before processing the bet

        # dictionary mapping each bet type to its corresponding function
        bet_functions = {
            "color": bet_on_color,
            "number": bet_on_number,
            "dozen": bet_on_dozen,
            "parity": bet_on_parity,
            "lohi": bet_on_lohi,
            "column": bet_on_column
        }

        # validate the bet type
        if bet_type not in bet_functions:
            raise ValueError(f"Invalid bet_type: '{bet_type}'. Supported bet types are: "
                             "'color', 'number', 'dozen', 'parity', 'lohi', 'column'.")

        bet_function = bet_functions[bet_type]

        try:
            return bet_function(self.previous[-1], amount, selection)
        except Exception as e:
            raise RuntimeError(f"An error occurred while processing the bet: {e}")

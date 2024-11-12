# Roulette Python Library

A Python library that simulates a roulette game with various types of bets, allowing you to experience roulette betting strategies programmatically.

## Features

- **Simulate Roulette Spins**: Easily simulate spins and get outcomes.
- **Place Various Bets**: Supports multiple bet types, including:
  - Color bets (`red`, `black`, `green`)
  - Number bets (specific numbers from 0 to 36)
  - Dozen bets (`1-12`, `13-24`, `25-36`)
  - Parity bets (`even`, `odd`)
  - Low/High bets (`1-18` for low, `19-36` for high)
  - Column bets (`1st`, `2nd`, and `3rd` column)
- **Calculate Payouts**: Each bet returns the calculated payout based on the type and outcome.

## Installation

To install the library locally:

1. Clone the repository:
   
   ```bash
   git clone https://github.com/roman-ladus/roulette.git
   ```
   
3. Navigate to the library directory:
   
   ```bash
   cd roulette
   ```

5. Install using `pip`:
   
   ```bash
   pip install .
   ```

## Usage

Below is an example of how to use the Roulette Simulator Library in a Python script:

```python
from roulette import roulette, bet_on_color

# create a roulette game instance
game = roulette()

# place a color bet on 'black' with an amount of 20
result = game.bet(amount=20, bet_type="color", selection="black")
print("Color bet result:", result)

# place a number bet on '21' with an amount of 20
result = game.bet(amount=20, bet_type="number", selection=21)
print("Number bet result:", result)
```

## Bet Types and Functions

Each type of bet has a corresponding function within the library:

| Bet Type | Function         | Description                                             |
|----------|------------------|---------------------------------------------------------|
| Color    | `bet_on_color`   | Bet on a color (`red`, `black`, `green`)                |
| Number   | `bet_on_number`  | Bet on a specific number (0–36)                         |
| Dozen    | `bet_on_dozen`   | Bet on a dozen (1 for 1–12, 2 for 13–24, 3 for 25–36)  |
| Parity   | `bet_on_parity`  | Bet on parity (`odd`, `even`)                           |
| Low/High | `bet_on_lohi`    | Bet on low (`1-18`) or high (`19-36`) numbers           |
| Column   | `bet_on_column`  | Bet on columns (1st, 2nd, 3rd)                          |

## Requirements

- Python 2.6 or higher

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

If you wish to contribute, please fork the repository and submit a pull request. Any contributions, whether code, bug fixes, or documentation improvements, are welcome!

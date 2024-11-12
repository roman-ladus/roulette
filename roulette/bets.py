
def bet_on_color(outcome, amount, selection):
    
    if selection not in ["red", "black", "green"]:
        raise ValueError("Invalid selection: Choose 'red', 'black', or 'green'.")

    red = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 23, 25, 27, 30, 32, 34, 36}

    if outcome == 0 and selection == "green":
        return amount * 35
    elif outcome in red and selection == "red":
        return amount * 2
    elif outcome not in red and selection == "black":
        return amount * 2
    return 0

def bet_on_parity(outcome, amount, selection):
    
    if selection not in ["odd", "even"]:
        raise ValueError("Invalid selection: Choose 'odd' or 'even'.")

    if outcome != 0 and outcome % 2 == 0 and selection == "even":
        return amount * 2
    elif outcome != 0 and outcome % 2 != 0 and selection == "odd":
        return amount * 2
    return 0

def bet_on_lohi(outcome, amount, selection):

    if selection not in ["low", "high"]:
        raise ValueError("Invalid selection: Choose 'low' or 'high'.")

    if outcome > 18 and selection == "high":
        return amount * 2
    elif outcome <= 18 and outcome > 0 and selection == "low":
        return amount * 2
    return 0

def bet_on_dozen(outcome, amount, selection):

    if selection not in [1, 2, 3]:
        raise ValueError("Invalid selection: Choose a dozen between 1 and 3.")

    if (selection - 1) * 12 < outcome <= selection * 12:
        return amount * 3
    return 0

def bet_on_number(outcome, amount, selection):

    if selection < 0 or selection > 36:
        raise ValueError("Invalid selection: Choose a number between 0 and 36.")

    if outcome == selection:
        return amount * 35
    return 0

def bet_on_column(outcome, amount, selection):
    
    if selection not in [1, 2, 3]:
        raise ValueError("Invalid selection: Choose a column between 1 and 3.")

    if outcome != 0 and (outcome - 1) % 3 + 1 == selection:
        return amount * 2
    return 0

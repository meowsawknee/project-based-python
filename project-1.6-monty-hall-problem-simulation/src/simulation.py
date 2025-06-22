from game import simulate_game

# Run the game multiple times (e.g., 1000 or 10,000 rounds)
# to compare if the "switch" strategy performs better than "stay".

def run_simulation(num_trials: int = 1000) -> tuple[float, float]:
    """Runs the Monty Hall simulation for a number of trials and compares win rates.

    :param num_trials: Number of games to simulate for each strategy
    :type num_trials: int, optional
    :return: Tuple containing win rate for switching and staying
    :rtype: tuple[float, float]
    """
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        if simulate_game(switch=True):
            switch_wins += 1
        if simulate_game(switch=False):
            stay_wins += 1
    
    switch_rate = switch_wins / num_trials
    stay_rate = stay_wins / num_trials
    
    return switch_rate, stay_rate
import random
from typing import Dict

def simulate_game(switch: bool) -> bool:
    """Simulates one round of the Monty Hall problem.

    :param switch: Whether the player decides to switch their choice after the host reveals a goat.
    :type switch: bool
    :return: True if the player wins the car, False otherwise.
    :rtype: bool
    """
    # Create a list of doors with 2 goats and 1 car
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    # Simulate the player's initial random choice (0, 1, or 2)
    player_choice = random.choice([0, 1, 2])

    # Find doors that the host can reveal (not chosen by player and not the car)
    possible_doors_to_reveal = [i for i in range(3) if i != player_choice and doors[i] == 'goat']
    host_reveal_door = random.choice(possible_doors_to_reveal)
    # possible_doors_to_reveal = []
    # for i in range(3):
    #     if i != player_choice and doors[i] == 'goat':
    #         possible_doors_to_reveal.append(i)

    # Determine final choice: switch or stay
    if switch:
        # Only one remaining door that is not player's original or host's reveal
        final_choice = [i for i in range(3) if i != player_choice and i != host_reveal_door][0]
    else:
        final_choice = player_choice
    
    # Return whether the final choice was the car
    return doors[final_choice] == 'car'


def simulate_game_manual(player_choice: int, switch: bool) -> Dict[str, int]:
    """Simulate a manual Monty Hall game with user input.

    :param player_choice: Door number chosen by the player (0, 1, or 2)
    :type player_choice: int
    :param switch: Whether the player switches after the host reveals a goat.
    :type switch: bool
    :return: A dictionary with positions of car, goat doors, host reveal, and final result.
    :rtype: dict
    """
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    host_reveal_door = random.choice(
        [i for i in range(3) if i != player_choice and doors[i] == 'goat']
    )

    if switch:
        final_choice = [i for i in range(3) if i != player_choice and i != host_reveal_door][0]
    else:
        final_choice = player_choice
    
    return {
        'doors': doors,
        'player_choice': player_choice,
        'host_reveal': host_reveal_door,
        'final_choice': final_choice,
        'won': doors[final_choice] == 'car'
    }
"""
Rock, Paper, Scissors, Lizard, Spock 

You're facing off against Sheldon Cooper in an extended version of the classic game.
Reach 5 points before Sheldon does... or suffer the wrath of his ego.

Author: Hossein Mehrabi
Inspired by The Big Bang Theory, created by Sam Kass and Karen Bryla.
"""

import random


# --- Constansts ---
CHOICES = ["rock", "paper", "scissors", "lizard", "spock"]
WIN_CONDITIONS = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["paper", "spock"],
    "spock": ["rock", "scissors"],
}
ACTIONS = {
    ("scissors", "paper"): "cuts",
    ("paper", "rock"): "covers",
    ("rock", "lizard"): "crushes",
    ("lizard", "spock"): "poisons",
    ("spock", "scissors"): "smashes",
    ("scissors", "lizard"): "decapitates",
    ("lizard", "paper"): "eats",
    ("paper", "spock"): "disproves",
    ("spock", "rock"): "vaporizes",
    ("rock", "scissors"): "crushes"
}

# --- Game Setup ---
print("🧠 Welcome to Rock, Paper, Scissors, Lizard, Spock")
player_name = input("What's your name, challenger? ").strip().capitalize()
print(f"Hello {player_name}, prepare to face Sheldon Cooper!")
print("-" * 50)

player_score = 0
sheldon_score = 0


# --- Game Loop ---
while player_score < 5 and sheldon_score < 5:
    user_input = input(f"\nChoose one ({', '.join(CHOICES)}), or type 'q' to quit: ").lower().strip()

    if user_input == "q":
        print("🚪 Game exited. Maybe next time, Bazinga!")
        break

    if user_input == "bazinga":
        print("💥 Sheldon: Nice try, but I'm the only one allowed to say that.")
        continue

    if user_input not in CHOICES:
        print("❗ Invalid choice. Try again using only the allowed options.")
        continue

    sheldon_choice = random.choice(CHOICES)
    print(f"🤖 Sheldon chooses: {sheldon_choice}")

    if user_input == sheldon_choice:
        print("⚖️ It's a tie. Great minds think alike.")
    elif sheldon_choice in WIN_CONDITIONS[user_input]:
        action = ACTIONS.get((user_input, sheldon_choice), "defeats")
        print(f"🏆 {player_name}'s {user_input.capitalize()} {action} Sheldon's {sheldon_choice.capitalize()}! You win this round.")
        player_score += 1
    else:
        action = ACTIONS.get((sheldon_choice, user_input), "defeats")
        print(f"Sheldon's {sheldon_choice.capitalize()} {action} your {user_input.capitalize()}! He wins. Bazinga!")
        sheldon_score += 1
    
    print(f"📊 Score - {player_name}: {player_score} | Sheldon: {sheldon_score}")


# --- Result ---
if player_score == 5:
    print(f"\n🎉 Congratulations {player_name}, you defeated Sheldon Cooper!")
elif sheldon_score == 5:
    print(f"\n🧬 Sheldon: As expected, the superior intellect prevails. BAZINGA!!!")

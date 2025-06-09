from typing import Type
from src.base import PasswordGenerator


def test_uniqueness(generator: PasswordGenerator, n: int = 1000) -> None:
    """Generate multiple passwords and report how many are unique.

    Args:
        generator (PasswordGenerator): An instance of a password generator class.
        n (int, optional): Number of passwords to generate. Defaults to 1000.
    
    Returns:
        None. Prints the unqueness statistics to the console.
    """
    passwords = [generator.generate() for _ in range(n)]
    unique_passwords = set(passwords)
    num_unique = len(unique_passwords)
    num_duplicates = n - num_unique
    uniqueness_rate = (num_unique / n) * 100
 
    print(f"🔍 Generated {n} passwords.")
    print(f"✅ Unique passwords: {num_unique}")
    print(f"♻️ Duplicates: {num_duplicates}")
    print(f"📊 Uniqueness rate: {uniqueness_rate:.2f}%")
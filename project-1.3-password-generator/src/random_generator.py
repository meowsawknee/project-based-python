import random
import string
from src.base import PasswordGenerator
from src.utils.strength_estimator import estimate_strength

class RandomPasswordGenerator(PasswordGenerator):
    """
    Generates a random password using letters, digits, and/or symbols.

    Attributes:
        length (int): Length of the generated password.
        use_symbol (bool): Whether to include punctuation symbols.
        use_digit (bool): Whether ro include digits.

    Example:
        >>> generator = RandomPasswordGenerator(10, True, True)
        >>> generator.generate()
        'A8!j@dW2z%'
    """
    
    def __init__(self, length: int = 8, use_symbols: bool = False, use_digits: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if use_symbols:
            self.characters += string.punctuation
        if use_digits:
            self.characters += string.digits
    
    def generate(self) -> str:
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        self._last_password = password # Refacored: save last generated password
        self._last_strength = estimate_strength(password) # Refacored: save password strength
        return password
    
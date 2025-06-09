import random
import string
from src.base import PasswordGenerator
from src.utils.strength_estimator import estimate_strength

class PinCodeGenerator(PasswordGenerator):
    """Generates a numeric pin code of specified length."""

    def __init__(self, length: int = 4):
        self.length = length
    
    def generate(self) -> str:
        password = ''.join(random.choice(string.digits) for _ in range(self.length))
        self._last_password = password
        self._last_strength = estimate_strength(password)
        return password
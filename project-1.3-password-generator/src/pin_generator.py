import random
import string
from src.base import PasswordGenerator


class PinCodeGenerator(PasswordGenerator):
    """Generates a numeric pin code of specified length."""

    def __init__(self, length: int = 4):
        self.length = length
    
    def generate(self) -> str:
        return ''.join(random.choice(string.digits) for _ in range(self.length))
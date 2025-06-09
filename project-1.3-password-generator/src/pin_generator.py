import random
import string
from typing import Optional

from src.base import PasswordGenerator
from src.utils.strength_estimator import estimate_strength


class PinCodeGenerator(PasswordGenerator):
    """Generates a numeric PIN code with optional constraints.
    
    Args:
        length (int): Length of the generated PIN code. (including checksum if enabled)
        only_even (bool): If True, all digits will be even.
        only_odd (bool): If True, all digits will be odd.
        starts_with (str): If provided, the PIN code will start with this number.
        checksum (bool): If True, adds a checksum digit at the end.

    Example:
        >>> pin = PinCodeGenerator(5, only_even=True, starts_with="2", checksum=True)
        >>> pin.generate()
        '28640'
    """

    def __init__(self,
                length: int = 4,
                only_even: bool = False,
                only_odd: bool = False,
                starts_with: Optional[str] = None,
                checksum: bool = False
    ):
        self.only_even = only_even
        self.only_odd = only_odd
        self.starts_with = starts_with
        self.checksum = checksum
        self.length = length
    
        if only_even:
            self.allowed_digits = "02468"
        elif only_odd:
            self.allowed_digits = "13579"
        else:
            self.allowed_digits = string.digits

    def generate(self) -> str:
        digits = []

        if self.starts_with:
            digits.append(self.starts_with)
        
        num_required = self.length - len(digits)

        if self.checksum:
            num_required -= 1

        digits += [random.choice(self.allowed_digits) for _ in range(num_required)]

        if self.checksum:
            check_digit = sum(int(digit) for digit in digits) % 10
            digits.append(str(check_digit))

        password = ''.join(digits)
        self._last_password = password
        self._last_strength = estimate_strength(password)
        return password
    
    def regenerate(self) -> str:
        return self.generate()

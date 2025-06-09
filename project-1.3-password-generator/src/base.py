import os
from abc import ABC, abstractmethod
from src.utils.strength_estimator import estimate_strength


class PasswordGenerator(ABC):
    """
    Abstract base class for all password generators.
    """
    def __init__(self):
        self._last_password = None # Refactored : added to store generated password
        self._last_strength = None # Refactored : added to store password strength

    @abstractmethod
    def generate(self) -> str:
        """Generate a password."""
        pass
    
    def get_strength(self) -> str:
        """
        Get the strength of the last generated password.

        Returns:
            str: Strength level.

        Raises :
            ValueError: If no password has been generated yet.
        """
        if self._last_strength is None:
            raise ValueError("No password generated yet. Call 'generate()' first.")
        return self._last_strength
    
    def export_to_file(self, filename: str = "password.txt") -> None:
        """
        Save the last generated password to a file.

        Args:
            filename (str): Name of the output file (default: 'password.txt').

        Raises:
            ValueError: If no password has been generated yet.

        """
        if self._last_password is None:
            raise ValueError("No password generated yer. Call 'generate()' first.")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self._last_password)
        print(f"✅ Password exported to {os.path.abspath(filename)}")

    def copy_to_clipboard(self) -> None:
        """
        Copy the last generated password to the system clipboard.

        Raises:
            ValueError: If no password has been generated yet.
            ImportError: If pyperclip is not installed.
        """
        if self._last_password is None:
            raise ValueError("No password generated yet. Call 'generate()' first.")
        
        try:
            import pyperclip
            pyperclip.copy(self._last_password)
            print("📋 Password copied to clipboard")
        except ImportError:
            raise ImportError("pyperclip is not installed. Run 'pip install pyperclip' to use this feature.")
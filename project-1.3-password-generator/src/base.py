from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
    """Abstract base class for all password generators."""

    @abstractmethod
    def generate(self) -> str:
        """Generate a password."""
        pass
        
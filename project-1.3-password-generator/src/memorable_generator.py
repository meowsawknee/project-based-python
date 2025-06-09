import random
from nltk.corpus import stopwords
from src.base import PasswordGenerator
from src.utils.strength_estimator import estimate_strength

class MemorablePasswordGenerator(PasswordGenerator):
    """
    Generates a memorable password using a set of words.

    The password is created by selecting random words from a vocabulary list,
    optionalyy capitalizing them and joining them with a custom separator.

    Attributes:
        number_of_words (int): How many words to use in the password.
        separator (str): Character user to join the words. Defalt is '-'.
        capitalization (bool): If True, each word is capitalized. Default is False.
        vocabulary (list[str]): Custom list of words. If None, default to English stopwords.
    
    Example:
        >>> generator = MemorablePasswordGenerator(3, separator='_', capitalization=True)
        >>> generator.generate()
        'These_Are_Words'
    """

    def __init__(self, number_of_words: int, separator: str = "-", capitalization: bool = False, vocabulary: list[str] = None):
        self.number_of_words = number_of_words
        self.separator = separator
        self.capitalization = capitalization
        self.vocabulary = vocabulary if vocabulary else self._default_vocabulary()

    def _default_vocabulary(self) -> list[str]:
        """Fetch default list of English stopwords (length > 3, alphabetic only)"""
        words = stopwords.words('english')
        return [word for word in words if word.isalpha() and len(word) > 3]
    
    def generate(self) -> str:
        """Generate a password by joining random words from the vocabulary."""
        words = random.sample(self.vocabulary, self.number_of_words)
        if self.capitalization:
            words = [word.capitalize() for word in words]
        password = self.separator.join(words)
        self._last_password = password # Refacored: save last generated password
        self._last_strength = estimate_strength(password) # Refacored: save password strength
        return password
    
def score_length(length: int) -> int:
    """
    Assign a score (0-3) based on the length of the password.

    Args:
        length (int): The length of the password.

    Returns:
        int: A score from 0 to 3.
    """
    if length < 6:
        return 0
    elif length < 8:
        return 1
    elif length < 10:
        return 2
    else:
        return 3



def estimate_strength(password: str) -> str:
    """
    Estimate the strength of a password based on its length and character variety.

    Args:
        password (str): The password to be evaluated.

    Returns:
        str: A strength level such as 'Very Weak', 'Weak', 'Medium', 'Strong', or 'Very Strong'.
    """
    score = 0
    length = len(password)
    score += score_length(length)
    
    # Score by character variety
    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1
    
    if any(c.isdigit() for c in password):
        score += 1
    
    if any(not c.isalnum() for c in password): # punctuation, symbols
        score += 1
    
    if score <= 2:
        return "Very Weak"
    elif score <= 4:
        return "Weak"
    elif score <= 6:
        return "Medium"
    elif score <= 8:
        return "Strong"
    else:
        return "Very Strong"
    

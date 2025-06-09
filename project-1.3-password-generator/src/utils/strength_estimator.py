def estimate_strength(password: str) -> str:
    """
    Estimate the strength of a password based on its length and character variety.

    Args:
        password (str): The password to be evaluated.

    Returns:
        str: A strength level such as 'Very Weak', 'Weak', 'Medium', 'Strong', or 'Very Strong'.
    """
    
    return len(password)
def is_happy(n: int) -> bool:
    """
    Determine whether a number is a'happy' number.
    
    A number is happy if repeatedly replacing it with the sum of the square of its digits
    eventually leads to 1. If it enters a loop that doesn't include 1, it's not happy.

    Args:
        n (int): A positive integer to check

    Returns:
        bool: True if the number is happy, False otherwise.
    
    Example:
        >>> is_happy(19)
        True

        >>> is_happy(4)
        False
    """
    seen_numbers = set()

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum([int(digit) ** 2 for digit in str(n)])

    return n == 1


if __name__ == "__main__":
    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)

        if number <= 0:
            raise ValueError("Number must be positive.")
        
        if is_happy(number):
            print(f"{number} is a happy number.")
        else:
            print(f"{number} is NOT a happy number.")
    
    except ValueError as e:
        print(f"Invalid input: {e}")

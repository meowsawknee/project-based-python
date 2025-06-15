from run import is_happy

def test_happy_numbers():
    # Positive happy numbers
    assert is_happy(1) is True
    assert is_happy(7) is True
    assert is_happy(10) is True
    assert is_happy(19) is True
    assert is_happy(100) is True

    # Positive unhappy numbers
    assert is_happy(2) is False
    assert is_happy(4) is False
    assert is_happy(45) is False
    assert is_happy(89) is False

    # Test big number
    assert is_happy(1000000) is True

if __name__ == "__main__":
    test_happy_numbers()
    print("✅ All tests passed!")
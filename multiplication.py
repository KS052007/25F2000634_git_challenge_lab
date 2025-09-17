def multiply(a, b):
    """Multiply two numbers and return the result"""
    return a * b

def test_multiplication():
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"7 * 8 = {multiply(7, 8)}")
    print(f"-4 * 6 = {multiply(-4, 6)}")

if __name__ == "__main__":
    test_multiplication()
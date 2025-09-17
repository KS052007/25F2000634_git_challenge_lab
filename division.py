def divide(a, b):
    """Divide a by b and return the result"""
    if b == 0:
        return "Error: Can't divide by zero"
    return a / b

def test_division():
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"10 / 0 = {divide(10, 0)}")
    print(f"7 / 3 = {divide(7, 3)}")

if __name__ == "__main__":
    test_division()
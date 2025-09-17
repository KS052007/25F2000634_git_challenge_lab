def add(a, b):
    """Add two numbers and return the result"""
    return a + b

def test_addition():
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 + 20 = {add(10, 20)}")
    print(f"-5 + 3 = {add(-5, 3)}")

if __name__ == "__main__":
    test_addition()

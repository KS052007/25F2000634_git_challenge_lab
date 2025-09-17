def subtract(a, b):
    # Subtract b from a and return the result
    return a - b

def test_subtraction():
    print(f"10 - 3 = {subtract(10, 3)}")
    print(f"5 - 8 = {subtract(5, 8)}")
    print(f"0 - 5 = {subtract(0, 5)}")

if __name__ == "__main__":
    test_subtraction()
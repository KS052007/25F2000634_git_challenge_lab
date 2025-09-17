from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide

def calculator():
    print("=== Interactive Calculator ===")
    print("Available operations: +, -, *, /")
    print("Type 'quit' to exit")
    
    while True:
        try:
            operation = input("\nEnter operation (+, -, *, /) or 'quit': ").strip()
            
            if operation.lower() == 'quit':
                print("Thank you for using the calculator!")
                break
            
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please use +, -, *, or /")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
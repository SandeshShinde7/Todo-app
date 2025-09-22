# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("\n--- Simple CLI Calculator ---")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        choice = input("Enter operation (+, -, *, /) or 'exit': ").strip().lower()

        if choice == "exit":
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("Invalid operation! Please choose from +, -, *, /.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == "+":
            result = add(num1, num2)
        elif choice == "-":
            result = subtract(num1, num2)
        elif choice == "*":
            result = multiply(num1, num2)
        elif choice == "/":
            result = divide(num1, num2)

        print(f"Result: {result}\n")

if __name__ == "__main__":
    calculator()

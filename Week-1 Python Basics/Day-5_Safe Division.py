def safe_calci():
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")
                return
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")
    except ValueError:
        print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    safe_calci()
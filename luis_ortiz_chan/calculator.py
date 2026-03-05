def calculator():
    """Simple calculator that performs arithmetic operations on two numbers."""
    
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)
    
    try:
        # Capture two numbers
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Display operation options
        print("\nSelect an operation:")
        print("1. Sum (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        operation = input("\nEnter the operation number (1-4): ")
        
        # Perform the selected operation
        if operation == "1":
            result = num1 + num2
            op_name = "Sum"
            op_symbol = "+"
        elif operation == "2":
            result = num1 - num2
            op_name = "Subtraction"
            op_symbol = "-"
        elif operation == "3":
            result = num1 * num2
            op_name = "Multiplication"
            op_symbol = "*"
        elif operation == "4":
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
                return
            result = num1 / num2
            op_name = "Division"
            op_symbol = "/"
        else:
            print("\nError: Invalid operation number. Please enter 1, 2, 3, or 4.")
            return
        
        # Display the result
        print("\n" + "=" * 40)
        print(f"Result: {num1} {op_symbol} {num2} = {result}")
        print("=" * 40)
        
    except ValueError:
        print("\nError: Please enter valid numbers.")

if __name__ == "__main__":
    calculator()

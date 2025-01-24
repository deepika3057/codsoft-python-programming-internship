# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to handle user input and operations
def main():
    print("Welcome to the Simple Calculator!")

    while True:
        # Prompt the user to input the first number
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Prompt the user to input the second number
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # Display the operations menu
        print("\nChoose the operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        # Prompt the user to select an operation
        while True:
            try:
                choice = int(input("Enter the number corresponding to the operation (1/2/3/4): "))
                if choice not in [1, 2, 3, 4]:
                    print("Invalid choice! Please select 1, 2, 3, or 4.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number (1/2/3/4).")

        # Perform the selected operation
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)

        # Display the result
        print(f"\nResult: {result}")

        # Ask the user if they want to perform another calculation
        again = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the calculator! Goodbye.")
            break

if __name__ == "__main__":
    main()

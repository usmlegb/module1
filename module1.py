# Function to perform addition
def add_numbers(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract_numbers(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    try:
        # Input two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform addition
        sum_result = add_numbers(num1, num2)

        # Perform subtraction
        subtraction_result = subtract_numbers(num1, num2)

        # Display the results
        print(f"Addition Result: {num1} + {num2} = {sum_result}")
        print(f"Subtraction Result: {num1} - {num2} = {subtraction_result}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

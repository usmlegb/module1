# Function to perform multiplication
def multiply_numbers(num1, num2):
    return num1 * num2

# Function to perform division
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Division by zero is not allowed"
    return num1 / num2

if __name__ == "__main__":
    try:
        # Input two numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform multiplication
        multiplication_result = multiply_numbers(num1, num2)

        # Perform division
        division_result = divide_numbers(num1, num2)

        # Display the results
        print(f"Multiplication Result: {num1} * {num2} = {multiplication_result}")
        print(f"Division Result: {num1} / {num2} = {division_result}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

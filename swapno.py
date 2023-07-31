def swap_numbers(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1, num2

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        print(f"Before swapping: num1 = {num1}, num2 = {num2}")

        num1, num2 = swap_numbers(num1, num2)

        print(f"After swapping: num1 = {num1}, num2 = {num2}")

    except ValueError:
        print("Invalid input! Please enter valid integers.")

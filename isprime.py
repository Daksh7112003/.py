def is_prime(number):
    if number <= 1:
        return False

    # Check for factors from 2 to the number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

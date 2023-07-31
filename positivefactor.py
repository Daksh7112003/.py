def factor(n):
    if n <= 1:
        raise ValueError("n must be greater than 1")
    
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:  # Avoid adding the same divisor twice for perfect squares
                divisors.append(n // i)
    
    divisors.sort()
    return divisors

# Example usage:
try:
    num = int(input("Enter an integer greater than 1: "))
    divisors = factor(num)
    print("The positive divisors of", num, "are:", divisors)
except ValueError as e:
    print(e)

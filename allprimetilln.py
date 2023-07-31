def isprime(lowerlimit, upperlimit):
    primes = []
    for n in range(lowerlimit, upperlimit + 1):
        if n <= 1:
            continue
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

if __name__ == "__main__":
    lowerlimit = int(input("Enter the lower limit: "))
    upperlimit = int(input("Enter the upper limit: "))
    prime_numbers = isprime(lowerlimit, upperlimit)
    print("Prime numbers between", lowerlimit, "and", upperlimit, "are:", prime_numbers)

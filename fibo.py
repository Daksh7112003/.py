def fibonacci_series(n):
    a, b = 0, 1

    for i in range(n):
        print(a)
        c = a + b
        a, b = b, c

if __name__ == "__main__":
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    fibonacci_series(n)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input(f"Enter the value of n: "))
    print(f"Factorial of {n} is {factorial(n)}")

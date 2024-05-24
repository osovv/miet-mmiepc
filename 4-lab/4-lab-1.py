import math
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)
        if d == n:
            return pollard_rho(n)
    return d

def factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    factor = pollard_rho(n)
    return factorize(factor) + factorize(n // factor)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    number = int(input("Введите число для разложения на множители: "))
    factors = factorize(number)
    print(f"Множители числа {number}: {factors}")

if __name__ == "__main__":
    main()

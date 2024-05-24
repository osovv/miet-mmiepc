import math
import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def pollard_rho_log(a, b, p):
    def f(x, c):
        return (a * x + c) % p

    x, y, d = 1, 1, 1
    c = random.randint(1, p - 1)
    for i in range(p):
        x = f(x, c)
        y = f(f(y, c), c)
        d = gcd(abs(x - y), p)
        if d != 1 and d != p:
            break
    if d == p:
        return None
    return d

def discrete_logarithm(a, b, p):
    result = pollard_rho_log(a, b, p)
    if result is None:
        print("Не удалось найти логарифм с помощью ρ-алгоритма Полларда.")
    else:
        print(f"Результат: {result}")

def main():
    p = int(input("Введите значение p: "))
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    discrete_logarithm(a, b, p)

if __name__ == "__main__":
    main()

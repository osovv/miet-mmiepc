import sympy as sp
import time

def factorize_number(n):
    start_time = time.time()
    factors = sp.factorint(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return factors, elapsed_time

def main():
    number = int(input("Введите число для разложения на множители: "))
    factors, elapsed_time = factorize_number(number)
    print(f"Множители числа {number}: {factors}")
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

if __name__ == "__main__":
    main()

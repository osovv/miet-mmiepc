import sympy as sp
import time

# :source https://github.com/sympy/sympy/blob/a44299273eeb4838beaee9af3b688f2f44d7702f/sympy/ntheory/factor_.py#L1011-L1456
# https://chatgpt.com/c/d97d3fa3-edbe-4526-8567-1e2f8843cff8

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

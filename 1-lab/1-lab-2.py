import random
import concurrent.futures
import math
import multiprocessing

# Функция для определения простого числа Ферма
def fermat_test(n, k):
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True

# Функция для определения простого числа Миллера-Рабина
def miller_rabin_test(n, k):
    if n < 4:
        return n == 2 or n == 3
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Функция для генерации простого числа в указанном диапазоне
def generate_prime_in_range(min_range, max_range, sieve):
    while True:
        prime_candidate = random.randint(min_range, max_range)
        if prime_candidate in sieve:
            continue
        if fermat_test(prime_candidate, 20) and miller_rabin_test(prime_candidate, 20):
            return prime_candidate

# Функция для генерации решета Эратосфена
def sieve_eratosthenes(n):
    sieve = set()
    primes = []
    for i in range(2, n):
        if i not in sieve:
            primes.append(i)
            for j in range(i * i, n, i):
                sieve.add(j)
    return primes

# Главная функция для генерации p и q и сохранения их в файл
def generate_keys():
    bits = 512
    min_range = 2 ** (bits - 1)
    max_range = 2 ** bits
    sieve = sieve_eratosthenes(1000)  # Генерируем решето Эратосфена
    num_workers = multiprocessing.cpu_count() * 2  # Увеличиваем количество процессов
    print("Начало генерации ключей...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_workers) as executor:
        primes = list(executor.map(lambda _: generate_prime_in_range(min_range, max_range, sieve), range(num_workers)))
    p, q = primes[:2]  # Получаем первые два простых числа из списка
    print(f"p: {p}")
    print(f"q: {q}")
    # Сохранение в файл
    with open("keys.txt", "w") as file:
        file.write(f"p: {p}\n")
        file.write(f"q: {q}\n")
    print("Ключи сохранены в файле 'keys.txt'")
    print("Генерация завершена!")

if __name__ == "__main__":
    generate_keys()

def fast_modular_exponentiation(base, exp, m):
    result = 1
    de = base % m
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % m
        exp = exp >> 1
        base = (base * base) % m
    return result

def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Введите положительное целое число.")
                continue
            return number
        except ValueError:
            print("Введено не целое число. Попробуйте еще раз.")

def main():
  base = get_positive_integer("Введите основание: ")
  exp = get_positive_integer("Введите показатель степени: ")
  m = get_positive_integer("Введите модуль: ")

  result = fast_modular_exponentiation(base, exp, m)
  print(f"Результат: {result}")

if __name__ == "__main__":
  main()

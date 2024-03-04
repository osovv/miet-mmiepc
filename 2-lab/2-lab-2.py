def find_secret(c, n, t, z):
    # Вычисляем l, так как значение n и t известны
    l = pow(2, pow(2, t), n)
    # Используем свойство XOR, чтобы найти secret
    # secret = c ^ l ^ z
    # Решив уравнение для secret, получаем:
    # secret = c ^ (l ^ z)
    # Так как XOR является обратимой, мы можем распределить операцию XOR и найти secret
    secret = c ^ l ^ z
    return secret

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


def long_time_encrypt(secret, n, t, z):
  l = pow(2, pow(2, t), n)
  c = l ^ z ^ secret
  return c, n, t, z

def main():
  c, n, t, z = long_time_encrypt(15123712, 12321315, 237456, 12356)
  secret = find_secret(c,n,t,z)

if __name__ == "__main__":
  main()

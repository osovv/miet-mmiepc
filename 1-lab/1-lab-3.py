from Crypto.PublicKey import RSA
from decimal import Decimal, getcontext
import chardet
import requests
import re

def extended_gcd(a, b):
    if b == 0:
        return 1, 0
    else:
        x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
    return x, y

def public_key_attack(n, e):
    response = requests.get(url=f'http://factordb.com/index.php?query={str(n)}')
    response_numbers = response.text.split('\n')[26].split(';')
    n = []
    for s in response_numbers[1:]:
        if 'href' in s:
            cur_n = re.sub(r"((<).*?(>))|(&.*)|(=)|(\s)", '', s)
            if cur_n != '':
                n.append(int(cur_n))

    print("Numbers:", n)
    getcontext().prec = len(str(n)) + 1
    fi = (n[0] - 1) * (n[1] - 1)
    d = extended_gcd(fi, e)[1]
    return d

def check_byte_string(byte_string):
    result = chardet.detect(byte_string)
    encoding = result['encoding']
    confidence = result['confidence']

    print("Byte string:", byte_string)
    print(f"Detected encoding: {encoding} with confidence {confidence}")

    if encoding:
        decoded_string = byte_string.decode(encoding, errors='ignore')
        print(f"Decoded string: {decoded_string}")


def main():
    with open('public.pem', 'r') as fp:
        public_key = RSA.import_key(fp.read())

    d = public_key_attack(public_key.n, public_key.e)

    with open('crypt', 'rb') as fp:
        data = fp.read()

    data = int.from_bytes(data)

    m = pow(data, int(d), public_key.n)

    byte_string = m.to_bytes(32)

    check_byte_string(byte_string)


if __name__ == "__main__":
    main()

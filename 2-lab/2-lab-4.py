from ecdsa import SigningKey, VerifyingKey, SECP256k1
import base64
import sys

def generate_keys():
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    with open('private-elg.pem', 'w') as privfile:
        privfile.write(private_key.to_pem().decode('utf-8'))
    with open('public-elg.pem', 'w') as pubfile:
        pubfile.write(public_key.to_pem().decode('utf-8'))
    print("Ключи сгенерированы и сохранены.")

def sign_message(message, private_key_path):
    with open(private_key_path, 'r') as privfile:
        private_key = SigningKey.from_pem(privfile.read())
    signature = private_key.sign(message.encode())
    return base64.b64encode(signature).decode('utf-8')

def verify_signature(message, signature, public_key_path):
    with open(public_key_path, 'r') as pubfile:
        public_key = VerifyingKey.from_pem(pubfile.read())
    signature = base64.b64decode(signature.encode('utf-8'))
    try:
        return public_key.verify(signature, message.encode())
    except:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python elgamal_cli.py <команда> <аргументы>")
        print("Команды: generate_keys, sign <сообщение> <путь к приватному ключу>, verify <сообщение> <подпись> <путь к публичному ключу>")
        sys.exit(1)

    command = sys.argv[1]
    if command == "generate_keys":
        generate_keys()
    elif command == "sign":
        if len(sys.argv) != 4:
            print("Использование: python elgamal_cli.py sign <сообщение> <путь к приватному ключу>")
            sys.exit(1)
        message = sys.argv[2]
        private_key_path = sys.argv[3]
        signature = sign_message(message, private_key_path)
        print(f"Подпись: {signature}")
    elif command == "verify":
        if len(sys.argv) != 5:
            print("Использование: python elgamal_cli.py verify <сообщение> <подпись> <путь к публичному ключу>")
            sys.exit(1)
        message = sys.argv[2]
        signature = sys.argv[3]
        public_key_path = sys.argv[4]
        is_valid = verify_signature(message, signature, public_key_path)
        print(f"Подпись верна: {is_valid}")
    else:
        print("Неизвестная команда. Используйте 'generate_keys', 'sign', 'verify'.")
        sys.exit(1)

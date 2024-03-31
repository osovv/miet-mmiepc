import rsa
import base64
import sys

def generate_keys():
    (publickey, privatekey) = rsa.newkeys(1024)
    with open('public-rsa.pem', 'w') as pubfile:
        pubfile.write(publickey.save_pkcs1().decode('utf-8'))
    with open('private-rsa.pem', 'w') as privfile:
        privfile.write(privatekey.save_pkcs1().decode('utf-8'))
    print("Ключи сгенерированы и сохранены.")

def encrypt_message(message, public_key_path):
    with open(public_key_path, 'r') as pubfile:
        public_key = rsa.PublicKey.load_pkcs1(pubfile.read().encode('utf-8'))
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    return base64.b64encode(encrypted_message).decode('utf-8')

def decrypt_message(encrypted_message, private_key_path):
    with open(private_key_path, 'r') as privfile:
        private_key = rsa.PrivateKey.load_pkcs1(privfile.read().encode('utf-8'))
    decrypted_message = rsa.decrypt(base64.b64decode(encrypted_message.encode()), private_key)
    return decrypted_message.decode('utf-8')

def sign_message(message, private_key_path):
    with open(private_key_path, 'r') as privfile:
        private_key = rsa.PrivateKey.load_pkcs1(privfile.read().encode('utf-8'))
    signature = rsa.sign(message.encode(), private_key, 'SHA-1')
    return base64.b64encode(signature).decode('utf-8')

def verify_signature(message, signature, public_key_path):
    with open(public_key_path, 'r') as pubfile:
        public_key = rsa.PublicKey.load_pkcs1(pubfile.read().encode('utf-8'))
    try:
        rsa.verify(message.encode(), base64.b64decode(signature.encode()), public_key)
        return True
    except rsa.VerificationError:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python rsa_cli.py <команда> <аргументы>")
        print("Команды: generate_keys, encrypt <сообщение>, decrypt <сообщение>, sign <сообщение>, verify <сообщение> <подпись>")
        sys.exit(1)

    command = sys.argv[1]
    if command == "generate_keys":
        generate_keys()
    elif command == "encrypt":
        if len(sys.argv) != 4:
            print("Использование: python rsa_cli.py encrypt <сообщение> <путь к публичному ключу>")
            sys.exit(1)
        message = sys.argv[2]
        public_key_path = sys.argv[3]
        encrypted_message = encrypt_message(message, public_key_path)
        print(f"Зашифрованное сообщение: {encrypted_message}")
    elif command == "decrypt":
        if len(sys.argv) != 4:
            print("Использование: python rsa_cli.py decrypt <шифрованное сообщение> <путь к приватному ключу>")
            sys.exit(1)
        encrypted_message = sys.argv[2]
        private_key_path = sys.argv[3]
        decrypted_message = decrypt_message(encrypted_message, private_key_path)
        print(f"Расшифрованное сообщение: {decrypted_message}")
    elif command == "sign":
        if len(sys.argv) != 4:
            print("Использование: python rsa_cli.py sign <сообщение> <путь к приватному ключу>")
            sys.exit(1)
        message = sys.argv[2]
        private_key_path = sys.argv[3]
        signature = sign_message(message, private_key_path)
        print(f"Подпись: {signature}")
    elif command == "verify":
        if len(sys.argv) != 5:
            print("Использование: python rsa_cli.py verify <сообщение> <подпись> <путь к публичному ключу>")
            sys.exit(1)
        message = sys.argv[2]
        signature = sys.argv[3]
        public_key_path = sys.argv[4]
        is_valid = verify_signature(message,
        signature, public_key_path)
        print(f"Подпись верна: {is_valid}")
    else:
        print("Неизвестная команда. Используйте 'generate_keys', 'encrypt', 'decrypt', 'sign', 'verify'.")
        sys.exit(1)

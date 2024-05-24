import hashlib
import matplotlib.pyplot as plt


# Функция для изменения бита в позиции pos
def flip_bit(byte_string, position):
    byte_array = bytearray(byte_string)
    byte_index = position // 8
    bit_index = position % 8
    byte_array[byte_index] ^= (1 << bit_index)
    return bytes(byte_array)


# Функция для подсчета различных битов
def count_bit_diffs(hash1, hash2):
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(hash1, hash2))

# Исходное сообщение:
message1 = b"Hello World"
len_bits1 = len(message1) * 8

md5_diffs = []
sha512_diffs = []

original_md5_hash = hashlib.md5(message1).digest()
original_sha512_hash = hashlib.sha512(message1).digest()

# Изменение каждого бита в сообщении и вычисление хэшей
for i in range(len_bits1):
    modified_message = flip_bit(message1, i)
    modified_md5_hash = hashlib.md5(modified_message).digest()
    modified_sha512_hash = hashlib.sha512(modified_message).digest()
    md5_diffs.append(count_bit_diffs(original_md5_hash, modified_md5_hash))
    sha512_diffs.append(count_bit_diffs(original_sha512_hash, modified_sha512_hash))


# Функция для изменения бита в позиции pos
def flip_bit_in_bytes(b, pos):
    byte_pos = pos // 8
    bit_pos = pos % 8
    byte_array = bytearray(b)
    byte_array[byte_pos] ^= (1 << bit_pos)
    return bytes(byte_array)

# Функция для подсчета различных битов
def count_diff_bits(hash1, hash2):
    return sum(bin(b1 ^ b2).count('1') for b1, b2 in zip(hash1, hash2))

# Исходное сообщение:



def main():
  message2 = b"Hello World!"
  len_bits2 = len(message2) * 8
  sha1_diffs = []
  sha256_diffs = []

# Изменение каждого бита в сообщении и вычисление хэшей
  for i in range(len_bits2):
      modified_message2 = flip_bit_in_bytes(message2, i)
      original_sha1_hash = hashlib.sha1(message2).digest()
      modified_sha1_hash = hashlib.sha1(modified_message2).digest()
      sha1_diffs.append(count_diff_bits(original_sha1_hash, modified_sha1_hash))

      original_sha256_hash = hashlib.sha256(message2).digest()
      modified_sha256_hash = hashlib.sha256(modified_message2).digest()
      sha256_diffs.append(count_diff_bits(original_sha256_hash, modified_sha256_hash))

    # Creating subplots
  fig, (ax1, ax2) = plt.subplots(2, 1)  # 2 Rows, 1 Column

  ax1.plot(md5_diffs, label='MD5')
  ax1.plot(sha512_diffs, label='SHA-512')
  ax1.set_xlabel('Position of Flipped Bit')
  ax1.set_ylabel('Number of Changed Bits in Hash')
  ax1.set_title('Avalanche Effect in MD5 and SHA-512')
  ax1.legend()
  ax1.grid(True)  # Adding grid

  ax2.plot(sha1_diffs, label='SHA-1')
  ax2.plot(sha256_diffs, label='SHA-256')
  ax2.set_xlabel('Position of Flipped Bit')
  ax2.set_ylabel('Number of changed bits in hash')
  ax2.set_title('Avalanche Effect in SHA-1 and SHA-256')
  ax2.legend()
  ax2.grid(True)  # Adding grid

  plt.tight_layout()  # Adjust subplots to fit into figure area.
  plt.show()

if __name__ == '__main__':
  main()

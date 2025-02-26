from Crypto.Cipher import DES
import binascii

def pad(data):
    # DES requires input to be a multiple of 8 bytes
    while len(data) % 8 != 0:
        data += b'\x00'
    return data

def des_decrypt(ciphertext, key):
    # Ensure the key is exactly 8 bytes long
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long.")

    # Create a DES cipher in ECB (Electronic Codebook) mode
    des = DES.new(key, DES.MODE_ECB)

    # Decrypt and strip padding
    plaintext = des.decrypt(ciphertext)
    return plaintext.rstrip(b'\x00')

if __name__ == "__main__":
    # Example encrypted message (in hexadecimal form)
    encrypted_hex = "5c9d4f717692d8f3"

    # Convert hex to bytes
    ciphertext = binascii.unhexlify(encrypted_hex)

    # 8-byte DES key (must match the encryption key)
    key = b"myDESkey"

    try:
        # Decrypt the message
        decrypted_message = des_decrypt(ciphertext, key)
        print(f"Decrypted message: {decrypted_message.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")

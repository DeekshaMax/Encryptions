from Crypto.Cipher import AES
import random, string, base64

# AES Key needs to be either 16, 24 or 32 bytes long. 
key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32))
# Initialization Vector needs to be 16 Bytes long.
iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))

print("\n AES Key = ", key)
print("\n Initilization Vector = ", iv )


# Encryption

enc_s = AES.new(key, AES.MODE_CFB, iv)
text = input("\nEnter the Text to be Encrypted : ")

cipher_text = enc_s.encrypt(text)
encoded_cipher_text = base64.b64encode(cipher_text)

print(encoded_cipher_text)


# Decryption

decryption_suite = AES.new(key, AES.MODE_CFB, iv)
plain_text = decryption_suite.decrypt(base64.b64decode(encoded_cipher_text))

print(plain_text)

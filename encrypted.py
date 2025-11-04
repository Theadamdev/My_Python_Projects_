#my second project in a row
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key =  chars.copy()
random.shuffle(key)

#now the encryption
message = input("enter a message to encrypt : ")
encrypted = ""
for letter in message:
    index = chars.index(letter)
    encrypted += key[index]

print(f"Your message was : {message}")
print(f"Your encrypted message is : {encrypted}")

#now the decryption
encrypted = input("enter a message to decrypt : ")
message = ""
for letter in encrypted:
    index = key.index(letter)
    message += chars[index]

print(f"Your encrypted message was : {encrypted}")

print(f"Your message is : {message}")

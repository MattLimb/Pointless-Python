#!/usr/bin/python3
#Rotary

def add_rotatory(plain_text, rot_factor=13):
    plain_text = plain_text.replace(" ", "").lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    encrypted = ""
    for x in plain_text:
        count = 0
        for i in alphabet:
            if i == x:
                count += int(rot_factor)
                if count > int(25):
                    count -= 25
                encrypted += alphabet[count]
            count += 1
    return encrypted

def remove_rotatory(encrypted, rot_factor=13):
    encrypted = encrypted.replace(" ", "").lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    plain_text = ""
    for x in encrypted:
        count = 0
        for i in alphabet:
            if i == x:
                count -= int(rot_factor)
                if count < int(0):
                    count += 25
                plain_text += alphabet[count]
            count += 1
    return plain_text

            
encrypt = input("Please Enter A Phrase to Encrypt: ")
decrypt = add_rotatory(encrypt)
plain_decrypted = remove_rotatory(decrypt)
print("Encrypted = " + decrypt)
print("Decrypted = " + plain_decrypted)
#!/usr/bin/python3
#Generate Password
import random, hashlib, binascii, time, os
from tqdm import tqdm

def generate(passwd_length=8, hash_algorithm='sha512', salt="password_salt"):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '£', '$', '%', '^', '&', '*', '@', '?']
    password = ''

    for x in range(0, passwd_length):
        if x < passwd_length:
            password += characters[random.randint(0, len(characters)-1)]

    return password, binascii.hexlify(hashlib.pbkdf2_hmac(hash_algorithm, password.encode(), str(salt).encode(), 10000, passwd_length/2)).decode('utf-8')

def imp():
    def compare(user_hash):
        c = open('passwords.txt', 'r')
        items = c.readlines()
        c.close()
        for x in items:
            file_hash_1 = x.split("\n")[0]
            file_hash = file_hash_1.split(":")[1]
            if file_hash == user_hash:
                return True
            else:
                return False
        
    user_hash = []
    user_passwd = []
    print("Generating....")
    for x in tqdm(range(0, 101)):
        user_passwds, user_hashed = generate(passwd_length=8, hash_algorithm='sha256', salt=time.time())
        if os.path.exists("./passwords.txt"):
            compare(user_hashed)
        user_hash.append(user_hashed)
        user_passwd.append(user_passwds)
        
    print("\nWriting....")
    f = open("passwords.txt", "w")
    for i in tqdm(range(0, len(user_hash))):
        f.write(str("Passwd: " + user_passwd[i] + "\n"))
        f.write(str("Stored: " + user_hash[i] + "\n\n"))
    f.close()

imp()
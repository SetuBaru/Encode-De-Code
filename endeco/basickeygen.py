import random
class Code:
    ascii_map = {i: chr(i) for i in range(128)}
    def Generatekey(self):
        keys=[]
        for i in range(0,128):
            keys.append(i)
        values=keys.copy()
        random.shuffle(values)
        encrypt_key={keys[i]: values[i] for i in range(len(keys))}
        decrypt_key={value : key for (key, value) in encrypt_key.items()}
        return encrypt_key, decrypt_key
    def encrypt(self,text,encryption):
        encoding=text.translate(encryption)
        return encoding
    def decrypt(self,text,decryption):
        message=text.translate(decryption)
        return message
keygen=Code().Generatekey()
encrypt=Code().encrypt(input("Enter Message You'd Like to encrypt:  "),keygen[0])
decrypt=Code().decrypt(encrypt,keygen[1])
print(f'Message: {decrypt}')
print(f'Encryption_key: {keygen[1]}')
print(f'Secret Message:    {encrypt}')

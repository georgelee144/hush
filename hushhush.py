from cryptography.fernet import Fernet
import getpass
import hashlib
import base64
from atomicwrites import atomic_write
import os

UTF = 'utf-8'

def make_key(passphrase):
    
    hashed_passphrase = hashlib.sha256()
    hashed_passphrase.update(bytes(passphrase,UTF))
    
    key = base64.urlsafe_b64encode(hashed_passphrase.digest())

    return key

def encode_message(message,chiper_coder):
    
    return chiper_coder.encrypt(bytes(message,UTF)).decode(UTF)

def decode_message(message,chiper_coder):
    
    return chiper_coder.decrypt(bytes(message,UTF)).decode(UTF)

if __name__ == "__main__":

    passphrase = getpass.getpass()
    key = make_key(passphrase)
    chiper_coder = Fernet(key)

    with open('new 1.txt','r') as f:
        lines = f.readlines()        

    with atomic_write('new secret.txt', overwrite=True) as f:
        
        for line in lines:
            f.write(f'{encode_message(line,chiper_coder)}')
            f.write('\n')

    with open('new secret.txt','r') as f:
        lines = f.readlines()    

    with atomic_write('new released secret.txt', overwrite=True) as f:
        for line in lines:
            f.write(f'{decode_message(line,chiper_coder)}')
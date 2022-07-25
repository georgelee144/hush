from cryptography.fernet import Fernet
import getpass
import hashlib
import base64
from atomicwrites import atomic_write

UTF = 'utf-8'

def make_key(passphrase:str)->bytes:
    """
    makes key for Fernet chiper

    Args:
        passphrase (str): password given by user

    Returns:
        bytes: a key to be used in Fernet chiper
    """
    hashed_passphrase = hashlib.sha256()
    hashed_passphrase.update(bytes(passphrase,UTF))
    
    key = base64.urlsafe_b64encode(hashed_passphrase.digest())

    return key

def encode_message(message:str,chiper_coder:Fernet)->str: 
    """
    Encrypts message from user

    Args:
        message (str): message to be encrypted
        chiper_coder (Fernet): Fernet object from cryptography library

    Returns:
        str: Encrypted str aka random gibberish
    """
    return chiper_coder.encrypt(bytes(message,UTF)).decode(UTF)

def decode_message(message:str,chiper_coder:Fernet)->str:
    """
    Decrypts message from user. 
    Function will fail if passphrase used to make the chiper_coder is not the same passphrase used to encrypt message.

    Args:
        message (str): message to be decrypted
        chiper_coder (Fernet): Fernet object from cryptography library

    Returns:
        str: plain text
    """

    return chiper_coder.decrypt(bytes(message,UTF)).decode(UTF)

if __name__ == "__main__":

    #testing random stuff

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
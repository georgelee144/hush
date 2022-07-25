# hush

This is small project that decodes a encrypted text file and displays it to the screen.
User may add more to the file and re-encrypted the text file with a new passpharse.

All Passphares/passwords are hashed using SHA256. Hashes are one way encoding.
All contents within the textfiles are encrypted and decrypted with Fernet from the cryptography library.


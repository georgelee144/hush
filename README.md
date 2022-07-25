# hush

This is small project that decodes a encrypted text file and displays it to the screen.
User may add more to the file and re-encrypted the text file with a new passpharse.

All Passphares/passwords are hashed using SHA256. Hashes are one way encoding.
All contents within the textfiles are encrypted and decrypted with Fernet from the cryptography library.

![image](https://user-images.githubusercontent.com/43113880/180674292-fa58a078-217b-4e6b-9cb3-8de6b0f77a4c.png)

You can type the message you want to display in the text box below and enter a password in the **Passphrase:** line. 

We are gonna use `This message needs to be encrypted.` in this example and for the password,
we are gonna go with `password` on this. 
Next you would write out the full file path that you wat the encrypted file to be written to.

![image](https://user-images.githubusercontent.com/43113880/180674535-da685594-f9f9-498d-bc32-c192ed61dfaa.png)

After you hit the write file button, the message will disappear and a txt file with random gibberish should appear.

`gAAAAABi3e9iW_5ecjTUdPqoauLkz_zkdoZv3NLd_royutKKP-1TEBwsFB900s2kNhuZoQVb32sxPyHRUtKc4UKVG9JUK5E7iVZtAwg-SLXXrEM4sUo7OZCu5QFUVpT7YHHIiYdoVc4Y`


You can read that message in plain text again by select the file in the top section **Read File Path:** and retype the Passphrase, `password` in this example and hitting **Read file**.

You should see your original text again




You should be careful with write button as there isn't any confirmation to write to an existing file.
The app is prone to crashing:
1. Passphrase is wrong
2. File it is suppose to read doesn't exist
3. User lacks permission to read or write from a directory

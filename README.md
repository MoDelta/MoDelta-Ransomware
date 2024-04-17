# MoDelta-Ransomware

Use of : python3 ransom.py / ransomdecrypter.py

This application encrypts the target's files and will not open them unless you provide the password. Here, the location where the password is given is shown as the target's file to prevent illegal use. If you have software knowledge, you can change this :)

It is an entry level ransomware to prevent illegal use. All responsibility is yours.

The ransom.py script encrypts files in its directory, while ransomdecrypter.py decrypts them. This simulation is designed to provide practical insights into how ransomware operates and to enhance understanding of file encryption and decryption.

Disclaimer: This code is strictly for training and development purposes. Creating, distributing, or using ransomware for malicious purposes is illegal and unethical.

Requirements : Python 3 cryptography Python library To install the required library, run: pip install cryptography

Files :

ransom.py - Encrypts files in its directory.
ransomdecrypter.py - Decrypts files encrypted by ransom.py.
generatedkey.key - Stores the encryption key (created by ransom.py).
Usage : Encryption :

Place the ransom.py script in a directory with files you wish to encrypt.
Run the script: python3 ransom.py
Encrypted files and the generatedkey.key will be generated in the same directory.
Decryption :

Ensure ransomdecrypter.py and generatedkey.key are in the same directory as the encrypted files.
Run the script: python3 ransomdecrypter.py 3 .Files will be decrypted and restored to their original state.
Important Note : Use this script only in a controlled, secure environment and never on personal, sensitive, or critical files. The author is not responsible for any misuse of this educational tool or any damage incurred.

*This software was written by learning from the lessons of instructor Atıl Samancıoğlu.

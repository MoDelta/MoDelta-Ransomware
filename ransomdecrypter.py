import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransom.py" or file == "generated.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("generated.key", "rb") as generatedkey:      #Hackers do not suddenly print the password on the target's computer, as is the case here. Normally smtp, input etc. methods deliver it to them. This is because it's for testing purposes.

    secret_key = generatedkey.read()

for file in files:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_decrypted)

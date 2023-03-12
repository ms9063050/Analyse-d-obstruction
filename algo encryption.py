import os
import pygments
from pygments.lexers import guess_lexer_for_filename
import re
import magic

var1 = 0 #variable de keyword
var2 = 0 #variable de librairies
var3 = 0 #variable de cryptage
x    = 0
temp = []

# Liste 1
keywords = ["encrypt", "key","AES","RSA","blowfish", "asymmetric","symmetric","ciphers",
            "hashes", "hash", "key", "public\-key", "private\-key"]

with open("test", 'r') as file:
    text = file.read()

for k in keywords:
    if k in text:
        if k in temp :
            print("on fout rien")
        else :
            temp [x]= k
            x= x+1
            print(f"Le mot-clé '{k}' est présent dans le fichier.")
            var1 = var1 +1  

print("Le nombre de keywords qui sont présents dans le fichier est " +var1)

# Liste 2
lexer = guess_lexer_for_filename(file)

print("Le language de programation du fichier est "+lexer.name)

lib1 = ["cryptography", "PyCrypto", "M2Crypto", "bcrypt", "passlib", "keyczar", "PyOpenSSL", 
       "paramiko", "simple-crypt", "nacl"]
lib2 = ["Bouncy Castle", "Java Cryptography Extension", "Apache Commons Crypto", "OpenSSL","Cryptacular"]
lib3 = ["OpenSSL","libsodium","GnuPG","Libgcrypt","mbed TLS"]
lib4 = ["Crypto++","Botan","libsodium","OpenSSL","Libgcrypt"]
lib5 = ["Bouncy Castle","CryptSharp","System.Security.Cryptography","OpenSSL.NET","Security.Cryptography"]

if lexer.name == "Python":
    for l in lib1:
        pattern = r"import\s+{}\s|from\s+{}\s".format(l, l)
        match = re.search(pattern, text)
        if match:
            print("La librairie {} a été trouvée dans le script".format(l))
            var2= var2 + 1

if lexer.name == "Java":
    for l in lib2:
        pattern = r"import\s+{}\s|from\s+{}\s".format(l, l)
        match = re.search(pattern, text)
        if match:
            print("La librairie {} a été trouvée dans le script".format(l))
            var2= var2 + 1
            
if lexer.name == "C":
    for l in lib3:
        pattern = r"import\s+{}\s|from\s+{}\s".format(l, l)
        match = re.search(pattern, text)
        if match:
            print("La librairie {} a été trouvée dans le script".format(l))
            var2= var2 + 1

if lexer.name == "C++":
    for l in lib4:
        pattern = r"import\s+{}\s|from\s+{}\s".format(l, l)
        match = re.search(pattern, text)
        if match:
            print("La librairie {} a été trouvée dans le script".format(l))
            var2= var2 + 1

if lexer.name == "C#":
    for l in lib5:
        pattern = r"import\s+{}\s|from\s+{}\s".format(l, l)
        match = re.search(pattern, text)
        if match:
            print("La librairie {} a été trouvée dans le script".format(l))
            var2= var2 + 1

print("Le nombre de librairies qui sont présents dans le fichier est " +var2)

# Liste 3
file.close()

def algo_crypt(test):
    
    obj = magic.Magic()

    # Obtenir le type de fichier
    file_type = obj.from_file(test)

    # Vérifier si c'est un fichier binaire
    if "executable" in file_type or "shared object" in file_type:
        # Lire les premiers octets du fichier pour détecter les chaînes de caractères
        with open(test, "rb") as file:
            data = file.read(1024) # lire les 1024 premiers octets
            if b"RSA" in data:
                print("RSA encryption detected")
                var3 = var3+1
            elif b"AES" in data:
                print("AES encryption detected")
                var3 = var3+1
            elif b"Blowfish" in data:
                print("Blowfish encryption detected")
                var3 = var3+1

print("Le nombre de cryptage qui sont présents dans le fichier est " +var3)







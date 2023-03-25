import os
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
    if k.lower() in text:
        if k.lower() in temp :
            print("on fait rien")
        else :
            temp.append(k.lower())
            x= x+1
            print(f"Le mot-clé '{k}' est présent dans le fichier.")
            var1 = var1 +1  

print("Le nombre de keywords qui sont présents dans le fichier est " +str(var1))

# Liste 2

lib1 = ["cryptography", "PyCrypto", "M2Crypto", "bcrypt", "passlib", "keyczar", "PyOpenSSL", 
       "paramiko", "simple-crypt", "PyNaCl", "Java Cryptography Extension",
         "Apache Commons Crypto", "OpenSSL","Cryptacular","libsodium","GnuPG",
         "Libgcrypt","mbed TLS","Crypto++","Botan","Libgcrypt",
         "Bouncy Castle","CryptSharp","System.Security.Cryptography","OpenSSL.NET",
         "Security.Cryptography","Fernet"]
for l in lib1:
    pattern = r"import\s+{}\s|from\s+{}\s".format(l, l)
    match = re.search(pattern, text,re.IGNORECASE)
    if match:
        print("La librairie {} a été trouvée dans le script".format(l))
        var2= var2 + 1

print("Le nombre de librairies qui sont présents dans le fichier est " +str(var2))

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
            if b"RSA-2048" in data:
                print("RSA encryption detected")
                var3 = var3+1
            elif b"AES-256" in data:
                print("AES encryption detected")
                var3 = var3+1
            elif b"Blowfish" in data:
                print("Blowfish encryption detected")
                var3 = var3+1
            elif b"RC4" in data:
                print("RCS4 encryption detected")
                var3 = var3+1
            elif b"ChaCha20" in data:
                print("ChaCha20 encryption detected")
                var3 = var3+1
            elif b"Twofish" in data:
                print("Twofish encryption detected")
                var3 = var3+1
            elif b"Triple DES" in data:
                print("Triple DES encryption detected")
                var3 = var3+1
            elif b"Serpent" in data:
                print("Serpent encryption detected")
                var3 = var3+1
            elif b"Camellia" in data:
                print("Camellia encryption detected")
                var3 = var3+1      
    print("Le nombre de cryptage qui sont présents dans le fichier est " +str(var3))

#algo_crypt()

# Evaluation du fichier 
s = var1+var2+var3*2
if s <10 :
    print ("No specific threat")
if s <60 :
    print ("Ambigous")
if s >= 60 :
    print ("Malicious")









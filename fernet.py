from cryptography.fernet import Fernet
import os
def clear():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

#Fernet.generate_key() # create key
#Fernet(key).encrypt(data) # encrypt 
#Fernet(key).decrypt(encryptedData) #decrypt

#encrypt module
def EncryptData():
    global EncryptedText
    clear()
    try:
        with open("key","rb") as keyFile:
            key = keyFile.read()
    except:
        print("""Generating new key in running directory... \nThat's saved in the "key" file. That's key is requemenents to decrypt text. \nDon't lose that!\n""")
        key = Fernet.generate_key()
        with open("key","wb") as keyFile:
            keyFile.write(key)
    textToEncrypt = input("Enter text for encrypt: ")
    clear()
    EncryptedText = Fernet(key).encrypt(textToEncrypt.encode())
    print("Your encrypted text is:\n\n")
    print(str(EncryptedText.decode()))
    print("\n")
    x = input("Click Enter to continue...")
    clear()
    ConsoleInterface()



#decrypt module
def DecryptData():
    clear()
    try:
        with open("key","rb") as keyFile:
            key = keyFile.read()
    except:
        print(""" First enter "key" file in your running directory. """)
        x = input("Click Enter to continue...")
        clear()
        ConsoleInterface()
    textToDecrypt = input("Enter text for decrypt: ")
    clear()
    DecryptedText = Fernet(key).decrypt(textToDecrypt.encode())
    print("Your decrypted text is:\n\n")
    print(str(DecryptedText.decode()))
    print("\n")
    x = input("Click Enter to continue...")
    clear()
    ConsoleInterface()


def PrintLocalKey():
    clear()
    with open ("key","rb") as file:
        print(str(file.read().decode()))
        print("\n")
        x = input("Click Enter to continue...")
        clear()
        ConsoleInterface()

def RegenerateKey():
    clear()
    with open("key","wb") as file:
        file.write(Fernet.generate_key())
    print("Done!")
    x = input("Click Enter to continue...")
    clear()
    ConsoleInterface()
#console interface
def ConsoleInterface():
    global textAlert
    print("Welcome to this program. This program is going to encrypt or decrypt your text!")
    print("1.Encrypt \n2.Decrypt \n3.Check local key\n4.Regenerate key\n5.Exit\n")
    UserChoice = input(textAlert+"\n: ")
    textAlert="Enter number to continue"
    if UserChoice=="1":
        EncryptData()
    elif UserChoice=="2":
        DecryptData()
    elif UserChoice=="3":
        PrintLocalKey()
    elif UserChoice=="4":
        RegenerateKey()
    elif UserChoice=="5":
        clear()
        exit()
    else:
        clear()
        textAlert = "Wrong number selected! Try again!"
        ConsoleInterface()




















textAlert="Enter number to continue"
ConsoleInterface()

import encryptFile
import decryptFile
import generateAKey
import os

username="abcd"
password="kjsce"


def login():
    user=input("\nUsername : ")
    passw=input("Password : ")
    
    if user==username and passw==password:
        return 1
    else:
        return 0

def main():
    while (True):
        choice=int(input("\n1. Login\n2. Exit\n3. Update\n4. Help, credit & about. \n\tEnter choice - "))
        if choice==1:
            if login():
                generateAKey.gen_key()
                encryptFile.encryp()
                decryptFile.decryp()
            else:
                print("\nInvalid login")
                continue
        elif choice==0:
            print("Thank you!")
            os.remove('encrypted_file.txt')
            os.remove('SecretKey.key')
            break

if __name__=="__main__":
    main()
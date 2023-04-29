import hashlib
import pyautogui
import os

os.system("figlet HASHCRACKER")

HASH = str(input('wpisz hasz md5: '))

hasla = str(input('wpisz ścieżkę do pliku: '))

print("\n")

a = int(input("wybierz tryb: 1.cichy (działa w tle) \n 2. wyświetla wszystkie hasze \n : "))

if a == 1:

	with open(hasla , 'r') as file:
		for line in file.readlines():
			hash_object = hashlib.md5(line.strip().encode('utf-8'))
			hashed_word = hash_object.hexdigest()
			if hashed_word == HASH:
				print("\n złamane, hasło to: " + line.strip())
				break
				os.system("exit")

		
else:



	with open(hasla , 'r') as file:
		for line in file.readlines():
			hash_object = hashlib.md5(line.strip().encode('utf-8'))
			hashed_word = hash_object.hexdigest()
			print(hashed_word)
			if hashed_word == HASH:
				print("\n złamane, hasło to: " + line.strip())
				break
				os.system("exit")
			else:
				print("niezgodność")
		


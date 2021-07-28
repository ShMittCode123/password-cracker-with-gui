import hashlib
from tkinter import *

root = Tk()
root.title('PasswordCracker V 1.20')
root.geometry('970x168')


hashed_password = StringVar()
guess_password_file = StringVar()

def crack_password():

	password_found = False

	hashed_password_input = hashed_password.get()
	guess_password_file_input = guess_password_file.get()

	try:
		global password_file
		password_file = open(guess_password_file_input)
	except:
		file_not_found_error = Label(root, text = '[-] File not found', font = ('Arial', 12, 'bold'))
		file_not_found_error.grid(row = 5, column = 3)

	for word in password_file:

		enc_word = word.encode('utf-8')
		hashed_word = hashlib.md5(enc_word.strip())
		digest = hashed_word.hexdigest()

		if digest == hashed_password_input:
			password_found_label = Label(root, text = '[+] Password found. Password is {}'.format(word), font = ('Arial', 12, 'bold'))
			password_found_label.grid(row = 5, column = 3)
			password_found = True

	if password_found == False:
		password_not_found_label = Label(root, text = '[-] Password not found', font = ('Arial', 12, 'bold'))
		password_not_found_label.grid(row = 5, column = 3)

hashed_password_label = Label(root, text = 'Enter hashed password: ', font = ('Arial', 15, 'bold'))
hashed_password_input = Entry(root, textvariable = hashed_password, font = ('Arial', 11), width = 75)

guess_password_file_label = Label(root, text = 'Enter guessed-passwords file path: ', font = ('Arial', 15, 'bold'))
guess_password_file_entry = Entry(root, textvariable = guess_password_file, font = ('Arial', 11), width = 75)

crack_password_button = Button(root, text = 'Crack Password', command = crack_password, width = 12, height = 1, font = ('Arial', 12))

hashed_password_label.grid(row = 1, column = 2)
hashed_password_input.grid(row = 1, column = 3, pady = 15)

guess_password_file_label.grid(row = 3, column = 2)
guess_password_file_entry.grid(row = 3, column = 3, pady = 15)

crack_password_button.grid(row = 5, column = 2)

root.mainloop()

import string
import random

letters_list = list(string.ascii_letters)
symbols_list = list(string.punctuation)
numbers_list = list(string.digits)

print("Welcome to the password generator!")
letters = int(input("How many letters would you like in your password: "))
symbols  = int(input("How many symbols would you like: "))
numbers = int(input("How many numbers would you like: "))

password_list = []
for char in range(0,letters):
	password_list += random.choice(letters_list)
for char in range(0,symbols):
	password_list += random.choice(symbols_list)
for char in range(0,numbers):
	password_list += random.choice(numbers_list)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
	password += char

print("Your password is " + password)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
              'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

xarf = int(input("Parolingizda nechta xarf bolishini hohlaysiz: \n"))
raqam = int(input("Parolingizda nechta raqam bolishini hohlaysiz: \n"))
belgi = int(input("Parolingizda nechta belgi bolishini hohlaysiz: \n"))


for char in range(1, xarf + 1):
    password_list.append(random.choice(letters))

for char in range(1, raqam + 1):
    password_list += random.choice(numbers)

for char in range(1, belgi + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(f"Sizning yangi parolingiz - {password}")

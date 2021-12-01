import random

# CREAR UNA FUNCIÓN




letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) #5
nr_symbols = int(input(f"How many symbols would you like?\n")) #2
nr_numbers = int(input(f"How many numbers would you like?\n")) # 1
# Password: abcde()2
# Si quieres crear una lista debes dejar un espacio entre los corchetes.
p, q, r=[ ], [ ], [ ]
for i in range(0, nr_letters):
    ss1=random.randint(0, len(letters)-1)
    p+=letters[ss1]
for i in range(0, nr_symbols):
    ss2=random.randint(0, len(symbols)-1)
    q+=symbols[ss2]
for i in range(0, nr_numbers):
    ss3=random.randint(0, len(numbers)-1)
    r+=numbers[ss3]
# También se podría usar la misma lista para agregar más términos
Password=p+q+r
# Usamos la función .shuffle() para barajear la lista o para cambiar aleatoriamente las posiciones de los valores.
# random.shuffle(Password)
# for i in Password:
#     # Usamos end="" para indicarle el espacio de diferencia entre valor y valor de un LISTA.
#     print(i, end="")

# append() and random.choice()
random.shuffle(Password)
str_password=""
for i in Password:
    # "i" nos imprime el valor que tiene esa posición.
    str_password+=i 
print(f'Tu contraseña es: {str_password}')


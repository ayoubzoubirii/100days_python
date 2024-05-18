#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
total = nr_symbols + nr_letters + nr_numbers


password = [] 
password_code = ""

# random letters

for x in range(0,nr_letters):
    password.append(random.choice(letters))

# random numbers
    
for y in range(0,nr_numbers):
    password.append(random.choice(numbers))

# random symbols
        
for z in range(0,nr_symbols):
    password.append(random.choice(symbols))

# shuffle change all position in indexs

random.shuffle(password)


for passwor in password :
    password_code += passwor


print(password_code)



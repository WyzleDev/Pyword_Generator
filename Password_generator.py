import os
import random
chars = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

number = int( input(" Enter number of passwords > ") )
length = int(input(" Enter length of password > "))

for x in range(number):
    password = ''

    for i in range(length):
        password += random.choice(chars)

    print(password)

    file = open('password.txt', 'a')
    file.write('\n' + password)
    file.close()


os.system('pause')


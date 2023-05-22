import random  #importing random package

print("welcome to razma password generator")

passlength = int(input('Enter length of password')) #takes length as input

s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_*$" #LONG ASS CHARACTERS XD to create a random password

password = "".join(random.sample(s,passlength)); #generates random password

print(password); 

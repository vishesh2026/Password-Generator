import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*_"
while True:
    pass_length = int(input("enter the length of required password : "))
    pass_count = int(input("enter the number of required  password : "))
 
    for i in range (0, pass_count):
        password= ""
        for j in range (0, pass_length):
            pass_char = random.choice(characters)
            password = password + pass_char
        print("The generated password is",password)
    repeat = input("Do you wanat to generate more passwords :")
    if repeat =="no" or repeat == "No":
        break
print("Thank you")


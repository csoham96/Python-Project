import string
import random
#Intializing lists with different charecters required
special_chars=["!","@","#","$","%","^","&","*","?",":"]
numbers = [str(x) for x in range(10)]
lower_case=list(string.ascii_lowercase)
upper_case=list(string.ascii_uppercase)
MIN_LENGTH=8
MAX_LENGTH=15
def gen_password():   
    #One special charecter
    #One upper case
    #One Lower case
    #One number
    #min length will be 8
    #max length will be 15
    
    #concatinating all the chars into a single string
    chars=special_chars+numbers+lower_case +upper_case
    #Shuffle the strings
    random.shuffle(chars)
    #Taking one special char
    gen_password=random.choice(special_chars)
    #Taking one number
    gen_password+=random.choice(numbers)
    #Taking one lower case

    gen_password+=random.choice(lower_case)

    #Taking one upper case
    gen_password+=random.choice(upper_case)

    gen_password=list(gen_password)

    gen_password += [random.choice(chars) for x in range(random.randint(MIN_LENGTH-4,MAX_LENGTH-4))]
    return "".join(gen_password)

while True:
    x=input("Press key any key to gen password or q to exit")
    if x=='q':
        break
    else:
        print(gen_password())
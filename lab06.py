#This is done by Adam Magoulas
def encoder(code, encryption):
    code = str(code)
    code_list = list(code)
    index = 0
    for char in code_list:
        char = int(char)
        char += encryption
        code_list[index] = char
        index+=1
    encrypted_code_list = ''
    for i in code_list:
        encrypted_code_list += str(i)
    return (encrypted_code_list)

#This is done by G Shashank
def decoder(code, numbertoberemoved):
    decodedstring = ""
    code = str(code)
    for i in code:
        decodednumber = int(i) - numbertoberemoved
        if decodednumber < 0:
            finalnumber = 10 + decodednumber
            decodedstring += str(finalnumber)
        else:
            decodedstring += str(decodednumber)

    return decodedstring



if __name__ == "__main__":
    '''
    #This takes in a user input
    enc = int(input("What value would you like to use to encrypt your password: "))
    print(encoder(1234555, enc))'''

    y = decoder(45678888, 3)
    print(y)

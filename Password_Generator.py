#Password Generator

import random
def HowManyPasswords():

    PasswordAmount = raw_input('how many passwords do you want to generate? ')
    Amount = ErrorChecking(PasswordAmount,'Amount')

    return Amount

def ErrorChecking(String_Input,Which_One):
    bad_word = False

    for i in range(0,len(String_Input)):

        if bad_word == True:
            pass
        if (ord(String_Input[i]) > 57 or ord(String_Input[i]) < 48):
            print 'The inputted amount was not a number. \n 1 password will be printed'
            bad_word = True
            Result = 1

    if bad_word == False:
        Result = int(String_Input)

    if Which_One == 'Length':
        if Result > 50 or Result < 0:
            print('The length can not be greater than 50 or less than 0')
            print('The length was set to 10')
            Result = 10

    return Result

def WhatLength():
    print('inputting a 0 or below will use the default length 10')
    Length_Input = raw_input('What length would you like your password to be? ')
    Length = ErrorChecking(Length_Input,'Length')

    return Length

def GeneratePasswords(Amount,Length):
    for i in range(0,Amount):
        password = random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",Length)
        print i+1,':',''.join(password)

if __name__ == '__main__':
    Amount = HowManyPasswords()
    Length = WhatLength()
    GeneratePasswords(Amount, Length)

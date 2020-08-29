#!/usr/bin/env python3
import random
while True:
    def random_number(inp,inp2,inp3):
        number = random.randrange(inp,inp2)
        while True:
            if inp3 < number :
                print('The number entered is less than the number choosed by the computer')
                inp3  = int(input("Enter the number again:"))
                if inp3 < number :
                    print('The number entered is less than the number choosed by the computer')
            if inp3 > number :
                print('The number entered is greater than the number choosed by the computer')
                inp3  = int(input("Enter the number again:"))
                if inp3 > number :
                    print('The number entered is greater than the number choosed by the computer')
            if inp3 == number :
                print("Wow!You've found the answer")
                break

    choice = int(input("From which number do you want to start from: "))
    choice2 = int(input("Which number do you want to be maximum number: "))
    print('\nThe number has been choosed')
    choice3 = int(input("Enter the number you think is the number choosed: "))
    random_number(choice,choice2,choice3)

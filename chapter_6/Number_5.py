'''
Solution to pythonbookHalterman.
Chapter 6, no. 5.

Last updated: 27/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''

# A Game Program that allows a user to guess
# the computer's values in determined
# number of trials

import random
import math

print('Play the game to guess the computer\'s value.')
print('HINT: COMPUTER\'S VALUE IS BETWEEN 1 AND 100 INCLUSIVE')
print()
computer_value = random.randint(1, 100)
trials = int(input('How many times do you want to guess? '))
print()
attempts = trials
   
for n in range(trials):
    msg1 = 'You have ' + str(attempts - 1) + ' attempts left'
    msg2 = 'You have ' + str(attempts - 1) + ' attempt left'
    msg = msg1 if(attempts - 1 > 1) else msg2

    choice = eval(input('Enter guess ' + str(n + 1) + ': '))
    if (choice == computer_value):
        print('AWESOME! COMPUTER\'S VALUE IS', computer_value)
        print('YOU GUESSED THE COMPUTER\'S VALUE IN '\
              + str(n + 1) + ' moves')
        break
    elif(0 < math.fabs(choice - computer_value) <= 5):
        print('YOUR GUESS IS VERY CLOSE! ', end='')
        if(choice > computer_value):
            print('BUT GREATER THAN COMPUTER\'S VALUE')
        else:
            print('BUT LESSER THAN COMPUTER\'S VALUE')
        print(msg)
    elif(5 < math.fabs(choice - computer_value) <= 10):
        print('YOUR GUESS IS CLOSE! ', end='')
        if(choice > computer_value):
            print('BUT GREATER THAN COMPUTER\'S VALUE')
        else:
            print('BUT LESSER THAN COMPUTER\'S VALUE')
        print(msg)
    else:
        print('YOUR GUESS IS FAR! ', end='')
        if(choice > computer_value):
            print('AND GREATER THAN COMPUTER\'S VALUE')
        else:
            print('AND LESSER THAN COMPUTER\'S VALUE')
        print(msg)
    attempts -= 1
    print()
if(choice != computer_value):
    print('***GAME OVER***')
    print()
    print('COMPUTER\'S VALUE IS', computer_value)
    print('Rerun program to play again')
    
                        
                        

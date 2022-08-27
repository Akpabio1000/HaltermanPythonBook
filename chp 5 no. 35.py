'''
Solution to pythonbookHalterman.
Chapter 5, no. 35.

Last updated: 1/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''

sum = 0
count = 0
value = float(input('Enter number, negative number terminates program: '))

if value >= 0:  
    sum += value
    max = min = value
    count += 1

while value >= 0:
    value = float(input('Enter next number, negative number ends program: '))
    if value >= 0:
        sum += value        #Accumulates the sum of all values entered
        count += 1
        if value > max:
            max = value     #Maximum value I have seen thus far
        if value < min:
            min = value     #Minimum value I have seen thus far

if count > 0:       #if a negative value is entered first, nothing is printed
    print('Sum =', sum)
    print('Average =', sum/count)
    print('Maximum value =', max)
    print('Minimum value =', min)

                        
    
                        
                        

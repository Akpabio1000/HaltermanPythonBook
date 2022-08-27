'''
Solution to pythonbookHalterman.
Chapter 5, no. 35.

Last updated: 1/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''

sum = 0
value = float(input('Enter digit 1: '))
sum += value
max = min = value
for n in range(2, 21):
    value = float(input('Enter digit ' + str(n) + ': '))
    sum += value        #Accumulates the sum of all values entered
    if value > max:
        max = value     #Maximum value I have seen thus far
    if value < min:
        min = value     #Minimum value I have seen thus far
    
print('Sum =', sum)
print('Average =', sum/n)
print('Maximum value =', max)
print('Minimum value =', min)

                        
    
                        
                        

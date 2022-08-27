'''
Solution to pythonbookHalterman.
Chapter 6, no. 4.

Last updated: 27/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''

# Program that compute the hypotenuse
# when given adjacent and opposite
# of a right angled triangle

from math import sqrt

adjacent = eval(input('Enter adjacent value: '))
opposite = eval(input('Enter opposite value: '))

hypotenuse = sqrt(adjacent**2 + opposite**2)

print('Hypotenuse =', hypotenuse)

                        
                        

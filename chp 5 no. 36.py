'''
Solution to pythonbookHalterman.
Chapter 5, no. 36.

Last updated: 1/08/2022
Author: Akpabio Emmanuel
email: akpabio15@gmail.com
'''


star = int(input('Enter value: '))
for n in range(1, star + 1):
    for m in range(n):
        print(end='*')
    print()
for n in range(1, star):
    for m in range(star - n):
        print(end='*')
    print()
print()
                        
                        

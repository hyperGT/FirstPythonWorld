# create an algorithm that reads a number and outputs its double, triple and square root.
import math

n = int(input('Enter the number: '))

double = n**2
# or math.pow(n, 2)
triple = n**3
# math.pow(n, 3)
sq_r = n**(1/2)
# math.sqrt(n)


print('\n' + '-'*20)
print('\n Entered number: {} \n Double {}'.format(n, double), end=' ')
print('\n - \n Triple: {} \n Square Root: {}'.format(triple, sq_r))






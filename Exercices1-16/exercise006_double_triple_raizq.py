# create an algorithm that reads a number and outputs its double, triple and square root.
import math

n = int(input('Enter the number: '))

double = n*2
triple = n*3
sq_r = math.sqrt(n)


print('\n' + '-'*20)
print('\n Entered number: {} \n Double: {}'.format(n, double), end=' ')
print('\n Triple: {} \n Square Root: {}'.format(triple, sq_r))






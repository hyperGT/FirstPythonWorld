variable = input('digite algo: ')

print('what is the type?', type(variable))
print('is a numeric? ', variable.isnumeric())
print('is a alphanum? ', variable.isalnum())
print('is a string? ', variable.isalpha())
print('is a lower case?', variable.islower())
print('is a upper? ', variable.isupper())

# Arithim Operators
n1 = 5
n2 = 2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
r = n1 % n2

s = n1 + n2
sub = n1 - n2

print('\n-' * 5)
print('\n multiplicação {} \n divisão {:.2f} \n div inteira {} \n potencia {} \n resto {}'.format(m, d, di, p, r),
      end=' ')
print('\n soma {} \n subtração {}'.format(s, sub))

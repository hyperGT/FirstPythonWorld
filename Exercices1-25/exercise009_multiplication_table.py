# multiplication table program

print('-'*40 + '\n Multiplication table')
n = int(input(' Enter the number: '))

print('\n' + '-'*10)
i = 0
while i <= 10:
    r = n * i
    print(f'{n} x {i} = {r}')
    i += 1
print('-'*12)



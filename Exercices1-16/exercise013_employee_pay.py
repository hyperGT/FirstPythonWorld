# Make an algorithm that reads a employee pay amd show the new payment value, with 15% increase

payment = int(input('Enter the employee pay: '))
pay_raise = 15  # tradução: aumento de pagamento

new_salary = (payment * ((pay_raise / 100) + 1))

print(new_salary)

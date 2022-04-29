# Building a A Basic Calculator

# Collect Three inputs from the User
# Add, Subtract, Multiple 
# Two numbers together

# Input
# Define variables and assign values
num1 = int(input('Enter first number:'))
num2 = int(input('Enter Second number:'))
op = input('Enter Operator')


# Process
if op == '+':
    print('The addition is: ',num1+num2)

elif op == '-':
    print('The substraction is: ',num1-num2)

elif op == '*':
    print('The Multiplication is equals: ',num1*num2)

elif op == '/':
    print('The Division is ',num1/num2)

else:
    print('Invalid Operator')
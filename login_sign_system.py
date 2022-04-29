# Program Name:Login and Sign-up System
# Date: 04/29/2022
#
"""
    Program request user to create username and password
    to create account.  

    Following variables will be generated:
    1.username
    2.password
    3.username2
    4.password2 
"""

# Display welcome message to new user 
print('\nWelcome to our page!')
print('\nPlease create a new account')

# Prompts User to create credentials
username = input('Enter username: ')
password = input('Enter Password: ')

# Informs User account was created
print('The account has been created successfully!')
print('Please Login:')

# Requests User to type new credentials for-
# authentication
username2 = input('Please Enter Username: ')
password2 = input('Enter password: ')

# if statement checks for both conditions to be True or
#  equivalent
if username == username2 and password == password2:
    print('Logged in approved!')
else:
    print('Invalid credentials. Try Again!')

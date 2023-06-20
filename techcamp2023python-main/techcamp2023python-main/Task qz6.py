# TASK 6:Using Python Only
# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After ,you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.

attempts = 0

while attempts <=4:
    password = input('Enter your password: ')

    if password == 'admin123':
        print('Access granted!')
        
    else:
        print('Account Locked')
        attempts += 1
        

#soln2
for i in range(4):
 if password == 'admin123':
        print('Login successful!')
        break
 else:
    print('Invalid username and password, Account Locked!')
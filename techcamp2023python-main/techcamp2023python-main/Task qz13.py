# TASK 13: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a function.


# soln1

username = input('Enter Email Address: ')
password = input('Enter your password: ')

if username == 'admin@mail.com' and password == 'admin123':
        print('Login successful!')
      
        
else:
    print('Invalid username and password, Account Locked!')
       


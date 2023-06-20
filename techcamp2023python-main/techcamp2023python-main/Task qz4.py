# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it contains an “@” symbol and “.” symbol. 
# Hint: In Python you can use logical operators to solve this.
# Once you learn functions,revisit this and write this code inside a function.


# import re
# def validate_email(email):  
#     if re.match(r"[^@]+@[^@]+\.[^@]+", email):  
#         return True  
#     return False  

# email= input("Enter you email address: ")
# #wairiemail = "example@domain.com"  
# if validate_email(email):  
#     print("Valid email address")  
# else:  
#     print("Invalid email address")  

email=input ('Enter your email address: ')
if email.count('@')==1 and email.count('.')==1:
    print('valid email address')
else:
    print ('invalid email address')

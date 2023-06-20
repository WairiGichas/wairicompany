# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01... Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
# Once you learn functions,revisit this and write this code inside a function.

phone =str(input('Enter phone number: '))
if str('+254') in phone[0:4]:
    print ('valid')
elif str('07') in phone[0:2]:
    phone=phone[1:]
    print ('+254'+(phone))
elif str('01') in phone [0:2]:
    phone=phone[1:]
    print ('+254'+(phone))
elif str ('7') in phone [0:1]:
    phone=phone[1:]
    print ('+254'+(phone))


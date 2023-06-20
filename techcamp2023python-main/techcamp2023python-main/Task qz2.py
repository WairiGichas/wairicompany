# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
# Extras:

# Once you learn functions,revisit this and write this code inside a function.

num = int(input ("Enter any number to test whether it is odd or even: "))
if num % 2 == 0 and num %4 == 0:
    print ("Divisble by 4")
elif num % 2 == 0 and num %4 != 0:
        print ("even")
else:
        print("odd")

#               print ("The number is even")
# else:
#               print ("The provided number is odd")
                     
# # If the number is a multiple of 4, print out “divisible by 4”.

# if (num ** 4) == 0:
#         print("The number is divisible by 4")
# else:
#      print("The number is not divisible by 4, try again")
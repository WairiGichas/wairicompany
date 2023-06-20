# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars.py. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.
# Once you learn functions,revisit this and write this code inside a function.


num_of_rows = int(input("Enter the number of rows: "))

for i in range(0, num_of_rows):#this will handle the number of rows

    for j in range(0, i + 1): #to handle number of columns and values is changing according to j
            
        print("* ", end=" ") # to print stars
    print()# will print line after each row
 

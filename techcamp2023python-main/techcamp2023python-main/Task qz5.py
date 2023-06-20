# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 

num1=int(input("Enter 1st num: "))
num2=int(input("Enter 2nd num: "))
num3=int(input("Enter 3rd num: "))

if num1> num2 and num1 > num3:
    print (num1)
else:
    if num2 > num1 and num2 > num3:
        print (num2)
    else:
        if num3 > num1 and num3 > num1:
            print (num3)
        else:1
        print("Invalid entry")
        


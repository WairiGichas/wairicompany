# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.

num1=int(input("Enter 1st num: "))
num2=int(input("Enter 2nd num: "))
num3=int(input("Enter 3rd num: "))
num4=int(input("Enter 4th num: "))

if num1> num2 and num1 > num3 and num1 > num4:
    print (num1)
else:
    if num2 > num1 and num2 > num3 and num2 > num4:
        print (num2)
    else:
        if num3 > num1 and num3 > num1 and num3 > num4:
            print (num3)
        else:
            if num4 > num1 and num4 > num2 and num4 > num3:
                print (num3)
            else:
                print("Invalid entry")
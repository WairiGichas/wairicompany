# TASK 7: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
try:
    marks = int(input("Enter marks: "))

    if marks <0 or marks >100:
        print("Marks captured are off scale!!")
    else:
        if marks >= 79:
            print ("A")
        else:
            if marks >=60 and marks <79:
                print ("B")
            else:
                if marks >= 59 and marks < 49:
                    print ("C") 
                else: 
                    if marks >=40 and marks < 49:
                        print ("D")
                    else:
                        print("E")

except Exception as Error:
    print("Error while entering marks!!")





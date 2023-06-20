# # average_marks = 70
# # if (average_marks > 50) and (average_marks < 100):
# #      # This runs if it is true
# #            print("Pass") 
# # else:
# # 				   #This runs if it is false
# #                        print("Fail")

# if 5 <6:
#         print ("true") #the blocks should be aligned
#         print("also when true")
#         print("also when tru")
# else:
#         print("false")
# print("either way") # this block is read outside the if else block because its not in line with the lest of print block

# #Take user input and ask them for their marks. Print their grade.
#  average_marks= 70
# if average_marks  >= 70:
# 		 print("A")
# elif average_marks  >= 60 and average_marks  < 70:
# print("B")
# elif average_marks  >= 50 and average_marks  < 60:
#  		print("C")
# elif average_marks  >= 40 and average_marks  < 50:
#     		print("D")
# else:
#  print("E")

# #Take user input and ask them for their marks. Print their grade.
try:
    mrks=int(input("Enter your Marks: "))
    if mrks < 0 or mrks > 100:
        print ("mrks!")
    else:
        if mrks  >= 70:
            print("A")
        else:
            if mrks  >= 60 and mrks  < 70:
                print("B")
            else:
                if mrks  >= 50 and mrks  < 60:
                    print("C")
                else:
                    if mrks  >= 40 and mrks  < 50:
                        print("D")
                    else:
                        print("E")
# except: 
# print ("Enter the correct datatype")                     
except Exception as Error:
    print("Error")

#Take input from user requesting for marks. print their grade
#>= 70 is A
#>= 60 and < 70 is B
#>= 50 and < 60 is C
#>= 40 and < 50 is D
#< 40 is E

# marks=int(input("Enter your Marks: "))

#  if marks < 40:
#     print("E")
# elif marks >= 40 and marks < 50:
#     print ("D")
# elif marks >= 50 and marks < 60:
#     print ("C")
# elif marks >=60 and marks< 70:
#     print ("B")  
# else:
#     print ("A")


# # Qn 1. Take three numbers from a user and return the largest of the three
# fir= int(input('Enter first number : ')) 
# sec= int(input('Enter second number : ')) 
# thir = int(input('Enter third number : ')) 

# if fir_num > sec_num and fir_num > thir_num: 
#     print("fir")
# largest = sec_num 
# if sec_num  > fir_num and sec_num  > thir_num: 
# largest = thir_num 
# if thir_num  >fir_num and thir_num > sec_num: 
# else
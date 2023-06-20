# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  

basic_salary=int(input("Enter your basic Salary: "))
benefits=int(input("Enter your benefits figure: "))

gross= basic_salary + benefits
if gross>= 100000:
    print ("NHIF is Ksh 1700")
else:
    if gross >= 90000 and gross <99999:
        print ("NHIF is Ksh 1600")
    else:
        if gross >= 80000 and gross <89999:
            print ("NHIF is Ksh 1500")
        else:
            if gross >= 70000 and gross <79999:
                print ("NHIF is Ksh 1400")
            else:
                if gross >= 60000 and gross <69999:
                    print ("NHIF is Ksh 1300")
                else:
                    if gross >= 50000 and gross <59999:
                        print ("NHIF is Ksh 1200")
                    else:
                        if gross >= 45000 and gross <49999:
                            print ("NHIF is Ksh 1600")
                        else:
                            if gross >= 40000 and gross <44999:
                                print ("NHIF is Ksh 1600")
                            else:
                                print("No montly contributions to make")



                                
# TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
# Once you learn functions,revisit this and write this code inside a function.

# age = input("Enter your data of birth: ")
# from datetime import date
 
# def calculateAge(birthDate):
#     today = date.today()
#     age = today.year - birthDate.year -((today.month, today.day) < (birthDate.month, birthDate.day))
 
#     return age
     

# print(age)
 
# from datetime import date
# months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,12:31}

# def leap_year1 (year):# this fxn will check whether the year is a leap year or not
#     if year %4 ==0:
#         if year % 100 == 0:
#             if year % 400 ==00:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# def num_of_days (date1, date2):# this returns the diffrence of two dates in days
#     return (date2 - date1).days

# day1, mon1, year1 = input('Enter you date of birth in dd/mm/yyyy format: ').split('/')
# day2, mon2, year2 = input('Enter the current year in dd/mm/yyyy format: '). split('/')

# #converting dates intp date format
# date1=date(int(year1), int(mon1), int(day1))
# date2=date(int(year2), int(mon2), int(day2))

# #return value for mthe fxn- num_of_days
# total_days= num_of_days(date1, date2)

# #if birth year and current year is the same
# if int(year1) == int (year2):
#     month = total_days/30
#     day =total_days%30
#     year = 0
# else:
#     year =total_days/365
#     month= (total_days%365)/30

    
#     #checking whetehr the given year is leap year or not
#     #if so, make the total number of days in the month of february  29th instead of 28
#     if leap_year1(int(year1)):
#         months[2] =29

#  # if the current month is february and the current year is 

#     if  int (day2) == int(day1):
#         day = int(day2 )- int (day1)


#     elif int(mon2) == 2 and (leap_year1) or (not leap_year1(int(year2))):
#         year = year - 1
#         month =11

#         pre_month =months[int(mon2) -1]
#         days = pre_month - int(day1) + int(day2)
#         day =days

#     else:
#         pre_month =months[int(mon2) -1]
#         days =pre_month - int(day1) + int(day2)
#         day =days

# print("YOUR Age is: ",int(year), "years", int(month), "months", int(day), "days")

#soln 2
mydob = input("Enter DOB(dd-mm-yyyy): ").split("-")
mydobnew =[]

for i in mydob:
    mydobnew.append(int(i))
mydob = mydobnew

if len(mydob) !=3 or mydob[0] >1 or mydob[0] > 31 \
or mydob[1] <1 or mydob[1] > 12 or mydob[2] > 2023 \
or len(str(mydob[2])) !=4 or (mydob[1]== 2 and mydob[0] > 29)\
or (mydob[1] == 2 and mydob[0] > 28 and mydob[2] % 4 ! =0) \
:
    
    print ("invalid date")
else:
    print(mydob)







# DOB= int(input('Enter date of birth in dd-mm-yyyy format: '))
# today=date.today()
# age=today-DOB
# days=age.days
# months=int((days/365)*12)
# years=int(days/365)

# print(f'Years', {years})
#       #, 'Months', months, 'Days', days)


# DOB = date(1999, 8, 7)
# today = date.today()
# time_difference = today - DOB
# D = time_difference.days
# M = int((D/365)*12)
# Y = int(D/365)
# print(f"Years: {Y}")
# print(f"Months: {M}")
# print(f"Days: {D}")
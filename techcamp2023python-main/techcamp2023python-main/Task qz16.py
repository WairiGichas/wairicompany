# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using THIS LINK:  

# Once you learn functions,revisit this and write this code inside a function.

#NSSF function:
def calculate_nssf(salary, benefits):
    salary = float(input("Enter salary: "))
    benefits = float(input("Enter benefits: "))
    grosss_salary = salary + benefits
    nssf_rate = 0.06 
    max_deductible_nssf = 18000
    nssf = min((grosss_salary * nssf_rate), max_deductible_nssf)

    return (nssf)
nssf = calculate_nssf("salary", "benefits")
print("NSSF =", nssf)
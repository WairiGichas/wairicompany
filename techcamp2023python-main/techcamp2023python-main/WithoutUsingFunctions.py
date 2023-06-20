# Write a normal python program that calculates the total marks from:
# maths = 70
# maths = 70
# eng=  60
# swa = 74
# sci = 65
# sos = 78
# on the same program, the average marks ,then use the average to find the grade using the table below:
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

##PartA soln:

mks = [("maths", 70), ("eng",60),("swa",74),("sci",65),("sos",78)]
total =0 # create this variable outside the loop so that you dont lose it
for i in mks:
    
    #if i[1] !=70: # if you want to excempt maths

    total= total + i[1]
    print ("Total Marks: ", total)

##PartB Soln:
    break
avg= total /len(mks)
print ("Avarage Mark: ", avg)

#Finding grades soln:
mks= int(input("Enter Marks Awarded: "))
mks >= 0 and mks <= 100

if mks >= 79:
    print ("A")
elif mks >=60 and mks <79:
    print ("B")
elif mks >=50 and mks <60:   
    print ("C")
elif mks >=40 and mks <50:   
    print ("D")   
elif mks < 40:
    print ("E") 



   


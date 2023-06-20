# Write a normal python program that calculates the total marks from:
# maths = 70
# maths = 70
# eng=  60
# swa = 74
# sci = 65
# sos = 78
# on the same program, the average marks ,then use the average to find the grade using the table below:
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

#Part1 soln:
mks = [("maths", 70), ("eng",60),("swa",74),("sci",65),("sos",78)]
a=("maths")
b=("eng")
c=("swa")
d=("sci")
e=("sos")

total=0
def mkscalc(a,b,c,d,e):
    total= a+b+c+d+e
    return total

totalmarks= mkscalc(70,60,74,65,78)
avgmks = totalmarks/len(mks)

print ("Total Marks: ", totalmarks)
print ("Average Mark: ", avgmks)
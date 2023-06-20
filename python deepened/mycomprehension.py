lsstudents =[
    {"name":"John", "marks":50}, 
    {"name":"Dan", "marks":40},
    {"name":"Mary", "marks":80},
    {"name":"Jane", "marks":45},
    {"name":"Alex", "marks":90}
    ]                   

#create a new list of student names above 50
res = []

for i in lsstudents:# i is a dictionary
    if i ["marks"] > 50:
     #using a dict to pass names
        res.append(i["name"])

print(res)

#METHOD TWO
def tester(): #if working with a function

    lsstudents = [
    {"name":"John", "marks":50}, 
    {"name":"Dan", "marks":40},
    {"name":"Mary", "marks":80},
    {"name":"Jane", "marks":45},
    {"name":"Alex", "marks":90}
    ]                   

#create a new list of student names above 50
    res = []

    for i in lsstudents:# i is a dictionary
        if i ["marks"] > 50:
     #using a dict to pass names
            res.append(i["name"])
    return res

t = tester()
print(t)

#METHOD THREE
lsstudents =[
    {"name":"John", "marks":87}, 
    {"name":"Dan", "marks":40},
    {"name":"Mary", "marks":80},
    {"name":"Jane", "marks":45},
    {"name":"Alex", "marks":90}
    ]                   

# #create a new list of student names above 50
# res = []

# for i in lsstudents:# i is a dictionary
#     if i ["marks"] > 50:
#      #using a dict to pass names
#         res.append(i["name"])

# print(res)
resnew = [i['name'] for i in lsstudents if (i['marks'] > 70 and i['marks'] < 90) ]
print(resnew)


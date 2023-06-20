taskList = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]


#print (taskList)
# print(tasklist.values())
# print(tasklist[0]())

#1. Determining class of taskList using an inbuilt function
#print(type(taskList))

#2. Print KES
#print(taskList[2][2]["currency"])

#3. Print 560
#print(taskList[2][1])

#4. Use a function to determine the length of taskList
#print(len(taskList))

#5. Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.

#6. Change the name “John” to “Jane” . 
# taskList[4] =list(taskList[4])
# taskList[4][1]='Jane'
# taskList[4] = tuple(taskList[4])
# print(taskList[4])


#7. In the dictionary with the key currency, add another key “amount” with value 90
# taskList[2][2]["amount"]=90
# print (taskList)


#print (taskList)

# colors = ["red", "green", "burnt sienna", "blue"]
# print(colors.index("yellow"))


#Qn: What is the expression that returns the 'z' in 'baz'?
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
temp = x[3][1]
temp =list (temp)
print (x[3][1])
# TASK 10: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.

# prods = [[‘omo’,’30kshs’,300], [‘milk’,’50kshs’,200],[‘bread’,’45kshs’,359], [‘coffee’,’5kshs’,’79’]]

# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.
# Once you learn functions,revisit this and write this code inside a function.

prods = [['omo','30kshs',300], ['milk','50kshs',200],['bread','45kshs',359], ['coffee','5kshs',79]]
# #print (prods[0][2]+prods[1][2]+prods[2][2]+int(prods[3][2]))
# print ('Total Stocks', (prods[0][2]+prods[1][2]+prods[2][2]+int(prods[3][2])))
print ('Total Stocks', (prods[0][2]+prods[1][2]+prods[2][2]+int(prods[3][2])))

for i in count (prods):

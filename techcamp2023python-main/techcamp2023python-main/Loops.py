# ls1 =list(range(0,11))
# print (ls1)

# for i in ls1:
#     print ("now ken is",i)


# for i in range(0,11):
#   if i % 2 == 0:
#    print(i)
#   else: 
#    pass

ls2 = [("E", 40), ("A",30),("B",65)]
total =0 # create this variable outside the loop so that you dont lose it
for i in ls2:
    
    #if i[1] !=40:
        total= total + i[1]
  

        #if i[1]== 30:
    #break
    #avg= total /len(ls2)
    #print (avg)
print (total)


lazy_dog = "The lazy dog ran so fast it hit the wall" # to display “The lazy dog; ran so fast; it hit the wall.”
sliced_lazy_dog1=lazy_dog[0:12]
sliced_lazy_dog2=lazy_dog[13:24]
sliced_lazy_dog3=lazy_dog[25:40]
#print (sliced_lazy_dog1 +'; ' + sliced_lazy_dog2 +'; ' + sliced_lazy_dog3 +'.')

#Intergers
x=3
x*=3
#print (x)

#comparison operators result is a boolean
#print (3 < 10)
#print (3 >=10)
#print (3 !=10)
#print (3 ==10)
#print (3!=4)

#logical operator 'And' 'or'

#Assignment
# p= 16
# m= 13
# m+= 16
# print(m)

# m -= 16
# print(m)

# m=m*16
# print(m)

# m /= p
# print(m)

# m %= p #expotential shows remainder only
# print(m)

#converting floats to intergers
#temp=56.8926 # to 57 through casting
#print(float(temp))


temp=56.8926 # to 56.90 you use slicng and concantination then you convert back to a float
#sliced_temp_qn2= float.temp[0:4]
#round_temp= round (round_temp,2)
#print (format(temp, ".2f"))


# print(round(temp,2))
# print(round(temp,3))

string_temp =str (temp)

first_part =string_temp[3:4]
second_part = string_temp[4:] 
new_string =first_part + '.' + second_part
temp = float(new_string)
print(temp)
print(type(temp))


# sliced_temp_qn3=temp[0:6]
# print (sliced_temp_qn3)

# temp += 0.1
# print (temp)

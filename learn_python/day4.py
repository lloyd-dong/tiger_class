number = [4, 3.2, 5, 9 ,10]
sum = 0
for i in number :
	sum = sum + i
print( "i is {} ".format(t))
count =0
while count < len(number):
	sum = sum + number[count]
	count +=  1


average = float(sum) / len(number)

print("the numbers are {}".format(number))
print("the average is {}".format(average))

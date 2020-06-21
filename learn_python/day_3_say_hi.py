#final ver
def say_hi(name, city):
	print("Wecome {} from {} \n".format(name, city))

people =[]
name = input("What's your name? ")

while name != "bye":
	city = input("which city are you from? ")
	say_hi(name,city)
	people.append(name)
	name = input("What's your name? ")

print("I have said Hi to {} people".format(len(people)))
print("bye bye! " + ", ".join(people))

exit()

#ver 1  while loop
name = input("What's your name? ")
while name != "bye":
	print("hi " + name)
	name = input("What's your name? ")
exit()
#ver2 add a city
name = input("What's your name? ")
while name != "bye":
	city = input("which city are you from? ")
	print("welcome " + name + " from " + city)
	name = input("What's your name? ")

# ver 2.4 \n
	print("welcome " + name + " from " + city +"\n")
# ver 2.5 moden str template
	print("Wecome {} from {} \n".format(name, city))

#ver3  function with/without parameter
def say_hi(name, city):
	print("Wecome {} from {} \n".format(name, city))

name = input("What's your name? ")
while name != "bye":
	city = input("which city are you from? ")
	say_hi(name,city)
	name = input("What's your name? ")

#ver final list
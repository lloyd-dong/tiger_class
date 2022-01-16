
class Person:
	def __init__(self, name, height, weight):
		self.name = name
		self.height = height
		self.weight = weight
		

	def calculateBMI(self):
		BMI = float(self.weight) / pow(float(self.height),2)
		return round(BMI,2)


with open("input.csv", 'r') as f:
	for line in f.readlines():
		name, height, weight = line.split(',')
		person = Person(name, height, weight)
		print("{}'s BMI is {}".format(person.name, person.calculateBMI()))


# def main():

# 	with open("input.txt", 'r') as f:
# 		for line in f.readlines():
# 			name, height, weight = line.split(',')
# 			person = Person(name, height, weight)
# 			print("{}'s BMI is {}".format(person.name, person.calculateBMI()))

# if __name__ == "__main__":
# 	main()
import random

bottles_of_cola = 10
cola = ["pepsi" if random.random() > random.random() else "coca" for i in range(bottles_of_cola)]

def my_guess():
	return "pepsi" if random.random()> 0.5 else "coca"

print("cola is {}".format(cola))

count = 1000
results = []
for i in range(count):
	result = []
	for c in cola:
		result.append(1 if my_guess() == c else 0)
	# print("{}: {}, sum: {}".format(count, result, sum(result)))
	results.append(result)


# how many times are correct in one round
criteria = 4
correct = 0
for rs in results:	
	sum_ = sum(rs)	
	if sum_ == criteria:
		correct +=1

print("correct {} in {}, criteria: {}, ratio ={}%".format(correct,count, criteria, round(100*float(correct)/count,2)))
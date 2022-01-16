from scipy.special import comb
import numpy as np

bottles_of_cola = 10
total = pow(2,bottles_of_cola)

data = []
for i in range(bottles_of_cola+1):
	data.append(comb(bottles_of_cola,i))
pdf = np.around(np.divide(data, total),4)
cdf = np.around(np.cumsum(pdf),3)
print("sum: {}, data: {}".format(sum(data),data))
print("pdf: {}".format(pdf))
print("cdf: {}%".format(cdf))


import matplotlib.pyplot as plt
# plt.plot(range(0, len(data)),data)
plt.plot(range(0, len(data)),pdf)
plt.plot(range(0, len(data)),cdf)
plt.show()
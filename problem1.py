R = 0
for x in range(1000):
	if(x % 3 == 0 or x%5 == 0):
		R += x
print("The result is : {}".format(R))
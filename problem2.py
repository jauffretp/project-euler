X1 = 0
X2 = 1
R = 0
while(X2 <= 4000000):
	X2 = X1 + X2
	X1 = X2 - X1
	#print("X1 : {} X2 : {}".format(X1,X2))
	if(X2 % 2 == 0):
		R += X2

print("The result is : {}".format(R))
R = 0
N = 100
for x  in range(1,N+1):
	for y in range(x,N+1):
		if(x != y):
			#print("X : {} Y : {}".format(x,y))
			R += 2*x*y

print(R)
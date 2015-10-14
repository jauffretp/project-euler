
N = 1000000
L = [x for x in range(2,N+1)]

#print(L)
i = 0
while(i < len(L)):
	print(L[i])
	for Y in L[i+1:len(L)]:
		if(Y % L[i] == 0):
			#print(Y)
			L.remove(Y)
	i += 1


print("Len L : {} L10000 : {} L9999 : {} L : 10001 {} ".format(len(L), L[10000], L[9999], L[10001]))


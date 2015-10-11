import math

def is_palindrome(N):
	S = str(N)
	N = len(S)
	R = True
	for i in range(0,math.floor(N/2)):
		if(S[i] != S[N-i-1]):
			R = False
	return R

print("Is 10101 a palindrome ? : {}".format(is_palindrome(10101)))

print("Is 102101 a palindrome ? : {}".format(is_palindrome(102101)))

print("Is 1001 a palindrome ? : {}".format(is_palindrome(1001)))

print("Is 123321 a palindrome ? : {}".format(is_palindrome(12321)))

print("Is 1 a palindrome ? : {}".format(is_palindrome(1)))

print("Is 12 a palindrome ? : {}".format(is_palindrome(12)))



not_found = True
X = 999

L = []


while( X >= 1 and len(L) <= 5):
	Y = 999
	while(Y >= X and len(L) <= 5):
		print("X : {} Y : {} X*Y : {} Length L : {}".format(X,Y, X*Y, len(L)))
		if(is_palindrome(X*Y)):
			L.append(X*Y)
		Y -= 1
	X -= 1

print(L)
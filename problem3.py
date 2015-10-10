
R = 0
N = 600851475143

current_number = N
current_divisor = 2
largest_divisor = 0

while(current_number > 1):
	if(current_number % current_divisor == 0):
		current_number = current_number/current_divisor
		largest_divisor = current_divisor
		current_divisor = 2
	else:
		current_divisor += 1

print(largest_divisor)
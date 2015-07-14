def largePrime(n):
	count = 0
	for i in range(1, n+1, 1):
		if n % i == 0:
			for iterator in range(2, i, 1):
				if i % iterator == 0:
					break
				else:
					if i != n:
						count = i

	print count
#			for x in range(2, i, 1):
#				if i % x == 0:
#					flagger += 1
#				else:
#					count = i
	#print count

# largePrime(13195)

# idea:
# branches: take the number n, and increment division possibilities
# i.e check n % 1 == 0, n % 2 == 0, ... but instead of 1, 2, add a check
# in this check, make it so that the n's are divided only by primes 
# (make a list of primes from 2 to below the original number using a forloop-append)
# when n % x == 0, add x to a list of prime factors
# then get the result quot = n / x
# repeat the n % 1, n % 2 increment with quot
# quot % x == 0; here x is another prime
# repeat until no further division can take place
# extract the list of primes
# print the highest prime
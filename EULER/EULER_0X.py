def fibonacci(nx):
	if nx == 0:
		return 0
	elif nx == 1:
		return 1
	else:
		nx -= 1
		return fibonacci(nx) + fibonacci(nx-1)

print fibonacci(6)

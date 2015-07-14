def fibonacci(nx):
	if nx == 0:
		return 0
	elif nx == 1:
		return 1
	else:
		nx -= 1
		return fibonacci(nx) + fibonacci(nx-1)

def main():
	x = int(raw_input("Enter FIBONACCI term number: "))
	print fibonacci(x)

if __name__ == "__main__":
	main()

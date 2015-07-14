def multiple_sum():
	count = 0
	for value in range(1000):
		if value % 3 == 0 or value % 5 == 0:
			count += value
	return count

def main():
	print multiple_sum()

if __name__ == "__main__":
	main()
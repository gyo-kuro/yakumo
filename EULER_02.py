# if __name__ == "__main__":
#	main()

def fiboseq():
	count = 1
	back = 1
	summ = 0
	while count < 3000000:
		count = count + back
		print count
		if count % 2 == 0:
			summ += count
		back = count - back
	print summ

fiboseq()
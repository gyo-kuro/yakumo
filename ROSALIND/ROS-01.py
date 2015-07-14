from sys import argv

script, filename = argv

txt = open(filename)

def dna_bases():

	gua = 0
	cyt = 0
	ade = 0
	thy = 0
	null = 0

	dna_string = txt.read()
	checkstring = dna_string.lower()
	for base in checkstring:
		if base == "g":
			gua += 1
		elif base == "c":
			cyt += 1
		elif base == "a":
			ade += 1
		elif base == "t":
			thy += 1
		else:
			null += 1

	return str(ade) + " " + str(cyt) + " " + str(gua) + " " + str(thy)

def main():
	print dna_bases()

if __name__ == "__main__":
	main()






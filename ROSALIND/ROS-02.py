from sys import argv

script, filename = argv

txt = open(filename)

def rna_transcription():

	template = txt.read()
	templow = template.lower()

	rna = ""

	for base in templow:
		if base == "t":
			rna += "u"
		else:
			rna += base

	fullrna = rna.upper()
	return fullrna

def main():
	with open("Output.txt","w") as text_file:
		text_file.write("{}".format(rna_transcription()))

if __name__ == "__main__":
	main()






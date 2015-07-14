from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
codestring = txt.read()
for base in codestring:
	print base





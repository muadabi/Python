from sys import argv

script, fileName = argv

txt = open(fileName)

print "Here's your file %r:" % fileName
print txt.read()

print "Type the filename again:"
fileAgain = raw_input("> ")

txtAgain = open(fileAgain)

print txtAgain.read()


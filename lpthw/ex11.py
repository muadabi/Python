# Notice that we put a , (comma) at the end of each print line. This is so that print
# doesn't end the line with a newline and go to the next line.

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %r tall and %r  heavy." % (
        age, height, weight)


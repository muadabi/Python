# A string is asually a bit of text you want to display to someone, or "export" out
# of the program you are writing. Python know you want somethingto be a string when
# you put either " (double-quotes) or ' (single-quotes) around the text.



x = "There are %d types of people." %10
binary = "binary"
doNot = "don't"
y = "Those who know %s and those who %s." % (binary, doNot)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
jokeEvaluation = "Isn't that joke so funny?! %r"

print jokeEvaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e


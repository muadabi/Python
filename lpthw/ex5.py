# -- coding: utf-8 --
myName = 'Zed A. Shaw'
myAge = 35 # Not a lie
myHeight = 74 #inches
myWeight = 180 #lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'

print "Let's talk about %s." % myName # format string
print "He's %d inches tall." % myHeight
print "He's %d pounds heavy." % myWeight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (myEyes, myHair)
print "His teeth are usually %s depending on the coffee." % myTeeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	myAge, myHeight, myWeight, myAge + myHeight + myWeight)

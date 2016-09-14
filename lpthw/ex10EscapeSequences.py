# "escape sequences"
# \\ Blackslash ()
# \' Single quote (')
# \" Double quotes (")
# \a ASCII Bell (BEL)
# \b ASCII Backspace (BS)
# \f ASCII Formfeed (FF)
# \n ASCII Linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII Carriage Return (CR)
# \t ACSCII Horizontal Tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v ASCII Vertical Tab (VT)
# \ooo Character with octal value ooo
# \xhh Character with hex value hh

tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non aline."
blackslashCat = "I'm \\ a \\ cat."

fatCat = """
I'll do a list:
    \t* Cat food
    \t* Fishes
    \t* Catnip\n\t* Grass
"""

print tabbyCat
print persianCat
print blackslashCat
print fatCat

# Here's a tiny piece of fun code to try out:

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,


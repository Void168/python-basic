# String data type

# literal assignment
import math
first = "Le"
last = "Hung"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))

# constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#  Casting a number to a string
decade = str(2000)
print(type(decade))
print(decade)

statement = "I like indie ballad music from the " + decade + "s."
print(statement)


# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                                All good?

'''

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                          "
multiline = "                   " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, '.') + "$1".rjust(4))
print("Muffin".ljust(16, '.') + "$2".rjust(4))
print("CheeseCake".ljust(16, '.') + "$4".rjust(4))

# string index value
print(first[-1])
print(last[1:-1])

print(math.pi)

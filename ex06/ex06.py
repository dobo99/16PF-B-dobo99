x = "There are %d types of people." % 10
# simple word can locate '=''s left side
binary = "binary"
# using like this format because make simple sentence
do_not = "don't"
# also this can change few words into another word
y = "Those who know %s and those who %s." % (binary, do_not)
# We can put the string into another string

print x
# I define x in 1st line
print y
# 7th line defines what is y

print "I said: %r." % x
# we can use %r to put in another string
print "I also said: '%s'" % y
# %s is used when we put in the word

hilarious = False
# hilarious equal false in next sentence
joke_evaluation = "Isn't that joke so funny?! %r"
# '=' defines what is that mean

print joke_evaluation % hilarious
# If we define word in previous string, we can use just word without ''or ""

w = "This is the left side of..."
# simple word can equal the sentence
e = "a string with a right side."
# It is comfortable when you define frequently used sentence to simple word

print w+e
# using '+' to plus two sentence
# changing long centence to simple word can easily make long sentence
# or print same sentence in diffrent location at once
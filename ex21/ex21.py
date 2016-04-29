def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
# define calculation order. print formula and return answer
# same process about blow three define

def subtract (a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DEVIDING %d / %d" % (a,b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# printing process is inside to outside. print inside first

print "That becomes: ", what, "Can you do me a hand?"
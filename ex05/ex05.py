name = 'Lee'
age = 25
height_cm = 175
weight_kg = 70
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height_cm
print "He's %d pounds heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height_cm, weight_kg, age + height_cm + weight_kg)
print "I'll convert centimeters to inches, kilograms to pounds"
print '1 centimeter = 0.39 inch'
print '1 kilogram = 2.2 pound'
print 'converting %d cm to %d in' % (height_cm, height_cm*0.39)
print 'converting %d kg to %d lbs' % (weight_kg, weight_kg*2.2)
print "What is %r?"
print '%r' % 'print this no matter what'
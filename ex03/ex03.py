#-*-coding:cp949
print "I will now count my chickens:"

print "Hens", 25.0 + 30.0 / 6.0
# * and / is caculating faster than +,-
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0
# % is kind of dividing, but print remaining part

print "Now I will count the eggs:"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
# 1/4 is 0.25. It round off below decimal point
print "If I print 3+2+1-5+4%2-1.0/4.0+6,", 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6
# Writing this way has more accuracy than previous way
print "Is it true that 3+2<5-7?"

print 3 + 2 < 5 - 7
# when I printing < or >, it shows true or false

print "What is 3+2?", 3.0 + 2.0
# equations inside of "" are just word. Outside of "" is real equation
print "What is 5-7?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
print 10.5, 0.89, 3.0
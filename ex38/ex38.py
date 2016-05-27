ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
# split words that in the stuff list to one word
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # order 'while' is repeating order continuous
    next_one = more_stuff.pop() # 'pop' is selection a word in the list and out the list
    # put number in () for selecting a word. if nothing in (), popping right to left
    print "Adding: ", next_one
    stuff.append(next_one) # 'append' is adding the word that in () to the list
    print "There are %d items now." % len(stuff) # 'len' shows how much words that the list have

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # numbering left to right, start with 0. this shows 2nd word from left
print stuff[-1] # whoa! fancy # numbering right to left, start with -1. this shows first word from right
print stuff.pop() # 'pop()' shows very right word in the list. same as 'pop(-1)'
print ' '.join(stuff) # what? cool! # 'join' shows every words in the list
print '#'.join(stuff[3:5]) # super stellar! # [3:5] means showing up 4th and 5th word in the list from left

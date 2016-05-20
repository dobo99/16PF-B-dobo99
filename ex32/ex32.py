the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# use [] to make a list

# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)
    # print with the list 'the_count'. list's elements regard as number

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
    # print with the list 'fruits'

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print("I got %r" % i)
    # this is same as above. change list's elements regard as i

# we can also build lists. first start with an empty one
elements = []
# this is empty list

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to list." % i)
    # append is a function that list understand
    elements.append(i)
# range(0,6) means start with 0 and print 6 times, not to 6
# this statement make list of elements. 0 to 5 will be put in the list

# now we can print them out too
for i in elements:
    print("Element was: %d" % i)
# print this with the list 'element'
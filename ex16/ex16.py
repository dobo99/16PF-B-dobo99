from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#'w' means write. so this cammand will open the file
#'target' command will targeting the file what I want to

print "Truncating the file. Goodbye!"
target.truncate()
#truncate is delete. everything in that file will delete

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#target in here is what I targeting in line 12

print "And finally, we close it."
target.close()
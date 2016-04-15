from sys import argv

script, filename = argv

txt = open(filename)
# I make ex15_sample.txt file before, so if I write file name with txt, this file will open

print "Here's your file %r:" % filename
#I write file name in script parameter. it will show up
print txt.read()
#txt equals open file in line 5. command read will print ex15_sample.txt file

print "Type the filename again:"
file_again = raw_input("> ")
#write file name exactly same with .txt

txt_again = open(file_again)
#It's the same with in line 5

print txt_again.read()
# It will print what I write in line 14(raw_input)
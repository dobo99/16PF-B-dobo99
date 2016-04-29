from sys import argv
# take a module 'argv' from system

script, input_file = argv
# script and input_file are variables

def print_all(f):
    print (f.read())
# define 'print_all' to print string in reading file

def rewind(f):
    f.seek(0)
# define 'rewind' to seek 0 byte(rewind first of the file)

def print_a_line(line_count, f):
    print("%d %s" % (line_count, f.readline()))
# define 'print_a_line' to print reading file's 'line_count(number)'st string

current_file = open(input_file)
# order 'current_file' is opening file

print("first let's print the whole file:\n")
# printing

print_all(current_file)
# read current_file's strings and printing

print("Now let's rewind, kind of like a tape")
# printing

rewind(current_file)
# return to the first string of current_file, literally first

print("Let's print three lines:")
# printing

current_line = 1
print_a_line(current_line, current_file)
# print current_file's 1st string

current_line = current_line + 1
print_a_line(current_line, current_file)
# print current_file's 2nd string

current_line = current_line + 1
print_a_line(current_line, current_file)
# print current_file's 3rd string
people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
# print this string When cars' number is more then people's.
elif cars < people:
    print("We should not take the cars.")
# elif is running when the forward if-statement is false.
else:
    print("We can't decide.")
# else is running when forward if-statements are all false.

if trucks > cars:
    print("That's too many trucks.")
# trucks number is 15, cars number is 40. so this will not print.
elif trucks < cars:
    print("Maybe we could take the trucks.")
# the forward if-statement is false, so this can be running.
# this if-statement is true. this will print
else:
    print("We still can't decide.")
# the forward if-statement is true. this will not run

if people > trucks:
    print("Alright, let's just take the trucks.")
# this if statement is true, so this will print
else:
    print("Fine, let's stay home then.")
# else have all possibility except forward if-statements'.
# the forward if-statement is true, so this will not run.

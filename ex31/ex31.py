if "raw_input" not in dir(__builtins__):
    raw_input = input
# I think this is defining what is raw_input. Why defining raw_input is?

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")
# this file is kind of game. this string is starting of the game.

door = raw_input("> ")
# I can select the way to next level.

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2.  Scream at the bear.")
# when I choose door number 1, this strings will be printed.

    bear = raw_input("> ")
    # I can choose many ways to go next level. 1, 2 or anything else.

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)
# These are results what I choose.

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's rstina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revovers yelling melodies.")
# If I choose door number 2, this will be printed

    insanity = raw_input("> ")
# I can choose many ways to go next level. 1, 2, 3, or anything else.

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
# these are results what I choose.

else:
    print("You stumble around and fall on a knife and die. Good job!")
# I can choose the way that I don't choose the door.

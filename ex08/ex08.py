formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "Three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this Thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# why the third string just have "" when the others have ''?
# is it affected by 5th line?